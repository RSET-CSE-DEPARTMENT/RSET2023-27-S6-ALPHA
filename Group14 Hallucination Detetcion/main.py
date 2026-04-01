"""
Main Pipeline: Question → Keywords → Context → Hallucination Detection

This script ties together:
1. Keyword Extractor (KeyBERT ML model)  
2. Context Generator (SERP API + Wikipedia/Web content)
3. HalluGuard Hallucination Detector (ModernBERT token classifier)

Input: JSON file with {question, answer}
Output: JSON file with {context, question, answer, hallucination results}
"""

import json
import sys
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our modules
from keyword_extractor import extract_keywords_from_text
from context_genarator import ContextGenerator

# ── HalluGuard model (lazy-loaded) ──
_detector = None

MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")


def get_detector():
    """Lazy-load the HalluGuard hallucination detector."""
    global _detector
    if _detector is None:
        from halluguard.models.inference import HallucinationDetector
        print(f"[HalluGuard] Loading model from: {MODEL_DIR}")
        _detector = HallucinationDetector(method="transformer", model_path=MODEL_DIR)
        print("[HalluGuard] Model loaded successfully.")
    return _detector


def _is_meaningful_span(text: str, confidence: float) -> bool:
    """
    Filter out noisy single-word / low-quality hallucination spans.
    
    A span is meaningful only if it:
      - has at least 2 words  OR  is >= 10 characters
      - is NOT purely stop-words / function-words / punctuation
      - has confidence >= 0.35
    """
    MIN_CONFIDENCE = 0.35
    MIN_WORDS = 2
    MIN_CHARS = 10

    # Basic thresholds
    if confidence < MIN_CONFIDENCE:
        return False

    text = text.strip()
    if not text:
        return False

    words = text.split()
    word_count = len(words)

    # Very short spans must pass stricter checks
    if word_count < MIN_WORDS and len(text) < MIN_CHARS:
        return False

    # Reject spans that consist entirely of stop / function words
    STOP_WORDS = {
        "a", "an", "the", "of", "in", "on", "at", "to", "for", "and",
        "or", "but", "is", "was", "are", "were", "be", "been", "being",
        "it", "its", "he", "she", "his", "her", "they", "them", "their",
        "this", "that", "these", "those", "with", "from", "by", "as",
        "not", "no", "so", "if", "do", "did", "has", "had", "have",
        "will", "would", "could", "should", "may", "can", "about",
        "also", "just", "than", "then", "very", "more", "most", "some",
        "such", "each", "which", "who", "whom", "what", "when", "where",
    }
    content_words = [w for w in words if w.lower().strip(".,;:!?\"'()") not in STOP_WORDS]
    if len(content_words) == 0:
        return False

    # Single content-word spans are still too noisy
    if word_count == 1:
        return False

    return True


def detect_hallucinations(context: str, question: str, answer: str) -> dict:
    """
    Run HalluGuard hallucination detection on the answer.
    
    Returns dict with hallucination_detected, overall_score, spans, summary.
    """
    try:
        detector = get_detector()
        
        # Context needs to be a list for the model
        context_list = [context] if isinstance(context, str) else context
        
        raw_spans = detector.predict(
            context=context_list,
            question=question,
            answer=answer,
            output_format="spans"
        )
        
        # ── Post-process: drop noisy single-word / low-confidence spans ──
        spans = [
            s for s in raw_spans
            if _is_meaningful_span(s.get("text", ""), s.get("confidence", 0))
        ]

        filtered = len(raw_spans) - len(spans)
        if filtered:
            print(f"[HalluGuard] Filtered out {filtered} noisy span(s) "
                  f"(single-word / low-confidence)")
        
        hallucination_detected = len(spans) > 0
        overall_score = round(max((s["confidence"] for s in spans), default=0.0), 6)
        count = len(spans)
        
        summary = (
            f"{count} hallucinated span(s) detected with max confidence {overall_score:.2f}."
            if hallucination_detected else "No hallucinations detected."
        )
        
        return {
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
        }
    except Exception as e:
        print(f"[HalluGuard] Detection error: {e}")
        return {
            "hallucination_detected": False,
            "overall_score": 0.0,
            "spans": [],
            "summary": f"Detection failed: {e}",
        }


def get_wikipedia_context(context_gen: ContextGenerator, keywords: str) -> dict:
    """
    Try to get context from Wikipedia specifically.
    """
    # Search specifically on Wikipedia
    wiki_keywords = f"{keywords} site:wikipedia.org"
    print(f"Searching Wikipedia: {wiki_keywords}")
    
    search_results = context_gen.search_serp(wiki_keywords, num_results=5)
    
    if not search_results:
        return None
    
    # Find Wikipedia result
    organic_results = search_results.get("organic_results", [])
    for result in organic_results:
        url = result.get("link", "")
        if "wikipedia.org/wiki/" in url:
            print(f"Found Wikipedia: {url}")
            title = context_gen.extract_wikipedia_title(url)
            if title:
                content = context_gen.fetch_wikipedia_content(title)
                if content and content.get("content"):
                    return {
                        "content": content,
                        "url": url,
                        "title": result.get("title", ""),
                        "source": "Wikipedia"
                    }
    
    return None


def extract_clean_wikipedia_summary(content_data: dict, max_chars: int = 5000) -> str:
    """
    Extract a clean summary from Wikipedia content.
    """
    if not content_data or not content_data.get("content"):
        return ""
    
    content = content_data["content"].get("content", "")
    
    # Split into paragraphs
    paragraphs = content.split('\n\n')
    
    clean_paragraphs = []
    char_count = 0
    
    for para in paragraphs:
        para = para.strip()
        
        # Skip empty or very short
        if len(para) < 80:
            continue
        
        # Skip section headers (usually ALL CAPS or end with ==)
        if para.isupper() or '==' in para:
            continue
        
        # Skip paragraphs that look like lists/references
        if para.startswith('*') or para.startswith('-') or para.startswith('#'):
            continue
        
        # Skip if too many numbers (likely a table or list)
        digits = sum(1 for c in para if c.isdigit())
        if digits > len(para) * 0.2:  # More than 20% digits
            continue
        
        clean_paragraphs.append(para)
        char_count += len(para)
        
        if char_count >= max_chars:
            break
    
    return '\n\n'.join(clean_paragraphs)


