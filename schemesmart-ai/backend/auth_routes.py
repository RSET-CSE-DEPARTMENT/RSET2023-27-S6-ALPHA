from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional

from backend.database import supabase
from backend.auth_utils import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class CurrentUser(BaseModel):
    id: int
    email: str
    created_at: Optional[str] = None

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = decode_access_token(token)

    result = supabase.table("users").select("*").eq("id", int(user_id)).execute()
    
    if not result.data:
        raise HTTPException(status_code=401, detail="User not found")
        
    user_data = result.data[0]
    return CurrentUser(**user_data)

# 📦 Request Schemas
class SignupRequest(BaseModel):
    email: str
    password: str

class ProfileRequest(BaseModel):
    # Core fields
    full_name: Optional[str] = None
    age: Optional[str] = None
    gender: Optional[str] = None
    education: Optional[str] = None
    income: Optional[str] = None
    category: Optional[str] = None
    state: Optional[str] = None
    marital_status: Optional[str] = None
    district: Optional[str] = None
    occupation: Optional[str] = None
    disability_status: Optional[str] = None
    sector: Optional[str] = None
    # Agriculture
    landholding_size: Optional[str] = None
    type_of_farming: Optional[str] = None
    # Women & Child
    single_girl_child: Optional[str] = None
    pregnancy_status: Optional[str] = None
    # Healthcare
    chronic_illness: Optional[str] = None
    health_insurance: Optional[str] = None
    # Education
    last_exam_percentage: Optional[str] = None
    scholarship_needed: Optional[str] = None
    # Housing
    pucca_house_status: Optional[str] = None
    previous_subsidy: Optional[str] = None


# 🔐 SIGNUP
@router.post("/signup")
async def signup(data: SignupRequest):

    # ── Server-side password strength validation ──────────────────────────────
    import re
    pw = data.password
    failures = []
    if len(pw) < 8:
        failures.append("at least 8 characters")
    if not re.search(r"[A-Z]", pw):
        failures.append("an uppercase letter (A–Z)")
    if not re.search(r"[a-z]", pw):
        failures.append("a lowercase letter (a–z)")
    if not re.search(r"[0-9]", pw):
        failures.append("a number (0–9)")
    if not re.search(r"[@#$%&*!]", pw):
        failures.append("a special character (@#$%&*!)")
    if failures:
        raise HTTPException(
            status_code=400,
            detail=f"Password must contain: {', '.join(failures)}."
        )
    # ─────────────────────────────────────────────────────────────────────────

    # Check if user already exists
    existing = supabase.table("users").select("id").eq("email", data.email).execute()

    if existing.data and len(existing.data) > 0:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    new_user_res = supabase.table("users").insert({
        "email": data.email,
        "password_hash": hash_password(data.password)
    }).execute()
    
    if not new_user_res.data:
        raise HTTPException(status_code=500, detail="Failed to create user")
        
    new_user = new_user_res.data[0]

    # 🔹 Auto create blank profile
    supabase.table("user_profiles").insert({
        "user_id": new_user["id"]
    }).execute()

    # Return token so frontend can auto-login immediately
    token = create_access_token({"sub": str(new_user["id"])})
    return {"message": "User created successfully", "access_token": token, "token_type": "bearer"}



@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    result = supabase.table("users").select("*").eq("email", username).execute()

    if not result.data or len(result.data) == 0:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    user = result.data[0]

    if not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["id"])})

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
async def read_current_user(current_user: CurrentUser = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at,
    }


@router.post("/profile")
async def save_profile(
    data: ProfileRequest,
    current_user: CurrentUser = Depends(get_current_user)
):
    # Prepare payload mapping to Supabase columns
    payload = {
        "user_id": current_user.id,
        "full_name": data.full_name,
        "age": data.age,
        "gender": data.gender,
        "education": data.education,
        "annual_income": data.income,
        "category": data.category,
        "state": data.state,
        "marital_status": data.marital_status,
        "district": data.district,
        "occupation": data.occupation,
        "disability_status": data.disability_status,
        "preferred_sectors": data.sector,
        # Agriculture
        "landholding_size": data.landholding_size,
        "type_of_farming": data.type_of_farming,
        # Women & Child
        "single_girl_child": data.single_girl_child,
        "pregnancy_status": data.pregnancy_status,
        # Healthcare
        "chronic_illness": data.chronic_illness,
        "health_insurance": data.health_insurance,
        # Education
        "last_exam_percentage": data.last_exam_percentage,
        "scholarship_needed": data.scholarship_needed,
        # Housing
        "pucca_house_status": data.pucca_house_status,
        "previous_subsidy": data.previous_subsidy,
    }
    # Remove None values so existing DB columns aren't overwritten with null
    payload = {k: v for k, v in payload.items() if v is not None}

    # Check if a profile exists in Supabase
    existing = supabase.table("user_profiles").select("id").eq("user_id", current_user.id).execute()

    if existing.data and len(existing.data) > 0:
        # Update
        supabase.table("user_profiles").update(payload).eq("user_id", current_user.id).execute()
    else:
        # Insert
        supabase.table("user_profiles").insert(payload).execute()

    return {"message": "Profile saved successfully to Supabase!"}


@router.get("/profile")
async def get_profile(
    current_user: CurrentUser = Depends(get_current_user)
):
    # Fetch from Supabase
    response = supabase.table("user_profiles").select("*").eq("user_id", current_user.id).execute()
    
    if response.data and len(response.data) > 0:
        sb_profile = response.data[0]
        return {
            "full_name":           sb_profile.get("full_name"),
            "age":                 sb_profile.get("age"),
            "date_of_birth":       sb_profile.get("date_of_birth"),
            "gender":              sb_profile.get("gender"),
            "marital_status":      sb_profile.get("marital_status"),
            "state":               sb_profile.get("state"),
            "district":            sb_profile.get("district"),
            "education":           sb_profile.get("education"),
            "occupation":          sb_profile.get("occupation"),
            "annual_income":       sb_profile.get("annual_income"),
            "category":            sb_profile.get("category"),
            "disability_status":   sb_profile.get("disability_status"),
            "preferred_sectors":   sb_profile.get("preferred_sectors"),
            # Agriculture
            "landholding_size":    sb_profile.get("landholding_size"),
            "type_of_farming":     sb_profile.get("type_of_farming"),
            # Women & Child
            "single_girl_child":   sb_profile.get("single_girl_child"),
            "pregnancy_status":    sb_profile.get("pregnancy_status"),
            # Healthcare
            "chronic_illness":     sb_profile.get("chronic_illness"),
            "health_insurance":    sb_profile.get("health_insurance"),
            # Education
            "last_exam_percentage": sb_profile.get("last_exam_percentage"),
            "scholarship_needed":  sb_profile.get("scholarship_needed"),
            # Housing
            "pucca_house_status":  sb_profile.get("pucca_house_status"),
            "previous_subsidy":    sb_profile.get("previous_subsidy"),
            # MSME
            "msme_status":         sb_profile.get("msme_status"),
            "business_turnover":   sb_profile.get("business_turnover"),
        }

    return {"message": "No profile found"}