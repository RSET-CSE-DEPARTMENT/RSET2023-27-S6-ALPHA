import json
import os
import re
import io
from gtts import gTTS
from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.responses import PlainTextResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai.recommender.tfidf import vectorizer, tfidf_matrix, schemes
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any, List, Optional
from fastapi import Body, HTTPException
from src.ai.agentic.form_schemas.index import SCHEMES  # custom form schemas
from src.ai.agentic.form_schemas.generic_fallback import GENERIC_FORM_SCHEMA  # fallback
from backend.auth_routes import router as auth_router
from backend.admin_routes import router as admin_router
from backend.notification_routes import router as notification_router
from ai.recommender.tfidf import get_recommendations
from backend.llm_chat import get_llm_response


# ----------------------------
# APP
# ----------------------------


# store form sessions
form_sessions = {}
app = FastAPI(title="SchemeSmart AI")

from backend.auth_routes import router as auth_router
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(notification_router)

# ----------------------------
# CORS (important for frontend)
# ----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# INCLUDE AUTH ROUTES
# ----------------------------

# Routers already included above

# ----------------------------
# MODELS
# ----------------------------

class UserProfile(BaseModel):
    age: int
    gender: str
    education: str
    income: str
    category: str
    state: str
    sector: str
    # Optional extended fields from profile
    occupation: Optional[str] = ""
    disabilityStatus: Optional[str] = ""
    # Agriculture
    landholdingSize: Optional[str] = ""
    typeOfFarming: Optional[str] = ""
    # Women & Child
    singleGirlChild: Optional[str] = ""
    pregnancyStatus: Optional[str] = ""
    # Healthcare
    chronicIllness: Optional[str] = ""
    healthInsurance: Optional[str] = ""
    # Education
    lastExamPercentage: Optional[str] = ""
    scholarshipNeeded: Optional[str] = ""
    # Housing
    puccaHouseStatus: Optional[str] = ""
    previousSubsidy: Optional[str] = ""


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Dict]] = []


# ----------------------------
# LOAD SCHEMES DATA
# ----------------------------

_BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEME_DIR = os.path.join(_BACKEND_DIR, "..", "src", "data", "schemes")

all_schemes = {}
scheme_by_id = {}
scheme_by_name = {}

def normalize(text: str):
    return re.sub(r"[^a-z0-9]+", "", text.lower())


# Only load if directory exists
if os.path.exists(SCHEME_DIR):

    for sector in os.listdir(SCHEME_DIR):

        sector_path = os.path.join(SCHEME_DIR, sector)

        if os.path.isdir(sector_path):

            all_schemes[sector.lower()] = []

            for file in os.listdir(sector_path):

                if file.endswith(".json"):

                    path = os.path.join(sector_path, file)

                    try:

                        with open(path, "r", encoding="utf-8") as f:

                            content = f.read().strip()

                            if not content:
                                continue

                            scheme = json.loads(content)

                            if "scheme_id" not in scheme:
                                continue

                            # Use the JSON's own sector field (not folder name)
                            # Only fall back to folder name if sector is missing
                            if not scheme.get("sector"):
                                scheme["sector"] = sector

                            # Index by folder for sector browsing
                            all_schemes[sector.lower()].append(scheme)

                            scheme_by_id[scheme["scheme_id"]] = scheme

                            scheme_by_name[
                                normalize(scheme.get("scheme_name", ""))
                            ] = scheme

                    except Exception as e:
                        print(f"Could not load {path}: {e}")


# ----------------------------
# STARTUP
# ----------------------------

# Removed SQLite setup


# ----------------------------
# ROOT
# ----------------------------

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "SchemeSmart AI backend is running"


# ----------------------------
# TTS ENDPOINT (Hindi / Malayalam)
# ----------------------------

class TTSRequest(BaseModel):
    text: str
    lang: str = "en"

