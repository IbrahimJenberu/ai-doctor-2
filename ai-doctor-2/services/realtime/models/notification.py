from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class Notification(BaseModel):
    """Represents a notification structure in the database"""
    id: int
    patient_id: Optional[int] = None  # Some notifications might not be patient-related
    message: Dict  # JSON-encoded message for structured data
    recipient_role: str  # Example: "doctor", "lab_technician", "admin"
    recipient_id: int  # ID of the recipient user
    created_at: datetime
    read: bool

class NotificationCreate(BaseModel):
    """Schema for creating a new notification"""
    patient_id: Optional[int] = None
    message: Dict
    recipient_role: str
    recipient_id: int
