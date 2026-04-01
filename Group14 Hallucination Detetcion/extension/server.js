/* ═══════════════════════════════════════════════════════════
   AI Hallucination Detector — Local Save Server
   Run:  node server.js
   Saves extracted Q&A JSON to  ./data/<timestamp>.json
   ═══════════════════════════════════════════════════════════ */

const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 7890;
const DATA_DIR = path.join(__dirname, "data");

// Ensure data folder exists
if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
}

const server = http.createServer((req, res) => {
    // CORS headers so the extension background can reach us
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");

    if (req.method === "OPTIONS") {
        res.writeHead(204);
        res.end();
        return;
    }

    if (req.method === "POST" && req.url === "/save") {
        let body = "";
        req.on("data", (chunk) => (body += chunk));
        req.on("end", () => {
            try {
                const json = JSON.parse(body);
                const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
                const site = json.site || "unknown";
                const filename = `${site}_${timestamp}.json`;
                const filepath = path.join(DATA_DIR, filename);

                // Save only { question, answer }
                const output = {
                    question: json.question || "",
                    answer: json.answer || "",
                };

                fs.writeFileSync(filepath, JSON.stringify(output, null, 2), "utf-8");
                console.log(`✓ Saved: ${filename}`);

                res.writeHead(200, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ ok: true, file: filename }));
            } catch (err) {
                console.error("✗ Error:", err.message);
                res.writeHead(400, { "Content-Type": "application/json" });
                res.end(JSON.stringify({ ok: false, error: err.message }));
            }
        });
        return;
    }

    res.writeHead(404);
    res.end("Not found");
});

server.listen(PORT, () => {
    console.log(`\n🔍 AHD Save Server running on http://localhost:${PORT}`);
    console.log(`📁 JSON files saved to: ${DATA_DIR}\n`);
});
