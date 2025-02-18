from fastapi import APIRouter

router = APIRouter()

@router.get("/mri")
async def get_mri_data():
    return {"message": "MRI data"}