@app.post("/tts")
async def text_to_speech(req: TTSRequest):
    try:
        tts = gTTS(text=req.text, lang=req.lang, slow=False)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return StreamingResponse(
            mp3_fp,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "inline; filename=tts.mp3"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS error: {str(e)}")


# ----------------------------
# RECOMMENDATION ENDPOINT
# ----------------------------

@app.post("/recommend")
async def recommend(profile: UserProfile):

    print("USER PROFILE RECEIVED:", profile.dict())

    results = get_recommendations(profile.dict())

    print("RECOMMENDATION RESULTS:", results)

    return {"recommendations": results}


# ----------------------------
# GET SCHEME BY ID
# ----------------------------
from backend.database import supabase as _supabase_client
from fastapi import HTTPException

@app.get("/scheme/{scheme_id}")
async def get_scheme(scheme_id: str):

    scheme = scheme_by_id.get(scheme_id)

    # Fallback: check Supabase for admin-added schemes not in JSON files
    if not scheme:
        try:
            result = _supabase_client.table("schemes").select("*").eq("scheme_id", scheme_id).execute()
            if result.data:
                scheme = result.data[0]
        except Exception:
            pass

    if not scheme:
        raise HTTPException(
            status_code=404,
            detail=f"Scheme not found: {scheme_id}"
        )

    return {
        "scheme_id": scheme.get("scheme_id"),
        "scheme_name": scheme.get("scheme_name", ""),
        "description": scheme.get("description", ""),
        "benefits": scheme.get("benefits", []),
        "eligibility": scheme.get("eligibility", []),

        "required_documents": scheme.get(
            "required_documents",
            scheme.get("documents_required", [])
        ),

        "ministry": scheme.get("implementing_department", scheme.get("ministry", "")),
        "deadline": scheme.get("deadline", ""),
        "officialUrl": scheme.get("officialUrl", ""),

        "sector": scheme.get("sector", ""),
        "category": scheme.get("sub_sector", scheme.get("category", "")),
        "state": scheme.get("state", "All India"),

        "explanation": [
            f"This scheme belongs to {scheme.get('sector', 'general')} sector.",
            f"It is available in {scheme.get('state', 'India')}.",
            "It provides financial or social assistance benefits.",
            "Check eligibility criteria carefully before applying."
        ]
    }

# Store active form sessions
form_sessions = {}

@app.post("/form/answer/{scheme_id}")

async def answer_question(scheme_id: str, data: dict = Body(...)):
    question_id = data.get("question_id")
    answer = data.get("answer")

    if not question_id:
        raise HTTPException(status_code=400, detail="question_id missing")

    session = form_sessions.get(scheme_id)
    if not session:
        raise HTTPException(status_code=400, detail="No active form session for this scheme")

    # -----------------------------
    # FIELD VALIDATION
    # -----------------------------
    # Use custom schema if available, else fall back to generic
    scheme = SCHEMES.get(scheme_id) or _get_generic_schema(scheme_id)

    field_schema = None
    if scheme:
        for step in scheme["form_steps"]:
            for field in step["fields"]:
                if field["id"] == question_id:
                    field_schema = field
                    break

    if field_schema:

        # Required validation
        if field_schema.get("required") and (answer is None or str(answer).strip() == ""):
            return {
                "error": True,
                "message": "This field is required",
                "speak": "This field is required"
            }

        # Number validation
        if field_schema.get("type") == "number":
            try:
                float(answer)
            except:
                return {
                    "error": True,
                    "message": "Please enter a valid number",
                    "speak": "Please enter a valid number"
                }

        # Enum validation
        if field_schema.get("type") == "enum":
            options = field_schema.get("options", [])
            if str(answer).lower() not in options:
                return {
                    "error": True,
                    "message": f"Please choose from {', '.join(options)}",
                    "speak": f"Please choose from {', '.join(options)}"
                }

        # Date validation
        if field_schema.get("type") == "date":
            if not re.match(r"\d{4}-\d{2}-\d{2}", str(answer)):
                return {
                    "error": True,
                    "message": "Date must be in format YYYY-MM-DD",
                    "speak": "Please enter the date in year month day format"
                }

        # Aadhaar validation
        if field_schema["id"] == "aadhaar_number":
            if not re.fullmatch(r"\d{12}", str(answer)):
                return {
                    "error": True,
                    "message": "Aadhaar number must be 12 digits",
                    "speak": "Aadhaar number must contain 12 digits"
                }

    # -----------------------------
    # Save the answer
    # -----------------------------
    session["answers"][question_id] = answer
    session["current"] += 1

    # Check if completed
    if session["current"] >= len(session["questions"]):
        return {"completed": True, "answers": session["answers"]}

    next_question = session["questions"][session["current"]]
    return {"completed": False, "question": next_question}


# ------------------- Start Form -------------------
@app.get("/form/start/{scheme_id}")
async def start_form(scheme_id: str):
    # Use custom schema if available, else fall back to generic
    scheme = SCHEMES.get(scheme_id) or _get_generic_schema(scheme_id)
    if not scheme:
        raise HTTPException(status_code=404, detail=f"No form schema found for: {scheme_id}")

    questions = []
    for step in scheme["form_steps"]:
        for field in step["fields"]:
            questions.append({
                "id": field["id"],
                "label": field["id"].replace("_", " ").title(),
                "text": f"Please enter your {field['id'].replace('_', ' ')}",
                "type": field.get("type", "string"),
                "options": field.get("options", []),
                "required": field.get("required", False),
            })

    form_sessions[scheme_id] = {"questions": questions, "current": 0, "answers": {}}
    return {"question": questions[0]}


def _get_generic_schema(scheme_id: str):
    """Return a copy of GENERIC_FORM_SCHEMA with the correct scheme_id."""
    import copy
    schema = copy.deepcopy(GENERIC_FORM_SCHEMA)
    schema["scheme_id"] = scheme_id
    return schema

# ----------------------------
# CHATBOT FUNCTION
# ----------------------------

def get_chatbot_response(user_message: str):

    msg = user_message.lower()
    normalized_msg = normalize(msg)
    
    # ---------------------------------
    # 1️⃣ Exact scheme name match
    # ---------------------------------

    for name_norm, scheme in scheme_by_name.items():

        if name_norm in normalized_msg:

            scheme_name = scheme.get("scheme_name", "")
            description = scheme.get("description", "")
            benefits = scheme.get("benefits", {})
            eligibility = scheme.get("eligibility", {})
            documents = scheme.get("required_documents", [])
            how_to_apply = scheme.get("application_process", {})

            if "document" in msg:
                return {"scheme_name": scheme_name, "documents": documents}

            if "how to apply" in msg or "apply" in msg:
                return {"scheme_name": scheme_name, "how_to_apply": how_to_apply}

            if "benefit" in msg:
                return {"scheme_name": scheme_name, "benefits": benefits}

            if "eligibility" in msg or "eligible" in msg:
                return {"scheme_name": scheme_name, "eligibility": eligibility}

            return {
                "scheme_name": scheme_name,
                "description": description,
                "benefits": benefits,
                "eligibility": eligibility,
                "documents": documents,
                "how_to_apply": how_to_apply,
            }
    
    # ---------------------------------
    # 2️⃣ Sector search
    # ---------------------------------

    for sector, sector_schemes in all_schemes.items():

        if sector in msg:

            scheme_names = [s.get("scheme_name", "") for s in sector_schemes]

            formatted_list = "\n".join(
                [f"• {name}" for name in scheme_names]
            )

            return {
                "response": f"Schemes in {sector.title()} Sector:\n\n{formatted_list}"
            }

    # ---------------------------------
    # 3️⃣ TF-IDF Semantic Search (NEW)
    # ---------------------------------

    try:

        user_vector = vectorizer.transform([msg])

        similarities = cosine_similarity(user_vector, tfidf_matrix)[0]

        top_indices = similarities.argsort()[-3:][::-1]

        best_schemes = []

        for idx in top_indices:

            scheme = schemes[idx]

            best_schemes.append(
                f"📌 {scheme.get('scheme_name','')}\n"
                f"{scheme.get('description','')}"
            )

        if best_schemes:

            return {
                "response": "\n\n".join(best_schemes)
            }

    except Exception as e:
        print("TFIDF chatbot error:", e)
    
    # ---------------------------------
    # 4️⃣ fallback
    # ---------------------------------

    return {"response": "Sorry, no matching scheme found."}


# ----------------------------
# CHAT ENDPOINT
# ----------------------------

@app.post("/chat")
async def chat(request: ChatRequest):
    reply = get_llm_response(request.message, request.history)
    return {"response": reply}


# ----------------------------
# PROFILE ENDPOINT
# ----------------------------

@app.get("/profile")
def get_profile():
    return {"message": "Profile endpoint working"}


@app.post("/profile")
def save_profile(profile: dict):

    print("PROFILE RECEIVED:", profile)

    return {"message": "Profile saved"}