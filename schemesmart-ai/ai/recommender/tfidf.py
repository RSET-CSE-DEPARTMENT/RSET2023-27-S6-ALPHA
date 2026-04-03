import os
import json
import re
import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

current_dir = os.path.dirname(os.path.abspath(__file__))
SCHEMES_PATH = os.path.join(os.path.dirname(os.path.dirname(current_dir)), "src", "data", "schemes")

# Add project root to path so we can import backend.database
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
try:
    from backend.database import supabase as _supabase_client
    _SUPABASE_AVAILABLE = True
except Exception:
    _supabase_client = None
    _SUPABASE_AVAILABLE = False

schemes = []
documents = []


# -------------------------
# LOAD SCHEME DATASET
# -------------------------

def _build_document(scheme: dict) -> str:
    """Convert a scheme dict into a weighted TF-IDF text document."""
    name = str(scheme.get("scheme_name", ""))
    description = str(scheme.get("description", ""))
    sector = str(scheme.get("sector", ""))
    category = str(scheme.get("category", "") or scheme.get("sub_sector", ""))

    benefits = scheme.get("benefits", [])
    if isinstance(benefits, list):
        benefits = " ".join(str(b) for b in benefits)
    elif isinstance(benefits, dict):
        benefits = " ".join(str(v) for v in benefits.values())
    else:
        benefits = str(benefits)

    eligibility = scheme.get("eligibility", [])
    if isinstance(eligibility, list):
        eligibility = " ".join(str(e) for e in eligibility)
    elif isinstance(eligibility, dict):
        eligibility = " ".join(str(v) for v in eligibility.values())
    else:
        eligibility = str(eligibility)

    docs = scheme.get("required_documents", scheme.get("documents_required", []))
    if isinstance(docs, list):
        docs = " ".join(str(d) for d in docs)
    else:
        docs = str(docs)

    keywords = scheme.get("keywords", [])
    if isinstance(keywords, list):
        keywords = " ".join(keywords)

    text = f"""
    {name} {name} {name}
    {sector} {sector}
    {category}
    {description}
    {benefits}
    {eligibility}
    {docs}
    {keywords}
    """
    return text.lower()


def load_schemes():

    global schemes, documents

    schemes = []
    documents = []

    # ---- 1. Load from JSON files (primary dataset) ----
    json_scheme_ids = set()

    for root, dirs, files in os.walk(SCHEMES_PATH):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        scheme = json.load(f)
                    if not scheme.get("scheme_id"):
                        continue
                    schemes.append(scheme)
                    documents.append(_build_document(scheme))
                    json_scheme_ids.add(scheme["scheme_id"])
                except Exception as e:
                    print(f"[TF-IDF] Could not load {path}: {e}")

    # ---- 2. Load Supabase-exclusive schemes (added via admin panel) ----
    if _SUPABASE_AVAILABLE and _supabase_client:
        try:
            result = _supabase_client.table("schemes").select("*").execute()
            supabase_schemes = result.data or []
            added = 0
            for s in supabase_schemes:
                sid = s.get("scheme_id", "")
                # Only add schemes that are NOT already loaded from JSON files
                if sid and sid not in json_scheme_ids:
                    schemes.append(s)
                    documents.append(_build_document(s))
                    added += 1
            if added:
                print(f"[TF-IDF] Loaded {added} additional scheme(s) from Supabase")
        except Exception as e:
            print(f"[TF-IDF] Could not fetch Supabase schemes: {e}")


load_schemes()


# -------------------------
# TF-IDF MODEL
# -------------------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,3),
    max_df=0.85,
    min_df=2,
    sublinear_tf=True
)

tfidf_matrix = None

def rebuild_tfidf():
    """
    Re-fit the TF-IDF vectorizer on the current schemes + documents.
    Call this after adding a new scheme so recommendations include it immediately.
    """
    global vectorizer, tfidf_matrix
    if documents:
        try:
            vectorizer = TfidfVectorizer(
                stop_words="english",
                ngram_range=(1, 3),
                max_df=0.85,
                min_df=2,
                sublinear_tf=True,
            )
            tfidf_matrix = vectorizer.fit_transform(documents)
            print(f"[TF-IDF] Rebuilt with {len(documents)} schemes")
        except ValueError as e:
            print(f"[TF-IDF] Rebuild error: {e}")
            tfidf_matrix = None
    else:
        tfidf_matrix = None


# Build TF-IDF on startup
rebuild_tfidf()


