#!/usr/bin/env python3
"""
server.py — HalluGuard hallucination detection API.

Endpoints:
    POST /detect  — Accepts JSON with context, input, answer; returns hallucination spans.
    GET  /health  — Health check.

Usage:
    python server.py                    # Run on http://localhost:5000
    python server.py --port 8080        # Run on http://localhost:8080
"""

import argparse
import sys
from pathlib import Path

from flask import Flask, jsonify, request

from halluguard.models.inference import HallucinationDetector

app = Flask(__name__)

MODEL_DIR = str(Path(__file__).parent / "model")

detector = None


def get_detector():
    """Lazy-load the detector on first request."""
    global detector
    if detector is None:
        if not Path(MODEL_DIR).exists():
            print(f"[ERROR] Model directory not found: {MODEL_DIR}", file=sys.stderr)
            print("[ERROR] Run the model download first.", file=sys.stderr)
            sys.exit(1)
        print(f"[INFO] Loading model from: {MODEL_DIR}", file=sys.stderr)
        detector = HallucinationDetector(method="transformer", model_path=MODEL_DIR)
        print("[INFO] Model loaded successfully.", file=sys.stderr)
    return detector


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/detect", methods=["POST"])
def detect():
    """
    Detect hallucinations in the given answer.

    Expected JSON body:
    {
        "context": ["passage 1", "passage 2", ...],
        "input": "the question asked",
        "answer": "the answer to check"
    }

    Returns:
    {
        "hallucination_detected": true/false,
        "overall_score": 0.99,
        "spans": [...],
        "summary": "..."
    }
    """
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "Request body must be valid JSON."}), 400

    context = payload.get("context", [])
    if isinstance(context, str):
        context = [context]
    question = payload.get("input", "")
    answer = payload.get("answer", "")

    if not answer:
        return jsonify({"error": "'answer' field is required."}), 400

    try:
        det = get_detector()
        spans = det.predict(
            context=context,
            question=question,
            answer=answer,
            output_format="spans"
        )

        hallucination_detected = len(spans) > 0
        overall_score = round(max((s["confidence"] for s in spans), default=0.0), 6)
        count = len(spans)

        summary = (
            f"{count} hallucinated span(s) detected with max confidence {overall_score:.2f}."
            if hallucination_detected else "No hallucinations detected."
        )

        return jsonify({
            "hallucination_detected": hallucination_detected,
            "overall_score": overall_score,
            "spans": spans,
            "summary": summary,
        })

    except Exception as e:
        return jsonify({"error": f"Detection failed: {e}"}), 500


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HalluGuard API Server")
    parser.add_argument("--port", type=int, default=5000, help="Port to run the server on")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    args = parser.parse_args()

    # Pre-load the model at startup
    print("[INFO] Pre-loading model...", file=sys.stderr)
    get_detector()

    print(f"\n🛡️ HalluGuard API running on http://{args.host}:{args.port}", file=sys.stderr)
    print("   POST /detect  — Detect hallucinations", file=sys.stderr)
    print("   GET  /health  — Health check\n", file=sys.stderr)

    app.run(host=args.host, port=args.port, debug=False)
