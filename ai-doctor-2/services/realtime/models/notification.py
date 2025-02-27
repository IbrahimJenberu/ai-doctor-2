# realtime/app/models/notification.py
from pydantic import BaseModel
from datetime import datetime

class Notification(BaseModel):
    id: int
    recipient_id: int  # User ID to whom the notification is sent
    message: str
    timestamp: datetime
    is_read: bool = False
