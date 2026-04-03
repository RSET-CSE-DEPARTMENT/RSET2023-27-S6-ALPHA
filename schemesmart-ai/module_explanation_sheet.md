# SchemeSmart AI — Detailed Module Explanation Sheet

> **Project Root:** `c:\Projects\schemesmart-ai\`
> This document maps every module to its exact source files with code-level explanations.

---

## Module 1 — User Profile Management
**Collecting and storing user demographics (age, income, category, etc.)**

### What It Does
Provides a multi-step form that collects a citizen's personal, socio-economic, and sector-specific details and persists them in the Supabase `user_profiles` table. The profile data is later used as the input to the recommendation engine.

### Key Files & Locations

| File | Role |
|---|---|
| [src/pages/Profile.tsx](file:///c:/Projects/schemesmart-ai/src/pages/Profile.tsx) | Primary UI — multi-step form (4 steps), profile summary view, save & fetch logic |
| [backend/auth_routes.py](file:///c:/Projects/schemesmart-ai/backend/auth_routes.py) | Backend API — `POST /profile` saves profile, `GET /profile` retrieves it |
| [backend/database.py](file:///c:/Projects/schemesmart-ai/backend/database.py) | Supabase client initialisation |
| [src/context/UserProfileContext.tsx](file:///c:/Projects/schemesmart-ai/src/context) | React context that holds the active user profile in memory for use by other pages |

### How It Works

**Frontend (Profile.tsx)**
- The form has 4 steps: *Basic Info → Background → Sectors → Sector Details*
- Step 1 collects: Name, Age, Gender
- Step 2 collects: Education, Income, Category, State, Marital Status, Occupation, Disability
- Step 3 shows sector checkboxes (Agriculture, Education, Healthcare, Women & Child Welfare, Housing)
- Step 4 shows conditional sub-questions *only* if a sector with extra fields was selected (e.g., selecting "Agriculture" adds Landholding Size and Type of Farming fields)
- On submit, `handleSubmit()` calls `POST /profile` with the full payload, then calls `handleFindSchemes()` which posts to `POST /recommend` and navigates to `/schemes`

**Backend (auth_routes.py)**
- `POST /profile` → `save_profile()` — maps frontend fields to Supabase column names and does an **upsert** (insert or update depending on whether profile exists)
- `GET /profile` → `get_profile()` — fetches all 20+ profile fields from `user_profiles` table for the logged-in user

**Supabase Tables Used:** `users`, `user_profiles`

**Fields Stored:**
```
full_name, age, gender, marital_status, state, district, education,
occupation, annual_income, category, disability_status, preferred_sectors,
landholding_size, type_of_farming, single_girl_child, pregnancy_status,
chronic_illness, health_insurance, last_exam_percentage, scholarship_needed,
pucca_house_status, previous_subsidy
```

---

## Module 2 — Data Acquisition & Dataset Preparation
**Gathering government schemes and converting them into structured JSON format**

### What It Does
Provides the static dataset of government schemes as structured JSON files, organised by sector folders. The backend loads these at startup and uses them for all recommendations and lookups.

### Key Files & Locations

| File | Role |
|---|---|
| [src/data/schemes/](file:///c:/Projects/schemesmart-ai/src/data/schemes) | **Root dataset directory** — contains 5 sector sub-folders |
| `src/data/schemes/agriculture/` | JSON files for agricultural schemes (PM-KISAN, PMFBY etc.) |
| `src/data/schemes/education/` | JSON files for education/scholarship schemes |
| `src/data/schemes/health/` | JSON files for healthcare schemes (Ayushman Bharat etc.) |
| `src/data/schemes/housing_shelter/` | JSON files for housing schemes (PMAY etc.) |
| `src/data/schemes/women_child/` | JSON files for women & child welfare schemes |
| [src/data/schemes.ts](file:///c:/Projects/schemesmart-ai/src/data/schemes.ts) | TypeScript-side sector list & type definitions used in the frontend |
| [backend/seed_supabase.py](file:///c:/Projects/schemesmart-ai/backend/seed_supabase.py) | Script to seed schemes into Supabase (for admin-added schemes) |

### Scheme JSON Structure
Each `.json` file in the sector folders follows this schema:
```json
{
  "scheme_id": "pmay_gramin",
  "scheme_name": "Pradhan Mantri Awas Yojana - Gramin",
  "sector": "Housing",
  "sub_sector": "Rural Housing",
  "state": "All India",
  "description": "...",
  "benefits": ["..."],
  "eligibility": { "age_limit": "...", "income_limit": "..." },
  "required_documents": ["Aadhaar", "Bank Account"],
  "application_process": { "mode": "Online", "steps": ["..."] },
  "deadline": "Ongoing",
  "officialUrl": "https://...",
  "keywords": ["housing", "rural", "pucca"]
}
```

### How It Gets Loaded
`backend/main.py` (lines 100–157) walks all sector folders at server startup, reads every `.json` file, and builds three in-memory dictionaries:
- `all_schemes[sector]` — list of schemes per sector
- `scheme_by_id[scheme_id]` — fast lookup by ID
- `scheme_by_name[normalised_name]` — fast lookup by clean name

`ai/recommender/tfidf.py` also does its own independent load with `load_schemes()` to build TF-IDF documents.

---

## Module 3 — Eligibility Filtering Engine
**Hard-filtering schemes (matching state, age limits, gender)**

### What It Does
Provides two-level filtration: (1) a **soft pre-filter** done by the TF-IDF scoring system via sector penalties, and (2) a **hard eligibility check** inside the practice form's `FormEngine` class which validates age limits, income caps, and category requirements against the user's filled answers.

### Key Files & Locations

| File | Role |
|---|---|
| [ai/recommender/tfidf.py](file:///c:/Projects/schemesmart-ai/ai/recommender/tfidf.py) | Sector-level hard penalty: non-matching sectors get ×0.25 multiplier (lines 339–343) |
| [src/ai_agentic/agentEngine.ts](file:///c:/Projects/schemesmart-ai/src/ai_agentic/agentEngine.ts) | `FormEngine` class — validates each field against `eligibility_rules` of a scheme |
| [src/pages/PracticeForm.tsx](file:///c:/Projects/schemesmart-ai/src/pages/PracticeForm.tsx) | Displays the real-time eligibility check results (Pass/Fail/Warning banners) |
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | Server-side field validation in `POST /form/answer/{scheme_id}` (lines 286–348) |

### How It Works

**Sector-level filter (tfidf.py lines 338–343):**
```python
if user_sectors and scheme_sector_matches(sch_sector):
    raw_tfidf *= 2.0  # Boost matching sector
