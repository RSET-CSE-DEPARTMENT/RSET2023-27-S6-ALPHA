"""
Flask API Server — AI Hallucination Detector Pipeline
Run:  python app.py

Endpoints:
  POST /save          — receives Q&A from browser extension, runs pipeline, returns results
  POST /analyze       — manual trigger: accepts {question, answer}, returns full result
  GET  /results       — lists all processed results
  GET  /results/<id>  — single result by filename
"""

import os
import json
import sys
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# ── Import pipeline modules ──────────────────────────────────
from keyword_extractor import extract_keywords_from_text
from context_genarator import ContextGenerator
from main import process_qa, get_detector

# ── App Setup ─────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from the browser extension

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RESULTS_DIR = os.path.join(DATA_DIR, "results")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ── Shared context generator (lazy-init to avoid loading on import) ──
_context_gen = None


def get_context_generator():
    global _context_gen
    if _context_gen is None:
        serp_key = os.getenv("SERP_API_KEY")
        if not serp_key:
            raise RuntimeError("SERP_API_KEY not set in .env")
        _context_gen = ContextGenerator(serp_key)
    return _context_gen


# ── Pipeline runner ───────────────────────────────────────────
def run_pipeline(question: str, answer: str, filename_prefix: str = "manual"):
    """Run the full pipeline and save the result. Returns the result dict."""
    ctx_gen = get_context_generator()
    result = process_qa(question, answer, ctx_gen)

    # Save result
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    result_filename = f"{filename_prefix}_{timestamp}.json"
    result_path = os.path.join(RESULTS_DIR, result_filename)

    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✓ Pipeline result saved: {result_filename}")
    result["_result_file"] = result_filename
    return result


# ══════════════════════════════════════════════════════════════
#  ROUTES
# ══════════════════════════════════════════════════════════════

@app.route("/save", methods=["POST", "OPTIONS"])
def save_endpoint():
    """
    Receives Q&A from the browser extension.
    Runs the FULL pipeline (context gen + hallucination detection) synchronously
    and returns results directly to the extension.
    """
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = data.get("answer", "")
    site = data.get("site", "unknown")

    # ── Save raw Q&A immediately ──
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    raw_filename = f"{site}_{timestamp}.json"
    raw_path = os.path.join(DATA_DIR, raw_filename)

    raw_output = {"question": question, "answer": answer}
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_output, f, indent=2, ensure_ascii=False)

    print(f"✓ Raw Q&A saved: {raw_filename}")

    # ── Run full pipeline synchronously ──
    try:
        result = run_pipeline(question, answer, filename_prefix=site)
        return jsonify({
            "ok": True,
            "file": raw_filename,
            "detection": result.get("detection", {}),
            "context": result.get("context", ""),
            "source": result.get("source", ""),
        })
    except Exception as e:
        print(f"✗ Pipeline error: {e}")
        return jsonify({
            "ok": False,
            "file": raw_filename,
            "error": str(e),
            "detection": {
                "hallucination_detected": False,
                "overall_score": 0.0,
                "spans": [],
                "summary": f"Pipeline error: {e}",
            },
        })


