# realtime/app/schema/notification_schema.py
from pydantic import BaseModel
from datetime import datetime

class NotificationCreate(BaseModel):
    recipient_id: int
    message: str

class NotificationResponse(BaseModel):
    id: int
    recipient_id: int
    message: str
    timestamp: datetime
    is_read: bool