elif user_sectors:
    raw_tfidf *= 0.25  # Penalise non-matching sector
```
This effectively filters out irrelevant sectors before ranking.

**State filter (tfidf.py lines 436–438):**
```python
if user_state and (user_state in sch_state or "all india" in sch_state):
    bonus += 0.08
```
Schemes available nationwide ("All India") always pass the state filter.

**Hard field validation (agentEngine.ts):**
The `FormEngine` class reads `eligibility_rules` from the form schema and on each field answer checks:
- `max_age` → fails if user's entered age exceeds the scheme's max age
- `max_annual_income` → fails if annual income exceeds the scheme limit
- `min_disability_percentage` → warns if claimed disability is below required %
These show as ✅ Pass / ❌ Fail / ⚠️ Warning badges in the practice form UI.

---

## Module 4 — AI-Based Scheme Ranking Module
**Using TF-IDF and Cosine Similarity to find the best semantic match**

### What It Does
The core AI engine that ranks all loaded schemes against a user's profile by combining TF-IDF cosine similarity with a rule-based bonus/penalty scoring system.

### Key Files & Locations

| File | Role |
|---|---|
| [ai/recommender/tfidf.py](file:///c:/Projects/schemesmart-ai/ai/recommender/tfidf.py) | **Main ranking engine** — TF-IDF model, cosine similarity, bonus scoring |
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | `POST /recommend` endpoint (lines 204–213) — receives profile, calls `get_recommendations()` |

### How It Works — Step by Step

**Step 1 — Document Building (`_build_document`, lines 29–72)**
Each scheme is converted to a weighted text string with sector name repeated 2×, scheme name 3×, plus description, benefits, eligibility, and keywords — all lowercased.

**Step 2 — TF-IDF Model (lines 126–161)**
```python
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 3),    # captures 1-, 2-, 3-word phrases
    max_df=0.85,           # ignores very common terms
    sublinear_tf=True      # logarithmic TF scaling
)
tfidf_matrix = vectorizer.fit_transform(documents)
```

**Step 3 — User Query Building (lines 254–322)**
The user profile is converted into a rich search query:
- Sector keywords (with aliases: "agriculture" → "farmer crop kisan")
- Age-tier keywords (youth / working-age / senior citizen)
- Income-tier keywords (BPL / subsidy language)
- Category keywords (SC/ST/OBC/EWS-specific terms)
- Gender keywords (women/mahila terms for females)
- Sector-specific inputs at **3× weight** (pregnancy, scholarship, pucca house etc.)

**Step 4 — Cosine Similarity**
```python
user_vector = vectorizer.transform([user_text])
similarities = cosine_similarity(user_vector, tfidf_matrix)[0]
```

**Step 5 — Bonus Scoring (lines 326–454)**
For each scheme a `bonus` is added based on:
| Criteria | Max Bonus |
|---|---|
| Sector-specific match (pregnancy, scholarship etc.) | +0.20 |
| Female gender match | +0.10 |
| Age-tier match (senior/youth) | +0.10 |
| Income tier (BPL) | +0.10 |
| Category (SC/ST/OBC) | +0.10 |
| State available | +0.08 |
| Disability | +0.14 |

**Final Score Normalisation:**
```python
normalised  = (raw_tfidf + bonus) / 1.8
final_score = 0.20 + normalised * 0.60   # range: 20%–82%
```
Top 12 results are returned.

---

## Module 5 — Scheme Recommendation Interface
**The frontend UI where users browse and view their matched schemes**

### What It Does
Displays the top-12 AI-matched schemes in a card grid with match score bars, AI explanation insights, sector filters, search, and bookmarking.

### Key Files & Locations

| File | Role |
|---|---|
| [src/pages/Schemes.tsx](file:///c:/Projects/schemesmart-ai/src/pages/Schemes.tsx) | **Main recommendations page** — card grid, search, sector filter, bookmark |
| [src/pages/SchemeDetail.tsx](file:///c:/Projects/schemesmart-ai/src/pages/SchemeDetail.tsx) | Full scheme detail view — benefits, eligibility, documents, apply button |
| [src/pages/BrowseSchemes.tsx](file:///c:/Projects/schemesmart-ai/src/pages/BrowseSchemes.tsx) | Browse all schemes (not filtered by profile) |
| [src/components/schemes/SchemeCard.tsx](file:///c:/Projects/schemesmart-ai/src/components/schemes/SchemeCard.tsx) | Reusable scheme card component |
| [src/context/UserProfileContext.tsx](file:///c:/Projects/schemesmart-ai/src/context) | Provides profile + recommendations to child pages |

### How It Works

1. `Schemes.tsx` reads the user profile from `UserProfileContext`
2. Calls `POST /recommend` with all profile fields (including extended sector-specific fields)
3. For each recommendation, calls `GET /scheme/{scheme_id}` to get full scheme details
4. Renders a responsive 3-column card grid. Each card shows:
   - Sector badge
   - Scheme name & description
   - Match score % with a green progress bar
   - ✨ "AI Recommendation Insight" bullet points (from `explanation[]` returned by tfidf.py)
   - View Details button → `/scheme/{id}`
   - Bookmark toggle (persisted to `localStorage`)
5. Live search filters by name; sector dropdown filters by sector tag
6. `SchemeDetail.tsx` at `/scheme/:id` shows full details and a **"Start Practice Application"** button → `/practice/:id`

---

## Module 6 — Application Form Template Module
**A dynamic engine that reads scheme requirements and generates a real-time practice form**

### What It Does
Generates a fully interactive, multi-step practice application form for any scheme. It either uses a hand-crafted schema (for specific schemes) or auto-generates a generic form by parsing the scheme's eligibility data.

### Key Files & Locations

| File | Role |
|---|---|
| [src/pages/PracticeForm.tsx](file:///c:/Projects/schemesmart-ai/src/pages/PracticeForm.tsx) | **Main form UI** — renders schema-driven fields, validation badges, eligibility panel |
| [src/ai_agentic/agentEngine.ts](file:///c:/Projects/schemesmart-ai/src/ai_agentic/agentEngine.ts) | `FormEngine` class — validates fields, manages answers, eligibility rules |
| [src/ai_agentic/form_schemas/index.ts](file:///c:/Projects/schemesmart-ai/src/ai_agentic/form_schemas/index.ts) | Registry of hand-crafted form schemas by `scheme_id` |
| [src/ai_agentic/form_schemas/education/](file:///c:/Projects/schemesmart-ai/src/ai_agentic/form_schemas/education) | Education-sector specific form schemas |
| [src/ai_agentic/form_schemas/housing/](file:///c:/Projects/schemesmart-ai/src/ai_agentic/form_schemas/housing) | Housing-sector specific form schemas |
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | `GET /form/start/{scheme_id}` and `POST /form/answer/{scheme_id}` endpoints |
| Python path: [src/ai/agentic/form_schemas/generic_fallback.py](file:///c:/Projects/schemesmart-ai/src/ai/agentic) | Python-side generic fallback schema |

### How It Works

**Schema Loading (PracticeForm.tsx lines 704–738):**
1. Check if `SCHEMES[scheme_id]` has a dedicated schema → use it
2. If not, call `GET /scheme/{id}` from backend, then run `buildGenericSchema(rawData)` to auto-generate form fields from the scheme's eligibility object

**`buildGenericSchema()` (PracticeForm.tsx lines 52–267):**
Reads six eligibility keys (`age_limit`, `income_limit`, `category`, `disability_percentage`, `state`) and constructs matching form fields with type-appropriate inputs (`string`, `number`, `date`, `enum`, `boolean`). Always adds: Full Name, Aadhaar, DOB, Gender, Mobile, Email, Address, Bank Details.

**`FormEngine` (agentEngine.ts):**
- `answer(fieldId, val)` — stores the user's answer
- `validate(fieldId, val)` — returns `{ type: "success"|"warning"|"error", message }` 
- `getEligibilitySummary()` — returns Pass/Fail/Warning for each eligibility rule
- Field types supported: `string`, `number`, `date`, `enum`, `boolean`

**Real-time Validation:**
Every keystroke triggers `validate()` → displays coloured badges (✅ green, ⚠️ amber, ❌ red) beneath each field. The **Eligibility Assessment** sidebar panel shows live scheme eligibility pass/fail status.

---

## Module 7 — AI Voice Assisted Form Guidance
**Text-to-speech and translation integrations that read out form fields**

### What It Does
Adds a language selector (English / Hindi / Malayalam) and a speaker button on every form field. When clicked, the field's hint text is optionally translated and then read aloud using the browser's Speech Synthesis API.

### Key Files & Locations

| File | Role |
|---|---|
| [src/pages/PracticeForm.tsx](file:///c:/Projects/schemesmart-ai/src/pages/PracticeForm.tsx) | All voice logic lives here (lines 604–698) |
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | `POST /tts` endpoint (lines 184–197) — server-side gTTS fallback for Hindi/Malayalam |

### How It Works (PracticeForm.tsx)

**Language State & Voice Loading (lines 604–622):**
```typescript
const [selectedLanguage, setSelectedLanguage] = useState("en"); // "en" | "hi" | "ml"
const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
// Loads all available browser voices on mount + on voiceschanged event
```

**Voice Picker — `pickVoice()` (lines 637–643):**
Uses strict BCP-47 matching to find the right browser voice:
```typescript
voices.find(v => v.lang === `${langCode}-IN`) ||   // exact: "hi-IN"
voices.find(v => v.lang.startsWith(`${langCode}-`)) || // prefix: "ml-"
voices.find(v => v.lang === langCode)               // fallback
```

**Translation — `translateText()` (lines 649–662):**
Calls the free Google Translate API (`translate.googleapis.com`) to convert English hint text to the target language. Falls back to English on failure.

**Playback — `handlePlayInstruction()` (lines 665–698):**
```typescript
// 1. Translate text if language is not English
// 2. Pick matching browser voice
// 3. Create SpeechSynthesisUtterance with correct lang + voice
// 4. Cancel any running speech, delay 150ms (Chromium bug workaround), then speak
```
Each field has a 🔊 button that toggles playback. If the same field's speaker is clicked again, it cancels the speech.

**Server-side TTS (backend/main.py `POST /tts`):**
Uses Python's `gTTS` (Google Text-to-Speech) library as a server-rendered MP3 fallback:
```python
tts = gTTS(text=req.text, lang=req.lang, slow=False)
# Returns StreamingResponse of audio/mpeg
```

---

## Module 8 — AI Chatbot Support Module
**RAG chatbot using Groq LLM to answer specific questions about schemes**

### What It Does
A floating chat widget that answers user questions about government schemes by combining TF-IDF retrieval (RAG = Retrieval-Augmented Generation) with the Groq Llama-3 LLM.

### Key Files & Locations

| File | Role |
|---|---|
| [src/components/chatbot/Chatbot.tsx](file:///c:/Projects/schemesmart-ai/src/components/chatbot/Chatbot.tsx) | **Chat UI** — floating chatbot window, message bubbles, send logic |
| [backend/llm_chat.py](file:///c:/Projects/schemesmart-ai/backend/llm_chat.py) | **RAG backend** — TF-IDF retrieval + Groq LLM call |
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | `POST /chat` endpoint (lines 500–503) — routes to `get_llm_response()` |

### How It Works

**Frontend (Chatbot.tsx):**
- Floating bubble button (bottom-right) opens a 400×560px chat window
- On send, posts `{ message, history }` to `POST /chat`
- Renders assistant and user messages with different styled bubbles
- Shows animated typing indicator (3 bouncing dots) while loading
- The `history` field sends last N messages for context

**Backend RAG Pipeline (llm_chat.py):**
The system implements a 4-step RAG pipeline:

```
Step 1: TF-IDF Retrieval
  - User message → vectorizer.transform([query])
  - cosine_similarity against all scheme documents
  - Returns top-5 most relevant schemes (min score > 0.01)

