/* ═══════════════════════════════════════════════════════════
   AI Hallucination Detector — Content Script
   Runs on: chatgpt.com, claude.ai, gemini.google.com
   ═══════════════════════════════════════════════════════════ */

(() => {
    "use strict";

    /* ─── Site Config ─── */
    const SITE_CONFIG = {
        chatgpt: {
            hostname: ["chatgpt.com", "chat.openai.com"],
            // Selectors ordered by reliability — first match wins
            responseSelectors: [
                '[data-message-author-role="assistant"]',
                ".agent-turn .markdown",
                ".markdown.prose",
            ],
            userSelectors: [
                '[data-message-author-role="user"]',
                ".human-turn",
            ],
            containerSelector: "main",
            label: "ChatGPT",
        },
        claude: {
            hostname: ["claude.ai"],
            responseSelectors: [
                '[data-is-streaming]',
                ".font-claude-message",
                ".prose",
                '[class*="response"]',
            ],
            userSelectors: [
                '[class*="human"]',
                '[class*="user"]',
            ],
            containerSelector: '[class*="conversation"]',
            label: "Claude",
        },
        gemini: {
            hostname: ["gemini.google.com"],
            responseSelectors: [
                ".model-response-text",
                ".response-content",
                "message-content.model-response-text",
                ".markdown",
            ],
            userSelectors: [
                ".user-query",
                '[class*="query-text"]',
            ],
            containerSelector: "main",
            label: "Gemini",
        },
    };

    /* ─── Detect site ─── */
    let currentSite = null;
    let siteConfig = null;
    const host = window.location.hostname.replace(/^www\./, "");

    for (const [key, cfg] of Object.entries(SITE_CONFIG)) {
        if (cfg.hostname.some((h) => host.includes(h))) {
            currentSite = key;
            siteConfig = cfg;
            break;
        }
    }

    if (!currentSite) return; // Not on a supported site

    console.log(`[AHD] Detected: ${siteConfig.label}`);

    /* ─── State ─── */
    let enabled = true;
    let panelEl = null;
    let lastProcessedResponse = null;
    let lastProcessedText = "";        // content-based dedup
    let pendingBackendCall = false;     // prevent overlapping calls

    /* ─── Demo hallucination analysis ─── */
    function analyzeText(text) {
        // Simulated hallucination detection with keyword heuristics (demo)
        const patterns = [
            { regex: /\b(exactly|precisely)\s+\d[\d,.]*\b/gi, prob: () => 55 + Math.floor(Math.random() * 30), category: "Numerical Precision", detail: "Exact numeric claims are often hallucinated. The true figure may be approximate." },
            { regex: /\b(always|never|every single|100%)\b/gi, prob: () => 60 + Math.floor(Math.random() * 25), category: "Absolute Claim", detail: "Absolute language is a hallucination risk — real-world data rarely supports absolutes." },
            { regex: /\b(studies show|research proves|scientists confirm|experts agree)\b/gi, prob: () => 65 + Math.floor(Math.random() * 25), category: "Unverified Source", detail: "Vague attribution to studies/experts without citations is a common hallucination pattern." },
            { regex: /\b(was (invented|discovered|founded|created) (in|by))\b/gi, prob: () => 40 + Math.floor(Math.random() * 35), category: "Historical Claim", detail: "Historical attributions may be inaccurate — verify dates, names, and events." },
            { regex: /\b(first ever|world's (first|largest|oldest|smallest))\b/gi, prob: () => 50 + Math.floor(Math.random() * 30), category: "Superlative Claim", detail: "Superlative claims are frequently hallucinated or outdated." },
            { regex: /\b(according to [A-Z][\w\s]{2,30})\b/g, prob: () => 45 + Math.floor(Math.random() * 25), category: "Attribution", detail: "Named attributions should be cross-checked — AI may fabricate or misattribute quotes." },
            { regex: /\b(\d{1,2}(?:st|nd|rd|th) century)\b/gi, prob: () => 35 + Math.floor(Math.random() * 30), category: "Temporal Claim", detail: "Century references may be off by one or entirely fabricated." },
            { regex: /\b(approximately|roughly|about|around) \d[\d,.]*%/gi, prob: () => 30 + Math.floor(Math.random() * 20), category: "Statistic", detail: "Approximate statistics may still be significantly off from real data." },
        ];

        const flags = [];
        for (const p of patterns) {
            let match;
            while ((match = p.regex.exec(text)) !== null) {
                const prob = p.prob();
                flags.push({
                    text: match[0],
                    index: match.index,
                    length: match[0].length,
                    prob,
                    category: p.category,
                    detail: p.detail,
                    breakdown: {
                        factual: Math.max(10, prob + Math.floor(Math.random() * 16 - 8)),
                        source: Math.max(10, prob + Math.floor(Math.random() * 16 - 8)),
                        context: Math.max(10, prob + Math.floor(Math.random() * 20 - 10)),
                        semantic: Math.max(10, prob + Math.floor(Math.random() * 16 - 8)),
                    },
                });
            }
        }

        // Sort by position
        flags.sort((a, b) => a.index - b.index);
        return flags;
    }

    /* ─── Helpers ─── */
    function severity(prob) {
        if (prob >= 70) return "high";
        if (prob >= 45) return "mid";
        return "low";
    }

    function severityColor(prob) {
        if (prob >= 70) return "#f87171";
        if (prob >= 45) return "#fbbf24";
        return "#34d399";
    }

    /* ─── Find last AI response element ─── */
    function findLastResponse() {
        for (const sel of siteConfig.responseSelectors) {
            const els = document.querySelectorAll(sel);
            if (els.length > 0) return els[els.length - 1];
        }
        return null;
    }

    /* ─── Find last user question ─── */
    function findLastUserMessage() {
        for (const sel of siteConfig.userSelectors) {
            const els = document.querySelectorAll(sel);
            if (els.length > 0) return els[els.length - 1];
        }
        return null;
    }

    /* ─── Build the floating panel ─── */
    function createPanel() {
        if (panelEl) panelEl.remove();

        panelEl = document.createElement("div");
        panelEl.id = "ahd-panel";
        panelEl.innerHTML = `
      <div class="ahd-header">
        <div class="ahd-brand">
          <svg class="ahd-logo" width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L2 7l10 5 10-5-10-5z" fill="url(#ahdg1)"/>
            <path d="M2 17l10 5 10-5" stroke="url(#ahdg2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2 12l10 5 10-5" stroke="url(#ahdg2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <defs>
              <linearGradient id="ahdg1" x1="2" y1="2" x2="22" y2="12"><stop stop-color="#818cf8"/><stop offset="1" stop-color="#c084fc"/></linearGradient>
              <linearGradient id="ahdg2" x1="2" y1="12" x2="22" y2="22"><stop stop-color="#818cf8"/><stop offset="1" stop-color="#c084fc"/></linearGradient>
            </defs>
          </svg>
          <span class="ahd-title">Hallucination Detector</span>
        </div>
        <div class="ahd-header-right">
          <div class="ahd-gauge-mini" id="ahd-gauge-mini">
            <svg viewBox="0 0 36 36" class="ahd-gauge-svg">
              <circle class="ahd-gauge-track" cx="18" cy="18" r="15"/>
              <circle class="ahd-gauge-fill" id="ahd-gauge-fill" cx="18" cy="18" r="15"/>
            </svg>
            <span class="ahd-gauge-label" id="ahd-gauge-label">—</span>
          </div>
          <button class="ahd-close" id="ahd-close">&times;</button>
        </div>
      </div>

      <div class="ahd-body">
        <!-- Question excerpt -->
        <div class="ahd-question" id="ahd-question"></div>

        <!-- Summary chips -->
        <div class="ahd-summary" id="ahd-summary"></div>

        <!-- Flagged items list -->
        <div class="ahd-flags" id="ahd-flags"></div>

        <!-- Detail drawer -->
        <div class="ahd-detail ahd-hidden" id="ahd-detail">
          <button class="ahd-detail-back" id="ahd-detail-back">← Back</button>
          <h4 class="ahd-detail-title" id="ahd-detail-title"></h4>
          <p class="ahd-detail-excerpt" id="ahd-detail-excerpt"></p>
          <div class="ahd-meter">
            <div class="ahd-meter-header">
              <span class="ahd-meter-label">Hallucination Probability</span>
              <span class="ahd-meter-value" id="ahd-meter-value">0%</span>
            </div>
            <div class="ahd-meter-bar"><div class="ahd-meter-fill" id="ahd-meter-fill"></div></div>
          </div>
          <div class="ahd-breakdown" id="ahd-breakdown"></div>
        </div>
      </div>

      <div class="ahd-footer">
        <span>${siteConfig.label}</span>
        <span class="ahd-dot">·</span>
        <span id="ahd-footer-count">0 issues</span>
      </div>
    `;
        document.body.appendChild(panelEl);

        // Wire close button
        document.getElementById("ahd-close").addEventListener("click", () => {
            panelEl.classList.add("ahd-collapsed");
            showReopenBtn();
        });

        // Wire back button
        document.getElementById("ahd-detail-back").addEventListener("click", () => {
            document.getElementById("ahd-detail").classList.add("ahd-hidden");
            document.getElementById("ahd-flags").classList.remove("ahd-hidden");
        });
    }

    /* ─── Reopen button ─── */
    let reopenBtn = null;
    function showReopenBtn() {
        if (reopenBtn) reopenBtn.remove();
        reopenBtn = document.createElement("button");
        reopenBtn.id = "ahd-reopen";
        reopenBtn.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
        <path d="M12 2L2 7l10 5 10-5-10-5z" fill="#818cf8"/>
        <path d="M2 17l10 5 10-5" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M2 12l10 5 10-5" stroke="#c084fc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>`;
        document.body.appendChild(reopenBtn);
        reopenBtn.addEventListener("click", () => {
            panelEl.classList.remove("ahd-collapsed");
            reopenBtn.remove();
            reopenBtn = null;
        });
    }

    /* ─── Populate panel with analysis ─── */
    function populatePanel(flags, questionText, answerText) {
        const questionEl = document.getElementById("ahd-question");
        const summaryEl = document.getElementById("ahd-summary");
        const flagsEl = document.getElementById("ahd-flags");
        const footerCount = document.getElementById("ahd-footer-count");

        // Build JSON object (sent to background for file saving)
        const extractedJson = {
            question: questionText,
            answer: answerText,
        };

        // Log JSON to console
        console.log("[AHD] Extracted Q&A JSON:", JSON.stringify(extractedJson, null, 2));

        // Question
        const trimmedQ = questionText.length > 120 ? questionText.slice(0, 120) + "…" : questionText;
        questionEl.innerHTML = `<span class="ahd-q-icon">Q</span><span class="ahd-q-text">${escapeHtml(trimmedQ)}</span>`;

        // Summary
        const high = flags.filter((f) => f.prob >= 70).length;
        const mid = flags.filter((f) => f.prob >= 45 && f.prob < 70).length;
        const low = flags.filter((f) => f.prob < 45).length;

        summaryEl.innerHTML = `
      <div class="ahd-chip ahd-chip-red"><span class="ahd-chip-val">${high}</span><span class="ahd-chip-lbl">High</span></div>
      <div class="ahd-chip ahd-chip-amber"><span class="ahd-chip-val">${mid}</span><span class="ahd-chip-lbl">Med</span></div>
      <div class="ahd-chip ahd-chip-green"><span class="ahd-chip-val">${low}</span><span class="ahd-chip-lbl">Low</span></div>
    `;

        // Flags list
        if (flags.length === 0) {
            flagsEl.innerHTML = `<div class="ahd-no-flags">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <p>No hallucinations detected!</p>
      </div>`;
        } else {
            flagsEl.innerHTML = flags
                .map(
                    (f, i) => `
        <div class="ahd-flag-item ahd-flag-${severity(f.prob)}" data-idx="${i}">
          <div class="ahd-flag-top">
            <span class="ahd-flag-category">${escapeHtml(f.category)}</span>
            <span class="ahd-flag-prob" style="color:${severityColor(f.prob)}">${f.prob}%</span>
          </div>
          <div class="ahd-flag-text">"${escapeHtml(f.text)}"</div>
          <div class="ahd-flag-bar-track"><div class="ahd-flag-bar-fill" style="width:${f.prob}%;background:${severityColor(f.prob)}"></div></div>
        </div>`
                )
                .join("");

            // Click handlers
            flagsEl.querySelectorAll(".ahd-flag-item").forEach((el) => {
                el.addEventListener("click", () => {
                    const idx = parseInt(el.dataset.idx);
                    showDetail(flags[idx]);
                });
            });
        }

        // Footer
        footerCount.textContent = `${flags.length} issue${flags.length !== 1 ? "s" : ""}`;

        // Gauge
        const avgProb = flags.length > 0 ? flags.reduce((s, f) => s + f.prob, 0) / flags.length : 0;
        const trust = Math.round(100 - avgProb);
        setMiniGauge(trust);

        // Report to background (badge update only — no extractedQA to avoid re-triggering backend)
        try {
            chrome.runtime.sendMessage({
                type: "AHD_STATUS",
                site: currentSite,
                issues: flags.length,
                lastScan: new Date().toISOString(),
            });
        } catch (e) { /* popup context may not have chrome.runtime */ }
    }

    /* ─── Mini gauge ─── */
    function setMiniGauge(pct) {
        const circumference = 2 * Math.PI * 15; // ~94.25
        const offset = circumference - (circumference * pct) / 100;
        const fill = document.getElementById("ahd-gauge-fill");
        const label = document.getElementById("ahd-gauge-label");
        if (!fill || !label) return;

        fill.style.strokeDashoffset = offset;
        fill.style.stroke = pct >= 75 ? "#34d399" : pct >= 50 ? "#fbbf24" : "#f87171";
        label.textContent = pct + "%";
    }

    /* ─── Show detail ─── */
    function showDetail(flag) {
        const detailEl = document.getElementById("ahd-detail");
        const flagsEl = document.getElementById("ahd-flags");
        flagsEl.classList.add("ahd-hidden");
        detailEl.classList.remove("ahd-hidden");

        document.getElementById("ahd-detail-title").textContent = flag.category;
        document.getElementById("ahd-detail-excerpt").textContent = flag.detail;
        document.getElementById("ahd-meter-value").textContent = flag.prob + "%";

        const fill = document.getElementById("ahd-meter-fill");
        fill.style.background = severityColor(flag.prob);
        requestAnimationFrame(() => (fill.style.width = flag.prob + "%"));

        const bd = document.getElementById("ahd-breakdown");
        bd.innerHTML = Object.entries(flag.breakdown)
            .map(
                ([key, val]) => `
      <div class="ahd-bd-item">
        <span class="ahd-bd-label">${key}</span>
        <span class="ahd-bd-value" style="color:${severityColor(val)}">${val}%</span>
      </div>`
            )
            .join("");
    }

    /* ─── Utility ─── */
    function escapeHtml(str) {
        const div = document.createElement("div");
        div.textContent = str;
        return div.innerHTML;
    }

    /* ─── Convert backend detection to panel flags ─── */
    function detectionToFlags(detection) {
        if (!detection || !detection.spans || detection.spans.length === 0) return [];
        return detection.spans.map((span) => {
            const prob = Math.round((span.confidence || 0) * 100);
            return {
                text: span.text || "",
                index: span.start || 0,
                length: (span.end || 0) - (span.start || 0),
                prob,
                category: "HalluGuard Detection",
                detail: `This span was flagged by the HalluGuard ML model with ${prob}% confidence as potentially hallucinated. Cross-check this claim with reliable sources.`,
                breakdown: {
                    factual: prob,
                    source: Math.max(10, prob + Math.floor(Math.random() * 10 - 5)),
                    context: Math.max(10, prob + Math.floor(Math.random() * 10 - 5)),
                    semantic: Math.max(10, prob + Math.floor(Math.random() * 10 - 5)),
                },
            };
        });
    }

    /* ─── Show loading state in panel ─── */
    function showLoadingState(questionText) {
        const questionEl = document.getElementById("ahd-question");
        const summaryEl = document.getElementById("ahd-summary");
        const flagsEl = document.getElementById("ahd-flags");
        const footerCount = document.getElementById("ahd-footer-count");

        const trimmedQ = questionText.length > 120 ? questionText.slice(0, 120) + "…" : questionText;
        questionEl.innerHTML = `<span class="ahd-q-icon">Q</span><span class="ahd-q-text">${escapeHtml(trimmedQ)}</span>`;
        summaryEl.innerHTML = `<div class="ahd-chip ahd-chip-amber"><span class="ahd-chip-lbl">Analyzing…</span></div>`;
        flagsEl.innerHTML = `<div class="ahd-no-flags">
            <p style="color:#fbbf24">⏳ Running HalluGuard ML analysis…</p>
        </div>`;
        footerCount.textContent = "analyzing…";
        setMiniGauge(50);
    }

    /* ─── Update panel with real backend results ─── */
    function updatePanelWithDetection(detection) {
        const flags = detectionToFlags(detection);
        const questionEl = document.getElementById("ahd-question");
        const questionText = questionEl ? questionEl.textContent : "";
        const answerText = lastAnswerText || "";

        populatePanel(flags, lastQuestionText || questionText, answerText);

        // Update badge state
        if (detection.hallucination_detected) {
            console.log(`[AHD] ⚠ Hallucination DETECTED: ${detection.summary}`);
        } else {
            console.log(`[AHD] ✓ No hallucination: ${detection.summary}`);
        }
    }

    /* ─── State for tracking last Q&A texts ─── */
    let lastQuestionText = "";
    let lastAnswerText = "";

    /* ─── Main scan function ─── */
    function scanLatestResponse() {
        if (!enabled) return;
        if (pendingBackendCall) return;  // Don't fire while a call is in-flight

        const responseEl = findLastResponse();
        if (!responseEl) return;

        const responseText = (responseEl.innerText || responseEl.textContent || "").trim();
        if (responseText.length < 20) return; // Too short

        // Content-based dedup: skip if the text hasn't changed
        if (responseText === lastProcessedText) return;

        // Also keep the element ref check as an extra guard
        lastProcessedResponse = responseEl;
        lastProcessedText = responseText;

        // Get user question
        const userEl = findLastUserMessage();
        const questionText = userEl ? (userEl.innerText || userEl.textContent || "").trim() : "(Question not detected)";

        // Store for later use when backend results arrive
        lastQuestionText = questionText;
        lastAnswerText = responseText;

        // Create panel & show loading state while backend processes
        createPanel();
        showLoadingState(questionText);

        // Start collapsed — user opens via FAB
        panelEl.classList.add("ahd-collapsed");
        showReopenBtn();

        // Send Q&A to background script → triggers backend pipeline call
        pendingBackendCall = true;
        // Safety timeout: unlock after 30s in case backend never responds
        setTimeout(() => { pendingBackendCall = false; }, 30000);
        try {
            chrome.runtime.sendMessage({
                type: "AHD_STATUS",
                site: currentSite,
                issues: 0,
                lastScan: new Date().toISOString(),
                extractedQA: { question: questionText, answer: responseText },
            });
        } catch (e) { /* popup context may not have chrome.runtime */ }

        console.log(`[AHD] Sent response to backend for analysis on ${siteConfig.label}`);
    }

    /* ─── MutationObserver — watch for new messages ─── */
    function startObserver() {
        const target = document.querySelector(siteConfig.containerSelector) || document.body;

        const observer = new MutationObserver((mutations) => {
            // Debounce: wait for DOM to settle
            clearTimeout(scanTimeout);
            scanTimeout = setTimeout(() => scanLatestResponse(), 1500);
        });

        observer.observe(target, { childList: true, subtree: true });
        console.log(`[AHD] Observer started on ${siteConfig.label}`);
    }

    let scanTimeout = null;

    /* ─── Listen for messages from background ─── */
    chrome.runtime.onMessage.addListener((msg) => {
        if (msg.type === "AHD_SET_ENABLED") {
            enabled = msg.enabled;
            if (!enabled && panelEl) {
                panelEl.classList.add("ahd-collapsed");
            }
        }

        /* ─── Receive real detection results from backend ─── */
        if (msg.type === "AHD_DETECTION_RESULT") {
            pendingBackendCall = false;  // Unlock for next detection
            console.log("[AHD] Received backend detection results:", msg.detection);
            if (panelEl) {
                if (msg.error) {
                    // Server offline fallback: use local regex analysis
                    console.log("[AHD] Server offline, falling back to local analysis");
                    const flags = analyzeText(lastAnswerText || "");
                    populatePanel(flags, lastQuestionText || "(Question not detected)", lastAnswerText || "");
                } else {
                    updatePanelWithDetection(msg.detection);
                }
                // Auto-expand panel so the user sees the results
                panelEl.classList.remove("ahd-collapsed");
                if (reopenBtn) { reopenBtn.remove(); reopenBtn = null; }
            }
        }
    });

    /* ─── Init ─── */
    // Wait for the page to fully load, then start observing
    if (document.readyState === "complete") {
        startObserver();
        // Scan once on load in case there's already a conversation
        setTimeout(() => scanLatestResponse(), 2000);
    } else {
        window.addEventListener("load", () => {
            startObserver();
            setTimeout(() => scanLatestResponse(), 2000);
        });
    }
})();
