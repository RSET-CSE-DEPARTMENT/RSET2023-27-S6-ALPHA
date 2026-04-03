"""
Keyword Extractor using KeyBERT (ML-based)
Input: JSON file with format {"question": "...", "answer": "..."} or list of such objects
Output: Set of keywords printed to console
"""

import json
import sys

try:
    from keybert import KeyBERT
except ImportError:
    print("KeyBERT not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keybert"])
    from keybert import KeyBERT

# Lazy-loaded model instance
_kw_model = None


def get_model():
    """Get or create the KeyBERT model (lazy loading)."""
    global _kw_model
    if _kw_model is None:
        print("Loading KeyBERT model...")
        _kw_model = KeyBERT()
    return _kw_model


def extract_keywords_from_text(text: str, top_n: int = 10) -> list:
    """
    Extract keywords from text using KeyBERT.
    
    Args:
        text: Input text to extract keywords from
        top_n: Number of top keywords to return
    
    Returns:
        List of (keyword, score) tuples
    """
    kw_model = get_model()
    
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=top_n,
        use_maxsum=True,
        nr_candidates=20
    )
    
    return keywords


def extract_keywords_from_json(json_file: str, top_n: int = 15) -> list:
    """
    Extract keywords from a JSON file using KeyBERT.
    
    Args:
        json_file: Path to JSON file
        top_n: Number of top keywords to return
    
    Returns:
        List of (keyword, score) tuples
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Handle both single object and list of objects
    if isinstance(data, dict):
        data = [data]
    
    all_text = []
    for item in data:
        if 'question' in item:
            all_text.append(item['question'])
        if 'answer' in item:
            all_text.append(item['answer'])
    
    combined_text = ' '.join(all_text)
    
    return extract_keywords_from_text(combined_text, top_n)


def main():
    """Main function to run keyword extraction."""
    if len(sys.argv) < 2:
        print("Usage: python keyword_extractor.py <json_file>")
        print("Example: python keyword_extractor.py input.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    try:
        keywords = extract_keywords_from_json(json_file)
        
        print("\n" + "=" * 50)
        print("EXTRACTED KEYWORDS (KeyBERT ML Model)")
        print("=" * 50)
        print(f"\nTotal keywords found: {len(keywords)}\n")
        
        # Print keywords with their relevance scores
        for keyword, score in keywords:
            bar = "█" * int(score * 20)
            print(f"  {score:.3f} {bar} {keyword}")
        
        print("\n" + "=" * 50)
        
        # Also print just the keywords as a set
        print("\nKeywords set:")
        keyword_set = {kw for kw, _ in keywords}
        print(keyword_set)
        
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
