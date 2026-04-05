import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

AI_DATA = []
TFIDF_MATRIX = None
VECTORIZER = None

def initialize_ai():
    global AI_DATA, TFIDF_MATRIX, VECTORIZER
    AI_DATA = []
    base_path = Path("ai/data/schemes")

    if not base_path.exists():
        print("Schemes folder not found:", base_path)
        return

    for sector_folder in base_path.iterdir():
        if sector_folder.is_dir():
            for file in sector_folder.glob("*.json"):
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if "scheme_id" in data and "scheme_name" in data:
                            AI_DATA.append(data)
                except:
                    continue

    # Initialize TF-IDF
    VECTORIZER = TfidfVectorizer()
    texts = [json.dumps(scheme).lower() for scheme in AI_DATA]
    TFIDF_MATRIX = VECTORIZER.fit_transform(texts) if texts else None

    print(f"Loaded {len(AI_DATA)} schemes into AI cache.")

def get_ai_cache():
    return AI_DATA, TFIDF_MATRIX, VECTORIZER
