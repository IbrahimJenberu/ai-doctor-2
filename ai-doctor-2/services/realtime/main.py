# ADPPM/services/realtime/app/main.py

from fastapi import FastAPI
from .router import notification

app = FastAPI()

# Include real-time notification routes
app.include_router(
    notification.router, prefix="/notification", tags=["Real-time Notifications"]
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