Step 2: Context Building
  - Each relevant scheme formatted as:
    "[scheme_id] Name | Sector | State
     Desc: ...  Benefits: ...  Eligibility: ...  Documents: ...  How to Apply: ..."

Step 3: Prompt Assembly
  - System prompt = base instructions + "--- RELEVANT SCHEMES ---" context block
  - Messages = [system, last 4 history turns, user message]

Step 4: Groq API Call
  - Model: llama-3.3-70b-versatile
  - Temperature: 0.4  |  Max tokens: 500
  - Returns natural language answer grounded in retrieved schemes
```

**Base System Prompt Behaviour:**
- Answers only from provided schemes context
- Under 250 words, uses bullet points
- Mentions scheme names and IDs
- Redirects off-topic questions politely
- Responds in the user's language

---

## Module 9 — Dashboard and Reminder Settings
*(Skipped — Planned but not yet implemented)*

### Current Status
This module is **not yet implemented** in the codebase. The route `/dashboard` exists:

| File | Status |
|---|---|
| [src/pages/Dashboard.tsx](file:///c:/Projects/schemesmart-ai/src/pages/Dashboard.tsx) | Placeholder page exists but has no real functionality |

### What Was Planned
- A personal dashboard to track which schemes the user has applied for
- Application status tracking (Applied / Under Review / Approved)
- Deadline reminders for scheme application cutoff dates
- Notification bell for new matching schemes (partially implemented via the notification system)

### Partially Implemented — Notification System
A notification system for new admin-added schemes does exist:

| File | Role |
|---|---|
| [backend/notification_routes.py](file:///c:/Projects/schemesmart-ai/backend/notification_routes.py) | `GET /notifications`, `POST /notifications/mark-read` |
| [backend/notification_supabase.sql](file:///c:/Projects/schemesmart-ai/backend/notification_supabase.sql) | SQL schema for `notifications` & `scheme_notifications` tables |
| [src/components/layout/Navbar.tsx](file:///c:/Projects/schemesmart-ai/src/components/layout/Navbar.tsx) | Bell icon in navbar that shows notification count badge |
| [backend/admin_routes.py](file:///c:/Projects/schemesmart-ai/backend/admin_routes.py) | Admin panel that can add schemes and trigger notifications |

---

## Module 10 — Backend and System Integration
**FastAPI and Supabase backend that glues everything together**

### What It Does
The central FastAPI server that exposes all REST API endpoints, enforces JWT authentication, orchestrates data loading, and connects the React frontend to Supabase as the database.

### Key Files & Locations

| File | Role |
|---|---|
| [backend/main.py](file:///c:/Projects/schemesmart-ai/backend/main.py) | **Central FastAPI app** — all routes registered here (520 lines) |
| [backend/auth_routes.py](file:///c:/Projects/schemesmart-ai/backend/auth_routes.py) | Auth sub-router — `/signup`, `/login`, `/me`, `/profile` |
| [backend/admin_routes.py](file:///c:/Projects/schemesmart-ai/backend/admin_routes.py) | Admin sub-router — `POST /admin/add-scheme` |
| [backend/notification_routes.py](file:///c:/Projects/schemesmart-ai/backend/notification_routes.py) | Notification sub-router |
| [backend/database.py](file:///c:/Projects/schemesmart-ai/backend/database.py) | Supabase Python client (`supabase-py`) initialisation |
| [backend/auth_utils.py](file:///c:/Projects/schemesmart-ai/backend/auth_utils.py) | `hash_password()`, `verify_password()`, JWT `create_access_token()` / `decode_access_token()` |
| [backend/models.py](file:///c:/Projects/schemesmart-ai/backend/models.py) | SQLAlchemy models (legacy – now replaced by Supabase) |
| [backend/requirements.txt](file:///c:/Projects/schemesmart-ai/backend/requirements.txt) | Python dependencies |
| [backend/.env](file:///c:/Projects/schemesmart-ai/backend/.env) | `SUPABASE_URL`, `SUPABASE_KEY`, `GROQ_API_KEY`, `SECRET_KEY` |
| [vite.config.ts](file:///c:/Projects/schemesmart-ai/vite.config.ts) | Frontend build config — `VITE_API_URL` env variable |
| [src/App.tsx](file:///c:/Projects/schemesmart-ai/src/App.tsx) | React Router — maps all URL routes to page components |

### Complete API Route Map

| Method | Endpoint | Handler File | Purpose |
|---|---|---|---|
| `GET` | `/` | `main.py` | Health check |
| `POST` | `/signup` | `auth_routes.py` | Register new user |
| `POST` | `/login` | `auth_routes.py` | Login, returns JWT |
| `GET` | `/me` | `auth_routes.py` | Get current user info |
| `GET` | `/profile` | `auth_routes.py` | Get user's saved profile |
| `POST` | `/profile` | `auth_routes.py` | Save/update user profile |
| `POST` | `/recommend` | `main.py` | Run TF-IDF recommendation |
| `GET` | `/scheme/{id}` | `main.py` | Fetch full scheme details |
| `GET` | `/form/start/{id}` | `main.py` | Initialise practice form session |
| `POST` | `/form/answer/{id}` | `main.py` | Submit + validate a form answer |
| `POST` | `/tts` | `main.py` | Server-side text-to-speech |
| `POST` | `/chat` | `main.py` | RAG chatbot message |
| `POST` | `/admin/add-scheme` | `admin_routes.py` | Admin: add new scheme |
| `GET` | `/notifications` | `notification_routes.py` | Get user notifications |

### Authentication Flow
```
Signup → BCrypt hash password → store in Supabase users table → return JWT
Login → verify BCrypt hash → return JWT
Subsequent requests → Bearer token in Authorization header → decode JWT → get user_id
```

### Frontend-Backend Connection
- Frontend uses `VITE_API_URL` env variable (set in `.env` at project root) to point to the FastAPI server (default: `http://localhost:8000`)
- The FastAPI server runs with CORS set to `allow_origins=["*"]` to accept requests from the Vite dev server (default: `http://localhost:5173`)
- Run command: `uvicorn backend.main:app --reload` (from project root)

