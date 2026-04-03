/* ═══════════════════════════════════════════════════════════
   AI Hallucination Detector — Popup Status Dashboard v2.0
   ═══════════════════════════════════════════════════════════ */

const statusDot = document.getElementById("statusDot");
const statusText = document.getElementById("statusText");
const statusSite = document.getElementById("statusSite");
const issueCount = document.getElementById("issueCount");
const lastScan = document.getElementById("lastScan");
const toggleCheck = document.getElementById("toggleCheck");

const SITE_LABELS = {
    chatgpt: "ChatGPT",
    claude: "Claude",
    gemini: "Gemini",
};

// Query background for state
chrome.runtime.sendMessage({ type: "AHD_GET_STATE" }, (state) => {
    if (chrome.runtime.lastError || !state) {
        statusDot.classList.add("inactive");
        statusText.textContent = "No AI chat detected";
        statusSite.textContent = "Open ChatGPT, Claude, or Gemini to begin";
        return;
    }

    if (state.site) {
        statusDot.classList.add("active");
        statusText.textContent = "Monitoring active";
        statusSite.textContent = `Connected to ${SITE_LABELS[state.site] || state.site}`;

        // Highlight the active site tag
        const tag = document.querySelector(`.site-tag[data-site="${state.site}"]`);
        if (tag) tag.classList.add("active");
    } else {
        statusDot.classList.add("inactive");
        statusText.textContent = "No AI chat detected";
        statusSite.textContent = "Open ChatGPT, Claude, or Gemini to begin";
    }

    // Issue count
    issueCount.textContent = state.issues != null ? state.issues : "—";

    // Last scan
    if (state.lastScan) {
        const d = new Date(state.lastScan);
        lastScan.textContent = d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    } else {
        lastScan.textContent = "—";
    }

    // Toggle
    toggleCheck.checked = state.enabled !== false;
});

// Toggle handler
toggleCheck.addEventListener("change", () => {
    chrome.runtime.sendMessage({ type: "AHD_TOGGLE", enabled: toggleCheck.checked });
});
