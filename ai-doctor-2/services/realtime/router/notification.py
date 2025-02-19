from fastapi import APIRouter

router = APIRouter()
@router.get("/notifications")
async def get_notifications():
    return {"message": "Notifications data"}

#