### Supabase Tables

| Table | Used By |
|---|---|
| `users` | Auth — stores email + hashed password |
| `user_profiles` | Profile module — all 20+ profile fields |
| `schemes` | Admin-added schemes (supplements JSON files) |
| `notifications` | Notification system for new schemes |
| `scheme_notifications` | Links notifications to specific schemes |

---

## Project Architecture Summary

```
schemesmart-ai/
├── src/                          ← React/TypeScript Frontend
│   ├── pages/
│   │   ├── Profile.tsx           ← Module 1: User Profile Form
│   │   ├── Schemes.tsx           ← Module 5: Recommendation UI
│   │   ├── SchemeDetail.tsx      ← Module 5: Scheme Detail View
│   │   ├── BrowseSchemes.tsx     ← Module 5: Browse All Schemes
│   │   ├── PracticeForm.tsx      ← Module 6 + 7: Form Engine + Voice
│   │   └── Dashboard.tsx         ← Module 9: (Placeholder)
│   ├── components/
│   │   ├── chatbot/Chatbot.tsx   ← Module 8: Chatbot UI
│   │   └── layout/Navbar.tsx     ← Module 9: Notification Bell
│   ├── ai_agentic/
│   │   ├── agentEngine.ts        ← Module 3 + 6: FormEngine Validator
│   │   └── form_schemas/         ← Module 6: Scheme Form Schemas
│   └── data/
│       └── schemes/              ← Module 2: JSON Dataset (5 sectors)
│
├── backend/                      ← FastAPI Python Backend
│   ├── main.py                   ← Module 10: Central API Server
│   ├── auth_routes.py            ← Module 1 + 10: Profile & Auth
│   ├── admin_routes.py           ← Module 9: Admin Panel
│   ├── notification_routes.py    ← Module 9: Notifications
│   ├── llm_chat.py               ← Module 8: RAG + Groq LLM
│   ├── database.py               ← Module 10: Supabase Client
│   └── auth_utils.py             ← Module 10: JWT + BCrypt
│
└── ai/
    └── recommender/
        └── tfidf.py              ← Module 3 + 4: TF-IDF Ranking Engine
```
