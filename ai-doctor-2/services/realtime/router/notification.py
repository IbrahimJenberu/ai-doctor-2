# realtime/app/router/notification.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.helper.websocket import manager
from app.schema.notification_schema import NotificationCreate, NotificationResponse
from datetime import datetime

router = APIRouter()

notifications = []  # In-memory storage for simplicity

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"User {user_id}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@router.post("/notifications/", response_model=NotificationResponse)
async def create_notification(notification: NotificationCreate):
    new_notification = {
        "id": len(notifications) + 1,
        "recipient_id": notification.recipient_id,
        "message": notification.message,
        "timestamp": datetime.utcnow(),
        "is_read": False
    }
    notifications.append(new_notification)
    await manager.broadcast(notification.message)
    return new_notification
