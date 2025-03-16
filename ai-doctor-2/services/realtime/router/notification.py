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

@router.get("/notifications/{user_id}/", response_model=List[Dict[str, Any]])
async def get_notifications(user_id: int, db_pool=Depends(db)):
    """Fetches notifications for a user"""
    notification_queries = NotificationQueries(db_pool)
    notifications = await notification_queries.get_notifications(user_id)
    return notifications

@router.put("/notifications/{notification_id}/read")
async def mark_notification_as_read(notification_id: int, db_pool=Depends(db)):
    """Marks a notification as read"""
    notification_queries = NotificationQueries(db_pool)
    updated_notification = await notification_queries.mark_as_read(notification_id)
    return {"message": "Notification marked as read", "data": updated_notification}

@router.post("/patient-status/")
async def update_patient_status(patient_id: int, status: str, updated_by: int, db_pool=Depends(db)):
    """Updates the patient status and triggers a notification"""
    status_queries = PatientStatusQueries(db_pool)
    updated_status = await status_queries.update_status(patient_id, status, updated_by)
    
    # Send notification based on the new status
    message = {
        "patient_id": patient_id,
        "status": status,
        "updated_by": updated_by
    }
    send_push_notification(updated_by, message)
    
    return {"message": "Patient status updated", "data": updated_status}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    """WebSocket connection for real-time notifications"""
    await manager.connect(websocket, user_id)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        await manager.disconnect(user_id)
