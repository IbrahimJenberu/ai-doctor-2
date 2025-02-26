# ADPPM/services/ai/app/main.py

from fastapi import FastAPI
from .router import xray, mri, symptoms

app = FastAPI()

# Include the routers for AI-related routes
app.include_router(xray.router, prefix="/xray", tags=["Chest X-ray Analysis"])
app.include_router(mri.router, prefix="/mri", tags=["Brain MRI Analysis"])
app.include_router(symptoms.router, prefix="/symptoms", tags=["Symptoms Analysis"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
  
