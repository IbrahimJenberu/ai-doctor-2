from fastapi import APIRouter

router = APIRouter()

@router.get("/lab")
async def get_lab_data():
    return {"message": "Lab data"}