@app.route("/analyze", methods=["POST"])
def analyze_endpoint():
    """
    Manual trigger: accepts {question, answer}, runs the full pipeline
    synchronously, and returns the result.
    """
    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = data.get("answer", "")

    if not question:
        return jsonify({"error": "Missing 'question' field"}), 400

    try:
        result = run_pipeline(question, answer, filename_prefix="manual")
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/results", methods=["GET"])
def list_results():
    """Returns all processed pipeline results as a JSON array."""
    results = []
    if os.path.isdir(RESULTS_DIR):
        for fname in sorted(os.listdir(RESULTS_DIR), reverse=True):
            if fname.endswith(".json"):
                fpath = os.path.join(RESULTS_DIR, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    entry = json.load(f)
                entry["_result_file"] = fname
                results.append(entry)
    return jsonify(results)


@app.route("/results/<result_id>", methods=["GET"])
def get_result(result_id):
    """Returns a single result by filename."""
    # Sanitize: only allow .json files inside RESULTS_DIR
    if not result_id.endswith(".json"):
        result_id += ".json"

    fpath = os.path.join(RESULTS_DIR, result_id)
    if not os.path.isfile(fpath):
        return jsonify({"error": "Result not found"}), 404

    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["_result_file"] = result_id
    return jsonify(data)


# ══════════════════════════════════════════════════════════════
#  RUN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Pre-load the HalluGuard model at startup
    print("\n🔍 AI Hallucination Detector — Flask Pipeline Server")
    print("[INFO] Pre-loading HalluGuard model...")
    try:
        get_detector()
        print("[INFO] HalluGuard model ready.")
    except Exception as e:
        print(f"[WARN] Could not pre-load model: {e}")

    print(f"📁 Raw Q&A saved to:       {DATA_DIR}")
    print(f"📁 Pipeline results in:    {RESULTS_DIR}")
    print(f"🌐 Endpoints:")
    print(f"   POST /save       — extension hook (saves + full pipeline)")
    print(f"   POST /analyze    — manual test   (synchronous pipeline)")
    print(f"   GET  /results    — list all results")
    print(f"   GET  /results/id — single result\n")

    app.run(host="0.0.0.0", port=7890, debug=False)

"""
Flask API Server — AI Hallucination Detector Pipeline
Run:  python app.py

Endpoints:
  POST /save          — receives Q&A from browser extension, runs pipeline, returns results
  POST /analyze       — manual trigger: accepts {question, answer}, returns full result
  GET  /results       — lists all processed results
  GET  /results/<id>  — single result by filename
"""

import os
import json
import sys
from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

# ── Import pipeline modules ──────────────────────────────────
from keyword_extractor import extract_keywords_from_text
from context_genarator import ContextGenerator
from main import process_qa, get_detector

# ── App Setup ─────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from the browser extension

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RESULTS_DIR = os.path.join(DATA_DIR, "results")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ── Shared context generator (lazy-init to avoid loading on import) ──
_context_gen = None


def get_context_generator():
    global _context_gen
    if _context_gen is None:
        serp_key = os.getenv("SERP_API_KEY")
        if not serp_key:
            raise RuntimeError("SERP_API_KEY not set in .env")
        _context_gen = ContextGenerator(serp_key)
    return _context_gen


# ── Pipeline runner ───────────────────────────────────────────
def run_pipeline(question: str, answer: str, filename_prefix: str = "manual"):
    """Run the full pipeline and save the result. Returns the result dict."""
    ctx_gen = get_context_generator()
    result = process_qa(question, answer, ctx_gen)

    # Save result
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    result_filename = f"{filename_prefix}_{timestamp}.json"
    result_path = os.path.join(RESULTS_DIR, result_filename)

    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✓ Pipeline result saved: {result_filename}")
    result["_result_file"] = result_filename
    return result


# ══════════════════════════════════════════════════════════════
#  ROUTES
# ══════════════════════════════════════════════════════════════

@app.route("/save", methods=["POST", "OPTIONS"])
def save_endpoint():
    """
    Receives Q&A from the browser extension.
    Runs the FULL pipeline (context gen + hallucination detection) synchronously
    and returns results directly to the extension.
    """
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = data.get("answer", "")
    site = data.get("site", "unknown")

    # ── Save raw Q&A immediately ──
    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    raw_filename = f"{site}_{timestamp}.json"
    raw_path = os.path.join(DATA_DIR, raw_filename)

    raw_output = {"question": question, "answer": answer}
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_output, f, indent=2, ensure_ascii=False)

    print(f"✓ Raw Q&A saved: {raw_filename}")

    # ── Run full pipeline synchronously ──
    try:
        result = run_pipeline(question, answer, filename_prefix=site)
        return jsonify({
            "ok": True,
            "file": raw_filename,
            "detection": result.get("detection", {}),
            "context": result.get("context", ""),
            "source": result.get("source", ""),
        })
    except Exception as e:
        print(f"✗ Pipeline error: {e}")
        return jsonify({
            "ok": False,
            "file": raw_filename,
            "error": str(e),
            "detection": {
                "hallucination_detected": False,
                "overall_score": 0.0,
                "spans": [],
                "summary": f"Pipeline error: {e}",
            },
        })


@app.route("/analyze", methods=["POST"])
def analyze_endpoint():
    """
    Manual trigger: accepts {question, answer}, runs the full pipeline
    synchronously, and returns the result.
    """
    data = request.get_json(force=True)
    question = data.get("question", "")
    answer = data.get("answer", "")

    if not question:
        return jsonify({"error": "Missing 'question' field"}), 400

    try:
        result = run_pipeline(question, answer, filename_prefix="manual")
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/results", methods=["GET"])
def list_results():
    """Returns all processed pipeline results as a JSON array."""
    results = []
    if os.path.isdir(RESULTS_DIR):
        for fname in sorted(os.listdir(RESULTS_DIR), reverse=True):
            if fname.endswith(".json"):
                fpath = os.path.join(RESULTS_DIR, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    entry = json.load(f)
                entry["_result_file"] = fname
                results.append(entry)
    return jsonify(results)


@app.route("/results/<result_id>", methods=["GET"])
def get_result(result_id):
    """Returns a single result by filename."""
    # Sanitize: only allow .json files inside RESULTS_DIR
    if not result_id.endswith(".json"):
        result_id += ".json"

    fpath = os.path.join(RESULTS_DIR, result_id)
    if not os.path.isfile(fpath):
        return jsonify({"error": "Result not found"}), 404

    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["_result_file"] = result_id
    return jsonify(data)


# ══════════════════════════════════════════════════════════════
#  RUN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Pre-load the HalluGuard model at startup
    print("\n🔍 AI Hallucination Detector — Flask Pipeline Server")
    print("[INFO] Pre-loading HalluGuard model...")
    try:
        get_detector()
        print("[INFO] HalluGuard model ready.")
    except Exception as e:
        print(f"[WARN] Could not pre-load model: {e}")

    print(f"📁 Raw Q&A saved to:       {DATA_DIR}")
    print(f"📁 Pipeline results in:    {RESULTS_DIR}")
    print(f"🌐 Endpoints:")
    print(f"   POST /save       — extension hook (saves + full pipeline)")
    print(f"   POST /analyze    — manual test   (synchronous pipeline)")
    print(f"   GET  /results    — list all results")
    print(f"   GET  /results/id — single result\n")

    app.run(host="0.0.0.0", port=7890, debug=False)
    