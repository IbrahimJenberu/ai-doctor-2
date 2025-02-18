from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
async def get_auth_data():
    return {"message": "Auth data"}
