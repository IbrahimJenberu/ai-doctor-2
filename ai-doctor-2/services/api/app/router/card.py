from fastapi import APIRouter

router = APIRouter()

@router.get("/card")
async def get_card_info():
    # Implement the logic to retrieve card room information
    return {"message": "Card Room info"}
