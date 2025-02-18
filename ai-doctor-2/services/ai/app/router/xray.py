from fastapi import APIRouter
from ..models.xray_model import analyze_xray

router = APIRouter()

@router.get("/xray")
async def get_xray_data():
    return {"message": "X-ray data"}

@router.post("/analyze")
async def analyze_xray_image(image: str):
    result = analyze_xray(image)
    return {"prediction": result}
