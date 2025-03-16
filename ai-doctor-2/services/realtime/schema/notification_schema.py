from pydantic import BaseModel
from typing import List
from models.notification import Notification

class NotificationListResponse(BaseModel):
    """Schema for returning a list of notifications"""
    notifications: List[Notification]

class NotificationResponse(BaseModel):
    """Schema for an individual notification response"""
    success: bool
    notification: Notification
