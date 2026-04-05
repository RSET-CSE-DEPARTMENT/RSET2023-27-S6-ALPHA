from recommender.tfidf import load_schemes, build_tfidf, hybrid_recommend

DATA_PATH = "ai/data/schemes"

# Load schemes
texts, metadata = load_schemes(DATA_PATH)

# Build TF-IDF
vectorizer, tfidf_matrix = build_tfidf(texts)

# Example user profile (simulate form input)
user_profile = {
    "age": 22,
    "gender": "female",
    "education": "graduate",
    "income": "low income",
    "category": "sc",
    "state": "Himachal Pradesh",
    "sector": "Agriculture"
}

# Get recommendations
results = hybrid_recommend(
    user_profile,
    vectorizer,
    tfidf_matrix,
    metadata
)

print("\nHybrid Recommended Schemes:\n")

if not results:
    print("No eligible schemes found.")
else:
    for r in results:
        print(f"{r['scheme_name']} ({r['state']}) - Score: {r['score']}")


# -------------------------
# MAIN PUBLIC FUNCTION (FOR BACKEND)
# -------------------------

# Load and build model only once
DATA_PATH = "ai/data/schemes"
texts, metadata = load_schemes(DATA_PATH)
vectorizer, tfidf_matrix = build_tfidf(texts)


def get_recommendations(user_profile: dict):
    """
    This is the only function backend should call.
    """

    results = hybrid_recommend(
        user_profile,
        vectorizer,
        tfidf_matrix,
        metadata
    )

    return results
