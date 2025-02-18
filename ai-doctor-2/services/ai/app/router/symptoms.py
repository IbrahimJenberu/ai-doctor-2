from fastapi import APIRouter

router = APIRouter()

@router.get("/symptoms")
async def get_symptoms_data():
    return {"message": "Symptoms data"}
