#!/usr/bin/env python3
"""
webapp.py  —  Standalone HalluGuard Web App

A self-contained web interface for hallucination detection.
Completely separate from the extension pipeline (app.py / server.py).

Run:  python webapp.py
Open:  http://127.0.0.1:8000
"""

import sys
from pathlib import Path

from flask import Flask, request, render_template, jsonify

from halluguard.models.inference import HallucinationDetector

app = Flask(__name__)

MODEL_DIR = str(Path(__file__).parent / "model")
_detector = None


def get_detector():
    """Lazy-load the HalluGuard detector."""
    global _detector
    if _detector is None:
        if not Path(MODEL_DIR).exists():
            print(f"[ERROR] Model directory not found: {MODEL_DIR}", file=sys.stderr)
            sys.exit(1)
        print(f"[INFO] Loading HalluGuard model from: {MODEL_DIR}", file=sys.stderr)
        _detector = HallucinationDetector(method="transformer", model_path=MODEL_DIR)
        print("[INFO] HalluGuard model loaded successfully.", file=sys.stderr)
    return _detector


# ───────────────────────────────────────────────────────
#  ROUTES
# ───────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/detect", methods=["POST"])
def detect():
    """
    Accept JSON { context, question, answer } and return hallucination spans.
    """
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "Request body must be valid JSON."}), 400

    context = payload.get("context", "")
    question = payload.get("question", "")
    answer = payload.get("answer", "")

    if not context or not question or not answer:
        return jsonify({"error": "All three fields (context, question, answer) are required."}), 400

    # Model expects context as a list
    context_list = [context] if isinstance(context, str) else context

    try:
        det = get_detector()
        spans = det.predict(
            context=context_list,
            question=question,
            answer=answer,
            output_format="spans",
        )

        hallucination_detected = len(spans) > 0
        overall_score = round(max((s["confidence"] for s in spans), default=0.0), 6)

        summary = (
            f"{len(spans)} hallucinated span(s) detected  ·  max confidence {overall_score:.2%}"
            if hallucination_detected
            else "No hallucinations detected — the answer is consistent with the context."
        )

        return jsonify({
            "hallucination_detected": hallucination_detected,
            "overall_score": overall_score,
            "spans": [
                {
                    "text": s["text"],
                    "start": s["start"],
                    "end": s["end"],
                    "confidence": round(s["confidence"], 4),
                }
                for s in spans
            ],
            "summary": summary,
        })

    except Exception as e:
        return jsonify({"error": f"Detection failed: {e}"}), 500


# ───────────────────────────────────────────────────────
#  ENTRYPOINT
# ───────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n🛡️  HalluGuard — Standalone Web App")
    print("[INFO] Pre-loading model …", file=sys.stderr)
    try:
        get_detector()
    except Exception as e:
        print(f"[WARN] Could not pre-load model: {e}", file=sys.stderr)

    print("🌐 Open your browser to: http://127.0.0.1:8000\n")
    app.run(host="0.0.0.0", port=8000, debug=False)
