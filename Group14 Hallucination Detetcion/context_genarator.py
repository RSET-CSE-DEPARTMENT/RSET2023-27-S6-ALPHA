import os
import requests
import json
from typing import Dict, List, Optional
import time
import re
from dotenv import load_dotenv 
load_dotenv()

class ContextGenerator:
    """
    A context generator that searches using SERP API and fetches content
    from Wikipedia or original sources, with answer extraction capabilities.
    """
    
    def __init__(self, serp_api_key: str):
        """
        Initialize the context generator.
        
        Args:
            serp_api_key: Your SerpAPI API key
        """
        self.serp_api_key = serp_api_key
        self.serp_base_url = "https://serpapi.com/search"
        self.wikipedia_api_url = "https://en.wikipedia.org/w/api.php"
        
        # User-Agent for Wikipedia API (required by Wikipedia)
        self.headers = {
            "User-Agent": "ContextGenerator/1.0 (Educational Project; Python/requests)"
        }
    
    def search_serp(self, keywords: str, num_results: int = 10) -> Dict:
        """
        Search using SERP API.
        
        Args:
            keywords: Search keywords
            num_results: Number of results to return
            
        Returns:
            Dictionary containing search results
        """
        params = {
            "q": keywords,
            "api_key": self.serp_api_key,
            "engine": "google",
            "num": num_results
        }
        
        try:
            response = requests.get(self.serp_base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error searching SERP API: {e}")
            return {}
    
    def extract_answer_box(self, search_results: Dict) -> Optional[str]:
        """
        Extract answer from Google's answer box/featured snippet if available.
        
        Args:
            search_results: SERP API search results
            
        Returns:
            Answer text or None
        """
        # Check for answer box
        answer_box = search_results.get("answer_box")
        if answer_box:
            # Try different answer box formats
            if "answer" in answer_box:
                return answer_box["answer"]
            if "snippet" in answer_box:
                return answer_box["snippet"]
            if "title" in answer_box:
                return answer_box["title"]
        
        # Check for featured snippet
        featured_snippet = search_results.get("featured_snippet")
        if featured_snippet:
            if "snippet" in featured_snippet:
                return featured_snippet["snippet"]
        
        # Check for knowledge graph
        knowledge_graph = search_results.get("knowledge_graph")
        if knowledge_graph:
            if "description" in knowledge_graph:
                return knowledge_graph["description"]
            if "title" in knowledge_graph:
                return knowledge_graph["title"]
        
        return None
    
    def is_wikipedia_url(self, url: str) -> bool:
        """
        Check if a URL is from Wikipedia.
        
        Args:
            url: URL to check
            
        Returns:
            True if Wikipedia URL, False otherwise
        """
        return "wikipedia.org" in url.lower()
    
    def extract_wikipedia_title(self, url: str) -> Optional[str]:
        """
        Extract Wikipedia page title from URL.
        
        Args:
            url: Wikipedia URL
            
        Returns:
            Page title or None
        """
        try:
            # Handle different Wikipedia URL formats
            if "/wiki/" in url:
                title = url.split("/wiki/")[1].split("#")[0].split("?")[0]
                # URL decode the title
                import urllib.parse
                return urllib.parse.unquote(title)
            return None
        except Exception as e:
            print(f"Error extracting Wikipedia title: {e}")
            return None
    
    def fetch_wikipedia_content(self, title: str) -> Dict:
        """
        Fetch FULL Wikipedia page content using Wikipedia API.
        
        Args:
            title: Wikipedia page title
            
        Returns:
            Dictionary containing COMPLETE page content and metadata
        """
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts|info",
            "explaintext": True,  # Get full plain text (entire article)
            "inprop": "url"
        }
        
        try:
            # Add User-Agent header (required by Wikipedia)
            response = requests.get(
                self.wikipedia_api_url, 
                params=params,
                headers=self.headers
            )
            response.raise_for_status()
            data = response.json()
            
            # Extract page content
            pages = data.get("query", {}).get("pages", {})
            if pages:
                page_id = list(pages.keys())[0]
                page_data = pages[page_id]
                
                full_content = page_data.get("extract", "")
                
                return {
                    "title": page_data.get("title", ""),
                    "content": full_content,  # FULL ARTICLE TEXT
                    "url": page_data.get("fullurl", ""),
                    "source": "Wikipedia",
                    "content_length": len(full_content),
                    "word_count": len(full_content.split()),
                    "char_count": len(full_content)
                }
            return {}
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Wikipedia content: {e}")
            return {}
    
    def fetch_webpage_content(self, url: str) -> Dict:
        """
        Fetch content from a regular webpage.
        
        Args:
            url: URL to fetch
            
        Returns:
            Dictionary containing page content
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Basic text extraction (you might want to use BeautifulSoup for better extraction)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return {
                "title": soup.title.string if soup.title else "No title",
                "content": text,  # Full webpage content
                "url": url,
                "source": "Webpage",
                "content_length": len(text),
                "word_count": len(text.split()),
                "char_count": len(text)
            }
        except Exception as e:
            print(f"Error fetching webpage content: {e}")
            return {}
    
    def get_first_organic_result(self, search_results: Dict) -> Optional[Dict]:
        """
        Extract the first organic search result.
        
        Args:
            search_results: SERP API search results
            
        Returns:
            First organic result or None
        """
        organic_results = search_results.get("organic_results", [])
        if organic_results:
            return organic_results[0]
        return None
    
    def extract_relevant_context_smart(self, content: str, keywords: str, 
                                      context_chars: int = 2000, 
                                      max_sections: int = 3) -> str:
        """
        IMPROVED: Extract multiple relevant sections based on keywords.
        This finds ALL occurrences of keywords and returns top sections.
        
        Args:
            content: Full content text
            keywords: Search keywords
            context_chars: Characters per section
            max_sections: Maximum number of sections to return
            
        Returns:
            Relevant excerpts from content
        """
        if not content:
            return ""
        
        # Split keywords and clean them
        keyword_list = [k.strip().lower() for k in keywords.split() if k.strip()]
        
        if not keyword_list:
            return content[:context_chars]
        
        content_lower = content.lower()
        
        # Find all positions where ANY keyword appears
        keyword_positions = []
        for keyword in keyword_list:
            start = 0
            while True:
                pos = content_lower.find(keyword, start)
                if pos == -1:
                    break
                keyword_positions.append({
                    'position': pos,
                    'keyword': keyword,
                    'score': len(keyword)  # Longer keywords get higher scores
                })
                start = pos + 1
        
        if not keyword_positions:
            # No keywords found, return beginning
            return content[:context_chars]
        
        # Sort by position
        keyword_positions.sort(key=lambda x: x['position'])
        
        # Cluster positions that are close together
        clusters = []
        current_cluster = [keyword_positions[0]]
        
        for kp in keyword_positions[1:]:
            # If within 500 chars of the last position in current cluster, add to it
            if kp['position'] - current_cluster[-1]['position'] < 500:
                current_cluster.append(kp)
            else:
                # Start new cluster
                clusters.append(current_cluster)
                current_cluster = [kp]
        clusters.append(current_cluster)
        
        # Score each cluster
        cluster_scores = []
        for cluster in clusters:
            # Score based on number of unique keywords and their lengths
            unique_keywords = set(kp['keyword'] for kp in cluster)
            score = len(unique_keywords) * 10 + sum(kp['score'] for kp in cluster)
            center_pos = sum(kp['position'] for kp in cluster) // len(cluster)
            cluster_scores.append({
                'score': score,
                'position': center_pos,
                'cluster': cluster
            })
        
        # Sort by score (highest first)
        cluster_scores.sort(key=lambda x: x['score'], reverse=True)
        
        # Extract top sections
        sections = []
        for i, cluster_info in enumerate(cluster_scores[:max_sections]):
            center_pos = cluster_info['position']
            
            # Extract context around this position
            start = max(0, center_pos - context_chars // 2)
            end = min(len(content), center_pos + context_chars // 2)
            
            # Try to start at sentence boundary
            if start > 0:
                # Look for sentence start within 100 chars before
                sentence_start = content.rfind('. ', max(0, start - 100), start)
                if sentence_start != -1:
                    start = sentence_start + 2
            
            # Try to end at sentence boundary
            if end < len(content):
                sentence_end = content.find('. ', end, min(len(content), end + 100))
                if sentence_end != -1:
                    end = sentence_end + 1
            
            excerpt = content[start:end].strip()
            
            # Add section marker
            section_label = f"[Section {i+1} - Keywords: {', '.join(set(kp['keyword'] for kp in cluster_info['cluster']))}]"
            sections.append(f"{section_label}\n{excerpt}")
        
        return "\n\n...\n\n".join(sections)
    
    def extract_sentences_with_keywords(self, content: str, keywords: str, 
                                       max_sentences: int = 10) -> List[str]:
        """
        NEW: Extract sentences that contain the keywords.
        Perfect for finding specific facts like "French President 1947".
        
        Args:
            content: Full content text
            keywords: Search keywords
            max_sentences: Maximum sentences to return
            
        Returns:
            List of sentences containing keywords
        """
        if not content:
            return []
        
        # Split into sentences (simple approach)
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        # Split keywords
        keyword_list = [k.strip().lower() for k in keywords.split() if k.strip()]
        
        matching_sentences = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            
            # Count how many keywords appear in this sentence
            matches = sum(1 for keyword in keyword_list if keyword in sentence_lower)
            
            if matches > 0:
                matching_sentences.append({
                    'sentence': sentence.strip(),
                    'match_count': matches,
                    'length': len(sentence)
                })
        
        # Sort by number of matches (most matches first), then by length (shorter first for conciseness)
        matching_sentences.sort(key=lambda x: (-x['match_count'], x['length']))
        
        # Return top sentences
        return [s['sentence'] for s in matching_sentences[:max_sentences]]
    
    def generate_context(self, keywords: str, include_answer_box: bool = True) -> Dict:
        """
        Generate context for given keywords by searching and fetching FULL content.
        IMPROVED: Now extracts multiple relevant sections and matching sentences.
        
        Args:
            keywords: Search keywords (can be multiple keywords combined)
            include_answer_box: Whether to try extracting direct answer from Google
            
        Returns:
            Dictionary containing generated context with FULL content + smart excerpts
        """
        print(f"Searching for: {keywords}")
        
        # Step 1: Search using SERP API
        search_results = self.search_serp(keywords)
        
        if not search_results:
            return {"error": "No search results found"}
        
        # Step 1.5: Try to extract direct answer from Google's answer box
        direct_answer = None
        if include_answer_box:
            direct_answer = self.extract_answer_box(search_results)
            if direct_answer:
                print(f"📌 Direct Answer Found: {direct_answer}")
        
        # Step 2: Get first organic result
        first_result = self.get_first_organic_result(search_results)
        
        if not first_result:
            return {"error": "No organic results found"}
        
        url = first_result.get("link", "")
        print(f"First result URL: {url}")
        
        # Step 3: Check if it's Wikipedia and fetch content accordingly
        if self.is_wikipedia_url(url):
            print("Detected Wikipedia page, fetching FULL article using Wikipedia API...")
            title = self.extract_wikipedia_title(url)
            if title:
                content = self.fetch_wikipedia_content(title)
                if content:
                    print(f"✓ Retrieved full Wikipedia article: {content.get('word_count', 0)} words, {content.get('char_count', 0)} characters")
            else:
                content = {"error": "Could not extract Wikipedia title"}
        else:
            print("Fetching full content from webpage...")
            content = self.fetch_webpage_content(url)
            if content:
                print(f"✓ Retrieved webpage content: {content.get('word_count', 0)} words, {content.get('char_count', 0)} characters")
        
        # Step 4: Extract MULTIPLE types of relevant context
        relevant_sections = ""
        matching_sentences = []
        
        if content and "content" in content:
            print("Extracting relevant sections...")
            relevant_sections = self.extract_relevant_context_smart(
                content["content"], 
                keywords,
                context_chars=2000,
                max_sections=3
            )
            
            print("Finding sentences with keywords...")
            matching_sentences = self.extract_sentences_with_keywords(
                content["content"],
                keywords,
                max_sentences=10
            )
            print(f"✓ Found {len(matching_sentences)} matching sentences")
        
        # Step 5: Return generated context
        return {
            "keywords": keywords,
            "direct_answer": direct_answer,  # Google's direct answer if available
            "matching_sentences": matching_sentences,  # NEW: Sentences containing keywords
            "relevant_sections": relevant_sections,  # IMPROVED: Multiple smart sections
            "search_result": {
                "title": first_result.get("title", ""),
                "snippet": first_result.get("snippet", ""),
                "url": url
            },
            "content": content  # Full content
        }


def main():
    """
    Example usage of the ContextGenerator
    """
    # Set your SERP API key (get from https://serpapi.com/)
    SERP_API_KEY = os.getenv("SERP_API_KEY")
    
    if not SERP_API_KEY or SERP_API_KEY == "your_api_key_here":
        print("Please set your SERP_API_KEY environment variable or in the .env file")
        return
    
    # Initialize the context generator
    generator = ContextGenerator(SERP_API_KEY)
    
    # Search query
    keywords = "first Plane Crash"
    
    print("\n" + "="*80)
    print(f"COMBINED SEARCH: {keywords}")
    print("="*80)
    
    result = generator.generate_context(keywords)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\n✅ SUCCESS - Full content retrieved!")
        
        # Show direct answer if available
        if result.get("direct_answer"):
            print(f"\n🎯 DIRECT ANSWER:")
            print(f"  {result['direct_answer']}")
        
        print(f"\nKeywords: {result['keywords']}")
        print(f"\nSearch Result:")
        print(f"  Title: {result['search_result']['title']}")
        print(f"  URL: {result['search_result']['url']}")
        print(f"  Snippet: {result['search_result']['snippet']}")
        
        content = result['content']
        print(f"\n📊 Content Statistics:")
        print(f"  Source: {content.get('source', 'Unknown')}")
        print(f"  Title: {content.get('title', 'N/A')}")
        print(f"  Total Characters: {content.get('char_count', 0):,}")
        print(f"  Total Words: {content.get('word_count', 0):,}")
        
        # NEW: Show matching sentences
        if result.get("matching_sentences"):
            print(f"\n🔍 MATCHING SENTENCES (containing your keywords):")
            print("=" * 80)
            for i, sentence in enumerate(result['matching_sentences'], 1):
                print(f"{i}. {sentence}")
                print()
            print("=" * 80)
        
        # Show relevant sections
        if result.get("relevant_sections"):
            print(f"\n📝 RELEVANT SECTIONS (focused on your keywords):")
            print("-" * 80)
            print(result['relevant_sections'])
            print("-" * 80)
        
        # Display first 1000 characters as preview
        print(f"\n📖 Full Content Preview (first 1000 chars):")
        print("-" * 80)
        print(content.get('content', 'No content')[:1000])
        print("...")
        print("-" * 80)
        
        # Save FULL content to JSON file
        output_file = "full_context_output.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\n✓ FULL context saved to: {output_file}")
        print(f"  Includes: direct_answer, matching_sentences, relevant_sections, and full article ({content.get('word_count', 0):,} words)")
        
        # Also save just the text content to a .txt file for easy reading
        text_file = "full_article_content.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(f"SEARCH QUERY: {keywords}\n")
            f.write(f"{'='*80}\n\n")
            
            if result.get("direct_answer"):
                f.write(f"DIRECT ANSWER:\n{result['direct_answer']}\n\n")
                f.write(f"{'='*80}\n\n")
            
            if result.get("matching_sentences"):
                f.write(f"MATCHING SENTENCES:\n")
                for i, sentence in enumerate(result['matching_sentences'], 1):
                    f.write(f"{i}. {sentence}\n\n")
                f.write(f"{'='*80}\n\n")
            
            f.write(f"Title: {content.get('title', 'N/A')}\n")
            f.write(f"Source: {content.get('source', 'Unknown')}\n")
            f.write(f"URL: {result['search_result']['url']}\n")
            f.write(f"Word Count: {content.get('word_count', 0):,}\n")
            f.write(f"\n{'='*80}\n\n")
            
            if result.get("relevant_sections"):
                f.write(f"RELEVANT SECTIONS:\n{result['relevant_sections']}\n\n")
                f.write(f"{'='*80}\n\n")
            
            f.write("FULL ARTICLE:\n\n")
            f.write(content.get('content', 'No content'))
        print(f"✓ Full article text also saved to: {text_file}")
    
    print("="*80)


if __name__ == "__main__":
    main()