def extract_answer_from_text(text: str, question: str) -> str:
    """
    Extract a focused answer from the text based on the question.
    """
    if not text:
        return ""
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Score sentences based on relevance
    question_words = set(question.lower().split())
    stop_words = {'what', 'is', 'the', 'a', 'an', 'how', 'does', 'it', 'and', 'or', 'to', 'of', 'in', 'for', 'with', 'by', 'from', 'are', 'was', 'were', 'that', 'this', 'which', 'who', 'whom', 'when', 'where', 'why'}
    question_keywords = question_words - stop_words
    
    scored_sentences = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        
        # Skip very short or very long sentences
        word_count = len(sentence.split())
        if word_count < 8 or word_count > 60:
            continue
        
        # Count keyword matches
        matches = sum(1 for kw in question_keywords if kw in sentence_lower)
        
        if matches > 0:
            scored_sentences.append((sentence, matches))
    
    # Sort by matches (highest first)
    scored_sentences.sort(key=lambda x: x[1], reverse=True)
    
    # Take top sentences up to ~500 chars
    result_sentences = []
    char_count = 0
    for sentence, _ in scored_sentences[:5]:
        result_sentences.append(sentence)
        char_count += len(sentence)
        if char_count > 500:
            break
    
    return ' '.join(result_sentences)


def process_qa(question: str, answer: str, context_generator: ContextGenerator) -> dict:
    """
    Process a single question-answer pair through the full pipeline.
    Now includes HalluGuard hallucination detection.
    """
    combined_text = f"{question} {answer}"
    
    # Step 1: Extract keywords
    print("\n" + "=" * 60)
    print("STEP 1: Extracting Keywords (KeyBERT)")
    print("=" * 60)
    
    keywords_with_scores = extract_keywords_from_text(combined_text, top_n=5)
    keywords_list = [kw for kw, score in keywords_with_scores]
    keywords_str = " ".join(keywords_list)
    
    print(f"\nExtracted keywords: {keywords_list}")
    
    # Step 2: Try Wikipedia first for clean content
    print("\n" + "=" * 60)
    print("STEP 2: Searching Wikipedia (Preferred Source)")
    print("=" * 60)
    
    # Use question as main search term for better Wikipedia results
    search_term = question.replace("?", "").strip()
    wiki_result = get_wikipedia_context(context_generator, search_term)
    
    context = ""
    source_url = ""
    
    if wiki_result:
        print(f"✓ Found Wikipedia content!")
        context = extract_clean_wikipedia_summary(wiki_result)
        source_url = wiki_result.get("url", "")
    
    # Step 3: Fallback to general search if no Wikipedia
    if not context or len(context) < 100:
        print("\n" + "=" * 60)
        print("STEP 3: Fallback - General Search")
        print("=" * 60)
        
        context_result = context_generator.generate_context(keywords_str)
        
        # Try direct answer first
        if context_result.get("direct_answer"):
            context = context_result["direct_answer"]
            source_url = context_result.get("search_result", {}).get("url", "")
        
        # Otherwise use snippet
        if not context or len(context) < 50:
            context = context_result.get("search_result", {}).get("snippet", "No context found.")
            source_url = context_result.get("search_result", {}).get("url", "")
    
    print(f"\nContext length: {len(context)} characters")
    print(f"Preview: {context[:300]}...")
    
    # Step 4: HalluGuard Hallucination Detection
    print("\n" + "=" * 60)
    print("STEP 4: Hallucination Detection (HalluGuard)")
    print("=" * 60)
    
    detection = detect_hallucinations(context, question, answer)
    
    print(f"\nResult: {detection['summary']}")
    if detection["spans"]:
        for span in detection["spans"]:
            print(f"  → \"{span['text']}\" (confidence: {span['confidence']:.2%})")
    
    # Build output
    output = {
        "context": context,
        "question": question,
        "answer": answer,
        "keywords": keywords_list,
        "source": source_url,
        "detection": detection,
    }
    
    return output


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_json_file> [output_json_file]")
        print("Example: python main.py input.json output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.json"
    
    # Get API key
    serp_api_key = os.getenv("SERP_API_KEY")
    if not serp_api_key:
        print("Error: SERP_API_KEY not found in .env file")
        sys.exit(1)
    
    try:
        # Load input JSON
        print(f"\nLoading input from: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, dict):
            data = [data]
        
        # Initialize context generator
        context_gen = ContextGenerator(serp_api_key)
        
        # Process each Q&A pair
        results = []
        for i, item in enumerate(data):
            print(f"\n{'#' * 60}")
            print(f"Processing Q&A pair {i + 1}/{len(data)}")
            print(f"{'#' * 60}")
            
            question = item.get("question", "")
            answer = item.get("answer", "")
            
            if not question:
                print(f"Warning: Skipping item {i + 1} - no question found")
                continue
            
            result = process_qa(question, answer, context_gen)
            results.append(result)
        
        # Write output
        output_data = results[0] if len(results) == 1 else results
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETE")
        print("=" * 60)
        print(f"\nOutput saved to: {output_file}")
        
        # Print full output
        print("\n--- FULL OUTPUT ---")
        print(json.dumps(output_data, indent=2, ensure_ascii=False))
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
