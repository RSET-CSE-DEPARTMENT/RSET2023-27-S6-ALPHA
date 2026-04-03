from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from backend.database import supabase
import ai.recommender.tfidf as tfidf_module

router = APIRouter()


class SchemeEligibility(BaseModel):
    gender: Optional[str] = None           # "Female", "Male", "Any"
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    education: Optional[str] = None        # "Graduate", "Post Graduate", etc.
    category: Optional[str] = None         # "SC", "ST", "OBC", "General", "Any"
    state: Optional[str] = None            # "All India" or specific state
    sector: Optional[str] = None           # "education", "health", etc.
    max_income: Optional[str] = None


class AddSchemeRequest(BaseModel):
    scheme_id: str
    scheme_name: str
    sector: str
    description: str
    eligibility: Optional[Dict[str, Any]] = {}
    benefits: Optional[Dict[str, Any]] = {}
    documents_required: Optional[List[str]] = []
    application_process: Optional[Dict[str, Any]] = {}
    keywords: Optional[List[str]] = []
    state: Optional[str] = "All India"


def user_matches_scheme(profile: dict, scheme: dict) -> bool:
    """Check if a user profile matches the scheme eligibility."""
    eligibility = scheme.get("eligibility", {})

    if not eligibility:
        return True  # no restrictions = matches everyone

    # Gender check
    scheme_gender = eligibility.get("gender", "Any")
    if scheme_gender and scheme_gender.lower() not in ["any", "all", ""]:
        user_gender = profile.get("gender", "")
        if user_gender and user_gender.lower() != scheme_gender.lower():
            return False

    # State check
    scheme_state = eligibility.get("state", "All India")
    if scheme_state and scheme_state.lower() not in ["all india", "all", "", "any"]:
        user_state = profile.get("state", "")
        if user_state and user_state.lower() != scheme_state.lower():
            return False

    # Sector check
    scheme_sector = eligibility.get("sector", "")
    if scheme_sector:
        user_sector = profile.get("preferred_sectors", "")
        if user_sector and scheme_sector.lower() not in user_sector.lower():
            return False

    # Age check
    user_age_str = profile.get("age", "")
    if user_age_str:
        try:
            user_age = int(user_age_str)
            min_age = eligibility.get("min_age")
            max_age = eligibility.get("max_age")
            if min_age and user_age < min_age:
                return False
            if max_age and user_age > max_age:
                return False
        except (ValueError, TypeError):
            pass

    # Category check
    scheme_category = eligibility.get("category", "Any")
    if scheme_category and scheme_category.lower() not in ["any", "all", ""]:
        user_category = profile.get("category", "")
        if user_category and scheme_category.lower() not in user_category.lower():
            return False

    return True


@router.post("/admin/add-scheme")
async def add_scheme(scheme: AddSchemeRequest):
    """
    Admin endpoint to add a new scheme.
    1. Saves scheme to Supabase schemes table.
    2. Matches against all user profiles.
    3. Sends notifications to matched users.
    """

    # --- 1. Insert scheme into Supabase ---
    scheme_data = {
        "scheme_id": scheme.scheme_id,
        "scheme_name": scheme.scheme_name,
        "sector": scheme.sector,
        "description": scheme.description,
        "eligibility": scheme.eligibility,
        "benefits": scheme.benefits,
        "documents_required": scheme.documents_required,
        "application_process": scheme.application_process,
        "keywords": scheme.keywords,
        "state": scheme.state,
    }

    # Delete existing entry with same scheme_id (if any), then insert fresh
    # This works across all versions of supabase-py
    supabase.table("schemes").delete().eq("scheme_id", scheme.scheme_id).execute()
    result = supabase.table("schemes").insert(scheme_data).execute()

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to save scheme to Supabase")

    # --- 2. Fetch all user profiles ---
    profiles_result = supabase.table("user_profiles").select("*").execute()
    profiles = profiles_result.data or []

    # --- 3. Match profiles and insert notifications ---
    notifications_to_insert = []
    matched_count = 0

    for profile in profiles:
        user_id = profile.get("user_id")
        if not user_id:
            continue

        if user_matches_scheme(profile, scheme_data):
            matched_count += 1
            notifications_to_insert.append({
                "user_id": user_id,
                "scheme_id": scheme.scheme_id,
                "scheme_name": scheme.scheme_name,
                "message": f"New scheme matching your profile: {scheme.scheme_name}",
                "is_read": False,
            })

    if notifications_to_insert:
        supabase.table("notifications").insert(notifications_to_insert).execute()

    # --- 4. Rebuild TF-IDF so the new scheme is immediately recommendable ---
    try:
        tfidf_module.load_schemes()
        tfidf_module.rebuild_tfidf()
        print(f"[Admin] TF-IDF rebuilt after adding: {scheme.scheme_id}")
    except Exception as e:
        print(f"[Admin] TF-IDF rebuild warning: {e}")

    return {
        "success": True,
        "message": f"Scheme '{scheme.scheme_name}' added successfully!",
        "total_profiles": len(profiles),
        "notifications_sent": matched_count,
    }


@router.get("/admin/schemes")
async def list_schemes():
    """List all schemes from Supabase."""
    result = supabase.table("schemes").select("*").order("added_at", desc=True).execute()
    return result.data or []
