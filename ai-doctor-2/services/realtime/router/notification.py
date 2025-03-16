from fastapi import APIRouter, Depends, WebSocket
from typing import List, Dict, Any
from database.connection import db
from database.queries import NotificationQueries, PatientStatusQueries
from app.helper.websocket import manager
from app.helper.push_notification import send_push_notification

router = APIRouter()

@router.post("/notifications/")
async def create_notification(patient_id: int, user_id: int, message: Dict[str, Any], type: str, db_pool=Depends(db)):
    """Creates a new notification and sends a WebSocket event"""
    notification_queries = NotificationQueries(db_pool)
    notification = await notification_queries.create_notification(patient_id, user_id, message, type)
    
    # Send real-time WebSocket event
    await manager.send_notification(user_id, notification)
    
    # Publish to Redis for scalability
    send_push_notification(user_id, notification)
    
    return {"message": "Notification sent", "data": notification}
