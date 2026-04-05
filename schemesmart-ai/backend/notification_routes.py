from fastapi import APIRouter, Depends, HTTPException
from backend.database import supabase
from backend.auth_routes import get_current_user, CurrentUser

router = APIRouter()


@router.get("/notifications")
async def get_notifications(current_user: CurrentUser = Depends(get_current_user)):
    """Get all notifications for the logged-in user."""
    result = (
        supabase.table("notifications")
        .select("*")
        .eq("user_id", current_user.id)
        .order("created_at", desc=True)
        .execute()
    )
    return result.data if result.data else []


@router.get("/notifications/unread-count")
async def get_unread_count(current_user: CurrentUser = Depends(get_current_user)):
    """Get count of unread notifications for the bell badge."""
    result = (
        supabase.table("notifications")
        .select("id")
        .eq("user_id", current_user.id)
        .eq("is_read", False)
        .execute()
    )
    count = len(result.data) if result.data else 0
    return {"unread_count": count}


@router.patch("/notifications/{notification_id}/read")
async def mark_as_read(
    notification_id: int,
    current_user: CurrentUser = Depends(get_current_user),
):
    """Mark a single notification as read."""
    result = (
        supabase.table("notifications")
        .update({"is_read": True})
        .eq("id", notification_id)
        .eq("user_id", current_user.id)
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"success": True}


@router.patch("/notifications/mark-all-read")
async def mark_all_read(current_user: CurrentUser = Depends(get_current_user)):
    """Mark all notifications as read."""
    supabase.table("notifications").update({"is_read": True}).eq(
        "user_id", current_user.id
    ).execute()
    return {"success": True}