# -------------------------
# RECOMMENDER
# -------------------------

def get_recommendations(user_profile):
    """
    Score every scheme against the user profile.
    Priority order:
      1. Sector match (HIGHEST - multiplier 2x / penalty 0.25x)
      2. Sector-specific inputs (high bonuses + 3x query weight)
      3. Demographics: gender, age, category, income, disability
      4. State availability
      5. Marital status / occupation
    """

    # ── Extract all profile fields ──────────────────────────────────────────
    gender     = str(user_profile.get("gender",    "")).lower().strip()
    education  = str(user_profile.get("education", "")).lower().strip()
    raw_sector = str(user_profile.get("sector",    "")).strip()
    income     = str(user_profile.get("income",    "")).lower().strip()
    category   = str(user_profile.get("category",  "")).lower().strip()
    occupation = str(user_profile.get("occupation","")).lower().strip()
    marital    = str(user_profile.get("maritalStatus",
                     user_profile.get("marital_status", ""))).lower().strip()
    disability = str(user_profile.get("disabilityStatus",
                     user_profile.get("disability_status", ""))).lower().strip()

    try:
        age = int(user_profile.get("age", 0))
    except (ValueError, TypeError):
        age = 0

    # Sector-specific fields
    landholding    = str(user_profile.get("landholdingSize",    "")).lower().strip()
    farming_type   = str(user_profile.get("typeOfFarming",      "")).lower().strip()
    single_girl    = str(user_profile.get("singleGirlChild",    "")).lower().strip()
    pregnancy      = str(user_profile.get("pregnancyStatus",    "")).lower().strip()
    chronic_ill    = str(user_profile.get("chronicIllness",     "")).lower().strip()
    health_ins     = str(user_profile.get("healthInsurance",    "")).lower().strip()
    scholarship_ok = str(user_profile.get("scholarshipNeeded",  "")).lower().strip()
    pucca_house    = str(user_profile.get("puccaHouseStatus",   "")).lower().strip()
    prev_subsidy   = str(user_profile.get("previousSubsidy",    "")).lower().strip()

    try:
        exam_pct_str = str(user_profile.get("lastExamPercentage", "")).strip()
        exam_pct = float(exam_pct_str) if exam_pct_str else None
    except ValueError:
        exam_pct = None

    # ── Multi-sector support ────────────────────────────────────────────────
    user_sectors = [s.strip().lower() for s in raw_sector.split(",") if s.strip()]

    SECTOR_ALIASES = {
        "women & child welfare": ["women", "child", "girl", "welfare", "mahila"],
        "women and child":       ["women", "child", "girl", "welfare"],
        "healthcare":            ["health", "medical", "healthcare"],
        "health":                ["health", "medical", "healthcare"],
        "agriculture":           ["agriculture", "farmer", "crop", "farming", "kisan"],
        "housing":               ["housing", "shelter", "house", "awas"],
        "housing & shelter":     ["housing", "shelter", "house", "awas"],
        "education":             ["education", "scholarship", "student", "school", "college"],
    }

    sector_keywords_flat = list(user_sectors)
    for us in user_sectors:
        for alias, words in SECTOR_ALIASES.items():
            if alias in us or us in alias:
                sector_keywords_flat.extend(words)

    def scheme_sector_matches(scheme_sector_str):
        ss = scheme_sector_str.lower()
        for us in user_sectors:
            if us in ss or ss in us:
                return True
            for alias, words in SECTOR_ALIASES.items():
                if (alias in us or us in alias) and any(w in ss for w in words):
                    return True
        return False

    # Auto-detect sector if blank
    if not user_sectors:
        if "student" in occupation or "postgraduate" in education or "undergraduate" in education:
            user_sectors = ["education"]
        elif gender == "female":
            user_sectors = ["women & child welfare"]
        elif "farmer" in occupation:
            user_sectors = ["agriculture"]
        elif disability not in ["", "none"]:
            user_sectors = ["healthcare"]

    # ── Build TF-IDF query ───────────────────────────────────────────────────
    query_tokens = []
    query_tokens.extend([education, income, category, occupation, gender])
    query_tokens.extend(sector_keywords_flat)

    # Age-based keywords
    if 15 <= age <= 30:
        query_tokens.append("youth young student scholarship fellowship stipend")
    elif 31 <= age <= 55:
        query_tokens.append("family livelihood employment self employment scheme")
    elif age > 55:
        query_tokens.append("senior citizen pension old age health welfare")

    # Income-based keywords
    if "below" in income and "1" in income:
        query_tokens.extend(["bpl financial assistance subsidy poverty low income"] * 2)
    elif "2.5" in income:
        query_tokens.append("middle income partial subsidy scheme eligibility")
    elif any(x in income for x in ["1 ", "1-"]):
        query_tokens.append("subsidy assistance low middle income beneficiary")

    # Gender
    if gender == "female":
        query_tokens.extend(["women girl empowerment scheme female welfare mahila"] * 2)

    # Category
    if category in ["sc", "st"]:
        query_tokens.extend(["scheduled caste scheduled tribe " + category + " reservation"] * 2)
    elif category == "obc":
        query_tokens.extend(["other backward class obc reservation"] * 2)
    elif category in ["ews", "minority"]:
        query_tokens.extend([category + " scheme assistance"] * 2)

    # Disability
    if disability not in ["", "none"]:
        query_tokens.extend(["disability divyangjan disabled person assistance scheme"] * 2)

    # Sector-specific inputs (3x weight)
    if single_girl == "yes":
        kw = "single girl child scholarship welfare benefit"
        query_tokens.extend([kw] * 3)
    if pregnancy == "yes":
        kw = "maternity benefit pregnant lactating mother child nutrition"
        query_tokens.extend([kw] * 3)
    if chronic_ill == "yes":
        kw = "chronic illness medical treatment disease health assistance"
        query_tokens.extend([kw] * 3)
    if health_ins == "no":
        kw = "health insurance medical coverage uninsured scheme"
        query_tokens.extend([kw] * 2)
    if scholarship_ok == "yes":
        kw = "scholarship stipend grant financial assistance student merit"
        query_tokens.extend([kw] * 3)
    if exam_pct is not None and exam_pct >= 75:
        query_tokens.extend(["merit scholarship high marks academic excellence"] * 2)
    if pucca_house == "no":
        kw = "housing pucca house construction rural shelter homeless awas"
        query_tokens.extend([kw] * 3)
    if prev_subsidy == "no":
        query_tokens.append("first time beneficiary housing subsidy scheme")
    if farming_type or landholding:
        agr_kw = "farmer agriculture crop subsidy farming " + farming_type + " " + landholding
        query_tokens.extend([agr_kw] * 3)
    if marital in ["widowed", "widow"]:
        query_tokens.extend(["widow pension welfare widowed woman scheme"] * 2)
    if marital == "married":
        query_tokens.append("married family welfare maternity household scheme")

    user_text = " ".join(t for t in query_tokens if t.strip())
    user_vector = vectorizer.transform([user_text])
    similarities = cosine_similarity(user_vector, tfidf_matrix)[0]

    # ── Score each scheme ────────────────────────────────────────────────────
    results = []
    for i, scheme in enumerate(schemes):
        raw_tfidf   = float(similarities[i])
        scheme_text = documents[i]
        bonus       = 0.0
        explanation = []

        sch_sector = str(scheme.get("sector", "")).lower()
        sch_state  = str(scheme.get("state",  "All India")).lower()
        user_state = str(user_profile.get("state", "")).lower()

        # 1. SECTOR MATCH - highest priority
        if user_sectors and scheme_sector_matches(sch_sector):
            raw_tfidf *= 2.0
            explanation.append("Matches your selected sector")
        elif user_sectors:
            raw_tfidf *= 0.25

        # 2. SECTOR-SPECIFIC inputs - highest bonuses (0.18-0.20)
        if single_girl == "yes" and ("single girl" in scheme_text or "girl child" in scheme_text):
            bonus += 0.20
            explanation.append("Special scheme for single girl child")

        if pregnancy == "yes" and any(w in scheme_text for w in ["maternity", "pregnant", "lactating"]):
            bonus += 0.20
            explanation.append("Maternity benefit scheme")

        if chronic_ill == "yes" and any(w in scheme_text for w in ["disease", "illness", "medical", "treatment"]):
            bonus += 0.18
            explanation.append("Relevant for chronic illness")

        if health_ins == "no" and any(w in scheme_text for w in ["health", "medical", "insurance"]):
            bonus += 0.12
            explanation.append("Health coverage for uninsured")

        if scholarship_ok == "yes" and any(w in scheme_text for w in ["scholarship", "stipend", "grant", "fellowship"]):
            bonus += 0.20
            explanation.append("Scholarship scheme matches your need")

        if exam_pct is not None and exam_pct >= 75 and any(w in scheme_text for w in ["merit", "scholarship"]):
            bonus += 0.12
            explanation.append("Merit scheme (score: " + str(exam_pct) + "%)")

        if pucca_house == "no" and any(w in scheme_text for w in ["house", "housing", "shelter", "awas"]):
            bonus += 0.20
            explanation.append("Housing scheme for those without pucca house")

        if prev_subsidy == "no" and any(w in scheme_text for w in ["housing", "construction"]):
            bonus += 0.08
            explanation.append("First-time housing beneficiary eligible")

        if farming_type or landholding:
            if any(w in scheme_text for w in ["farmer", "agriculture", "crop", "kisan"]):
                bonus += 0.15
                explanation.append("Relevant for farmers")
            if farming_type and farming_type in scheme_text:
                bonus += 0.12
                explanation.append("Matches farming type (" + farming_type + ")")
            small_land = landholding in ["landless", "below 1 acre", "1-2 acres"]
            if small_land and any(w in scheme_text for w in ["subsidy", "marginal"]):
                bonus += 0.10
                explanation.append("Suited for small/marginal farmers")

        if marital in ["widowed", "widow"] and any(w in scheme_text for w in ["widow", "widowed"]):
            bonus += 0.18
            explanation.append("Special scheme for widows")

        # 3. GENDER
        if gender == "female" and any(w in scheme_text for w in ["women", "girl", "female", "mahila"]):
            bonus += 0.10
            explanation.append("Relevant for women applicants")

        # 4. AGE TIER
        if 15 <= age <= 30 and any(w in scheme_text for w in ["youth", "student", "young", "scholarship"]):
            bonus += 0.08
            explanation.append("Suitable for young/student applicants")
        elif age > 55 and any(w in scheme_text for w in ["senior", "pension", "old age", "elderly"]):
            bonus += 0.10
            explanation.append("Senior citizen scheme")

        # 5. INCOME TIER
        if "below" in income and "1" in income:
            if any(w in scheme_text for w in ["financial assistance", "low income", "bpl", "poverty"]):
                bonus += 0.10
                explanation.append("Suitable for BPL/low income applicants")
        elif "2.5" in income and any(w in scheme_text for w in ["subsidy", "assistance"]):
            bonus += 0.05
            explanation.append("Partial subsidy applicable")
        elif any(x in income for x in ["1 ", "1-"]) and any(w in scheme_text for w in ["subsidy", "assistance"]):
            bonus += 0.06
            explanation.append("Subsidy scheme for lower-middle income")

        # 6. CATEGORY
        CAT_KEYWORDS = {
            "sc":       ["scheduled caste", " sc ", "dalit"],
            "st":       ["scheduled tribe", " st ", "tribal", "adivasi"],
            "obc":      ["backward class", "obc", "other backward"],
            "ews":      ["ews", "economically weaker"],
            "minority": ["minority", "muslim", "christian", "buddhist"],
        }
        cat_kws = CAT_KEYWORDS.get(category, [])
        if cat_kws and any(kw in scheme_text for kw in cat_kws):
            bonus += 0.10
            explanation.append("Supports " + category.upper() + " category")
        elif category and category in scheme_text:
            bonus += 0.06
            explanation.append("Open to " + category.upper() + " category")

        # 7. STATE
        if user_state and (user_state in sch_state or "all india" in sch_state):
            bonus += 0.08
            explanation.append("Available in your state")

        # 8. STUDENT / OCCUPATION
        if "student" in occupation and any(w in scheme_text for w in ["student", "scholarship", "education"]):
            bonus += 0.10
            explanation.append("Suitable for students")

        # 9. DISABILITY
        if disability not in ["", "none"] and any(w in scheme_text for w in ["disability", "divyang", "handicap", "disabled"]):
            bonus += 0.14
            explanation.append("Relevant for persons with disabilities")

        # FINAL SCORE - target range 20-80%
        normalised  = (raw_tfidf + bonus) / 1.8
        final_score = 0.20 + normalised * 0.60
        final_score = min(final_score, 0.82)
        final_score = max(final_score, 0.18)

        results.append({
            "scheme_id":   scheme.get("scheme_id"),
            "score":       round(final_score, 4),
            "explanation": explanation,
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:12]


# -------------------------
# GET SCHEME BY ID
# -------------------------

def get_scheme_by_id(scheme_id):

    for scheme in schemes:

        if scheme.get("scheme_id") == scheme_id:
            return scheme

    return None
