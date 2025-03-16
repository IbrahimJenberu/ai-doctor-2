from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
import asyncio
import redis
import json
import uvicorn
import asyncpg
from app.router.notification import router as notification_router
from app.helper.websocket import WebSocketManager
from app.helper.push_notification import send_push_notification
from app.models.notification import NotificationDB
from app.schema.notification_schema import NotificationSchema

app = FastAPI(title="Realtime Notification Service")

# Redis for Pub/Sub Notifications
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

# WebSocket Manager to Handle Active Connections
ws_manager = WebSocketManager()

# Database connection (PostgreSQL with LISTEN/NOTIFY)
DATABASE_URL = "postgresql+asyncpg://auth_user:admin123@pgdb/ai_doctor_db"

async def get_db():
    return await asyncpg.connect(DATABASE_URL)

@app.on_event("startup")
async def startup():
    """Runs on service startup."""
    print("Realtime Notification Service Started")
    asyncio.create_task(listen_to_postgres_notifications())

async def listen_to_postgres_notifications():
    """Listens for notifications from PostgreSQL (LISTEN/NOTIFY mechanism)."""
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("LISTEN new_notification;")
    print("Listening for PostgreSQL notifications...")
    
    while True:
        msg = await conn.fetch("SELECT pg_notify('new_notification', 'Doctor assigned a patient');")
        if msg:
            notification = json.loads(msg)
            await ws_manager.broadcast(json.dumps(notification))

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """WebSocket endpoint for real-time communication."""
    await ws_manager.connect(user_id, websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(user_id)

app.include_router(notification_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
