# ADPPM/services/api/app/main.
from fastapi import FastAPI
from app.router import opd, card, lab, auth

app = FastAPI()

# Include the routers for different modules
app.include_router(opd.router, prefix="/opd", tags=["OPD Room"])
app.include_router(card.router, prefix="/card", tags=["Card Room"])
app.include_router(lab.router, prefix="/lab", tags=["Lab Room"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to ADPPM API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
