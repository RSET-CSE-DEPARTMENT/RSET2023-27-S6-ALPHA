"""
RAG-powered chatbot:
1. Use TF-IDF to retrieve top-k relevant schemes for the user query
2. Send ONLY those schemes as context to Groq LLM
This keeps token usage well within limits.
"""
import os
import json
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
TOP_K = 5  # Number of schemes to inject as context per query

# ─── Load Scheme Dataset ────────────────────────────────────────────────────────

_SCHEMES_DIR = Path(__file__).parent.parent / "src" / "data" / "schemes"

def _load_all_schemes() -> list:
    schemes = []
    if not _SCHEMES_DIR.exists():
        return schemes
    for json_file in _SCHEMES_DIR.rglob("*.json"):
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
                if data.get("scheme_id"):
                    schemes.append(data)
        except Exception:
            pass
    return schemes

_ALL_SCHEMES = _load_all_schemes()


# ─── Build TF-IDF Index ─────────────────────────────────────────────────────────

def _scheme_to_text(s: dict) -> str:
    name = s.get("scheme_name", "")
    sector = s.get("sector", "")
    sub_sector = s.get("sub_sector", "")
    state = s.get("state", "")
    desc = s.get("description", "")

    benefits = s.get("benefits", [])
    if isinstance(benefits, list):
        benefits = " ".join(benefits)

    eligibility = s.get("eligibility", [])
    if isinstance(eligibility, list):
        eligibility = " ".join(eligibility)
    elif isinstance(eligibility, dict):
        eligibility = " ".join(str(v) for v in eligibility.values())

    docs = s.get("documents_required", s.get("required_documents", []))
    if isinstance(docs, list):
        docs = " ".join(docs)

    return f"{name} {name} {sector} {sub_sector} {state} {desc} {benefits} {eligibility} {docs}".lower()


_SCHEME_TEXTS = [_scheme_to_text(s) for s in _ALL_SCHEMES]

_vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
if _SCHEME_TEXTS:
    _tfidf_matrix = _vectorizer.fit_transform(_SCHEME_TEXTS)
else:
    _tfidf_matrix = None


# ─── Retrieval ──────────────────────────────────────────────────────────────────

def _retrieve_relevant_schemes(query: str, top_k: int = TOP_K) -> list:
    """Return top_k schemes most relevant to the query."""
    if _tfidf_matrix is None or not query.strip():
        return _ALL_SCHEMES[:top_k]

    try:
        q_vec = _vectorizer.transform([query.lower()])
        scores = cosine_similarity(q_vec, _tfidf_matrix)[0]
        top_indices = scores.argsort()[-top_k:][::-1]
        # Only include schemes with at least a minimal relevance score
        return [_ALL_SCHEMES[i] for i in top_indices if scores[i] > 0.01][:top_k]
    except Exception:
        return _ALL_SCHEMES[:top_k]


# ─── Context Builder ────────────────────────────────────────────────────────────

def _build_context(schemes: list) -> str:
    if not schemes:
        return "No specific schemes found for this query."
    lines = []
    for s in schemes:
        name = s.get("scheme_name", "")
        sid = s.get("scheme_id", "")
        sector = s.get("sector", "")
        state = s.get("state", "All India")
        desc = s.get("description", "")

        benefits = s.get("benefits", [])
        if isinstance(benefits, list):
            benefits_text = "; ".join(benefits)
        else:
            benefits_text = str(benefits)

        eligibility = s.get("eligibility", [])
        if isinstance(eligibility, list):
            elig_text = "; ".join(eligibility)
        elif isinstance(eligibility, dict):
            elig_text = "; ".join(f"{k}: {v}" for k, v in eligibility.items())
        else:
            elig_text = str(eligibility)

        docs = s.get("documents_required", s.get("required_documents", []))
        if isinstance(docs, list):
            docs_text = "; ".join(docs)
        else:
            docs_text = str(docs)

        process = s.get("application_process", {})
        steps = process.get("steps", []) if isinstance(process, dict) else []
        process_text = "; ".join(steps) if steps else process.get("mode", "") if isinstance(process, dict) else ""

        lines.append(
            f"[{sid}] {name} | {sector} | {state}\n"
            f"  Desc: {desc}\n"
            f"  Benefits: {benefits_text}\n"
            f"  Eligibility: {elig_text}\n"
            f"  Documents: {docs_text}\n"
            f"  How to Apply: {process_text}"
        )
    return "\n\n".join(lines)


# ─── Base system prompt (no scheme data - that's injected per request) ────────

_BASE_SYSTEM = """You are SchemeSmart AI, an expert assistant helping Indian citizens discover and understand government welfare schemes.

You will be given a small set of RELEVANT schemes retrieved from the database based on the user's query.
Answer ONLY based on the schemes provided. If the answer isn't in the provided schemes, say so and suggest the user refine their question.

Rules:
- Be concise and helpful (under 250 words)
- Use bullet points for lists
- Mention scheme names and IDs when referring to them
- For off-topic questions, politely redirect to scheme topics
- Respond in English unless the user writes in another language
"""


# ─── Chat Function ──────────────────────────────────────────────────────────────

def get_llm_response(user_message: str, history: Optional[list] = None) -> str:
    if not GROQ_API_KEY:
        return "⚠️ Groq API key not configured. Please set GROQ_API_KEY in backend/.env"

    # Step 1: Retrieve relevant schemes using TF-IDF
    relevant = _retrieve_relevant_schemes(user_message, top_k=TOP_K)
    scheme_context = _build_context(relevant)

    # Step 2: Build system prompt with injected context
    system_prompt = _BASE_SYSTEM + f"\n\n--- RELEVANT SCHEMES ---\n{scheme_context}\n--- END ---"

    # Step 3: Build messages
    messages = [{"role": "system", "content": system_prompt}]
    if history:
        messages.extend(history[-4:])  # last 4 turns for context economy
    messages.append({"role": "user", "content": user_message})

    # Step 4: Call Groq
    client = Groq(api_key=GROQ_API_KEY)
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4,
            max_tokens=500,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error communicating with AI: {str(e)}"
