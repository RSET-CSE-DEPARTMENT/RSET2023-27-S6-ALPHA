# 🛡️ HalluGuard — Real-Time AI Hallucination Detector

A real-time hallucination detection system that monitors AI chatbot responses (ChatGPT, Claude, Gemini) and identifies factually unsupported claims using a fine-tuned **ModernBERT** token-classification model, web-sourced context retrieval, and a Chrome browser extension for inline highlighting.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Browser Extension](#browser-extension)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## Overview

Large Language Models can produce confident-sounding but factually incorrect statements — *hallucinations*. HalluGuard tackles this by:

1. **Intercepting** Q&A pairs from AI chatbot interfaces via a Chrome extension.
2. **Extracting keywords** from the conversation using **KeyBERT**.
3. **Retrieving real-world context** from Wikipedia and the web via the **SerpAPI**.
4. **Detecting hallucinated spans** in the AI's answer using a fine-tuned **ModernBERT** token classifier.
5. **Highlighting** problematic spans directly inside the chatbot UI with confidence scores.

---

## Architecture

```
┌─────────────────────┐
│  Chrome Extension    │  content.js intercepts Q&A from
│  (Manifest V3)      │  ChatGPT / Claude / Gemini
└────────┬────────────┘
         │ POST /save
         ▼
┌─────────────────────┐
│  Flask API Server   │  app.py  (port 7890)
│  ┌───────────────┐  │
│  │ Keyword        │  │  KeyBERT extracts key phrases
│  │ Extractor      │  │
│  └───────┬───────┘  │
│          ▼          │
│  ┌───────────────┐  │
│  │ Context        │  │  SerpAPI → Wikipedia / Web
│  │ Generator      │  │
│  └───────┬───────┘  │
│          ▼          │
│  ┌───────────────┐  │
│  │ HalluGuard     │  │  ModernBERT token classifier
│  │ Detector       │  │  identifies hallucinated spans
│  └───────────────┘  │
└─────────────────────┘
         │
         ▼
   JSON response with
   hallucination spans
   + confidence scores
```

---

## Project Structure

```
halu/
├── app.py                  # Main Flask API server (extension pipeline, port 7890)
├── main.py                 # End-to-end pipeline: keywords → context → detection
├── keyword_extractor.py    # KeyBERT-based keyword extraction
├── context_genarator.py    # SerpAPI search + Wikipedia/web content retrieval
├── server.py               # Standalone HalluGuard detection API (port 5000)
├── webapp.py               # Standalone web UI for manual detection (port 8000)
├── halluguard/             # HalluGuard Python package
│   ├── __init__.py
│   ├── models/             # Model inference logic
│   ├── detectors/          # Detection utilities
│   ├── datasets/           # Dataset helpers
│   └── prompts/            # Prompt templates
├── model/                  # Fine-tuned ModernBERT model weights
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
├── extension/              # Chrome extension (Manifest V3)
│   ├── manifest.json
│   ├── background.js
│   ├── content.js          # Intercepts chatbot Q&A, highlights results
│   ├── content.css         # Hallucination highlight styles
│   ├── popup.html          # Extension popup UI
│   ├── popup.js
│   ├── popup.css
│   └── server.js           # (optional) local proxy helper
├── templates/
│   └── index.html          # Web UI template for webapp.py
├── data/                   # Runtime directory for saved Q&A and results
│   └── results/
├── pyproject.toml          # Package metadata & dependencies
├── requirements.txt        # Pip requirements
└── .env                    # Environment variables (SERP_API_KEY)
```

---

## Prerequisites

- **Python** ≥ 3.10
- **pip** (or an equivalent package manager)
- A **SerpAPI** key — get one at [serpapi.com](https://serpapi.com/)
- **Google Chrome** (for the browser extension)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Alen-Saji-05/Real-time-halu-detect.git
cd Real-time-halu-detect
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install the full package (includes `halluguard` as an editable package):

```bash
pip install -e .
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SERP_API_KEY=your_serpapi_key_here
```

### 5. Download / place model weights

Ensure the `model/` directory contains the fine-tuned ModernBERT weights:

```
model/
├── config.json
├── model.safetensors
├── tokenizer.json
└── tokenizer_config.json
```

---

## Usage

### Run the full pipeline server (used by the extension)

```bash
python app.py
```

The server starts on **`http://localhost:7890`** and exposes endpoints for the Chrome extension.

### Run the standalone web UI

```bash
python webapp.py
```

Opens a browser-based interface at **`http://127.0.0.1:8000`** where you can manually enter context, a question, and an answer to check for hallucinations.

### Run the standalone detection API

```bash
python server.py               # default port 5000
python server.py --port 8080   # custom port
```

### Run the CLI pipeline

```bash
python main.py input.json output.json
```

**Input JSON format:**

```json
{
  "question": "Who was the first president of the United States?",
  "answer": "The first president of the United States was Abraham Lincoln."
}
```

---

## API Reference

### `POST /save` — Extension Hook *(app.py, port 7890)*

Receives Q&A from the browser extension, runs the full pipeline, and returns results.

**Request body:**

```json
{
  "question": "...",
  "answer": "...",
  "site": "chatgpt"
}
```

**Response:**

```json
{
  "ok": true,
  "file": "chatgpt_2026-04-01T19-30-00.json",
  "detection": {
    "hallucination_detected": true,
    "overall_score": 0.92,
    "spans": [
      { "text": "Abraham Lincoln", "start": 49, "end": 64, "confidence": 0.92 }
    ],
    "summary": "1 hallucinated span(s) detected with max confidence 0.92."
  },
  "context": "...",
  "source": "https://en.wikipedia.org/wiki/..."
}
```

### `POST /analyze` — Manual Trigger *(app.py, port 7890)*

```json
{ "question": "...", "answer": "..." }
```

Returns the full pipeline result including context, keywords, detection results, and source URL.

### `GET /results` — List All Results *(app.py, port 7890)*

Returns a JSON array of all processed pipeline results, sorted newest first.

### `GET /results/<id>` — Single Result *(app.py, port 7890)*

Returns a single result by filename.

### `POST /detect` — Direct Detection *(server.py, port 5000)*

```json
{
  "context": ["passage 1", "passage 2"],
  "input": "the question",
  "answer": "the answer to check"
}
```

### `GET /health` — Health Check *(server.py, port 5000)*

Returns `{ "status": "ok" }`.

### `POST /api/detect` — Web App Detection *(webapp.py, port 8000)*

```json
{
  "context": "...",
  "question": "...",
  "answer": "..."
}
```

---

## Browser Extension

The Chrome extension automatically monitors AI chatbot conversations and highlights hallucinated text inline.

### Supported Platforms

| Platform | URL |
|----------|-----|
| ChatGPT  | `chatgpt.com`, `chat.openai.com` |
| Claude   | `claude.ai` |
| Gemini   | `gemini.google.com` |

### Installation

1. Make sure the Flask API server is running (`python app.py`).
2. Open Chrome and navigate to `chrome://extensions/`.
3. Enable **Developer mode** (top-right toggle).
4. Click **Load unpacked** and select the `extension/` directory.
5. The extension icon will appear in the toolbar. Navigate to any supported AI chatbot and start a conversation — hallucinations will be highlighted automatically.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Hallucination Detection | Fine-tuned **ModernBERT** (token classification) |
| Keyword Extraction | **KeyBERT** |
| Context Retrieval | **SerpAPI** + **Wikipedia API** |
| Backend | **Flask**, **Flask-CORS** |
| Web Scraping | **BeautifulSoup4**, **lxml** |
| ML Framework | **PyTorch**, **Transformers** (Hugging Face) |
| Browser Extension | **Chrome Manifest V3** (vanilla JS) |
| Environment | **python-dotenv** |

---

## License

This project is licensed under the **MIT License** — see [pyproject.toml](pyproject.toml) for details.
