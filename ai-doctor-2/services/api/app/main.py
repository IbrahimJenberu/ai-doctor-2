# ADPPM/services/api/app/main.py

from fastapi import FastAPI
from .router import opd, card, lab, auth

app = FastAPI()

# Include the routers for different modules
app.include_router(opd.router, prefix="/opd", tags=["OPD Room"])
app.include_router(card.router, prefix="/card", tags=["Card Room"])
app.include_router(lab.router, prefix="/lab", tags=["Lab Room"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
