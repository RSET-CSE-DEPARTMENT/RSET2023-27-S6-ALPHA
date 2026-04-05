/* ═══════════════════════════════════════════════════════════
   AI Hallucination Detector — Background Service Worker
   ═══════════════════════════════════════════════════════════ */

const SAVE_SERVER = "http://localhost:7890/save";

let state = {
  site: null,
  issues: 0,
  lastScan: null,
  enabled: true,
  extractedQA: null,
};

// Listen for messages from content script
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "AHD_STATUS") {
    state.site = msg.site;
    state.issues = msg.issues;
    state.lastScan = msg.lastScan;
    state.extractedQA = msg.extractedQA || null;

    // Update badge
    const text = msg.issues > 0 ? String(msg.issues) : "";
    const color =
      msg.issues > 3 ? "#f87171" : msg.issues > 0 ? "#fbbf24" : "#34d399";
    chrome.action.setBadgeText({ text, tabId: sender.tab.id });
    chrome.action.setBadgeBackgroundColor({ color, tabId: sender.tab.id });

    // Send Q&A to server → get detection results → forward to content script
    if (msg.extractedQA) {
      const tabId = sender.tab.id;
      saveToServer(msg.extractedQA, msg.site, tabId);
    }

    sendResponse({ ok: true });
  }

  if (msg.type === "AHD_GET_STATE") {
    sendResponse(state);
  }

  if (msg.type === "AHD_TOGGLE") {
    state.enabled = msg.enabled;
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs[0]) {
        chrome.tabs.sendMessage(tabs[0].id, {
          type: "AHD_SET_ENABLED",
          enabled: state.enabled,
        });
      }
    });
    sendResponse({ ok: true, enabled: state.enabled });
  }

  return true;
});

/* ─── POST JSON to pipeline server, forward results to content script ─── */
async function saveToServer(qaData, site, tabId) {
  try {
    const resp = await fetch(SAVE_SERVER, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: qaData.question || "",
        answer: qaData.answer || "",
        site: site || "unknown",
      }),
    });
    const result = await resp.json();
    console.log("[AHD] Pipeline result:", result);

    // Forward detection results back to the content script
    if (tabId && result.detection) {
      chrome.tabs.sendMessage(tabId, {
        type: "AHD_DETECTION_RESULT",
        detection: result.detection,
        context: result.context || "",
        source: result.source || "",
      });
      console.log("[AHD] Detection results forwarded to tab", tabId);
    }
  } catch (err) {
    console.warn("[AHD] Pipeline server not running:", err.message);
    // Send error state to content script so it can show a fallback
    if (tabId) {
      chrome.tabs.sendMessage(tabId, {
        type: "AHD_DETECTION_RESULT",
        detection: {
          hallucination_detected: false,
          overall_score: 0,
          spans: [],
          summary: "Server offline — could not analyze.",
        },
        error: true,
      });
    }
  }
}
