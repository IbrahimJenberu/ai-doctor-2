# realtime/app/models/notification.py
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Notification(Base):
    """
    Defines the Notification model for storing real-time events.
    """
    __tablename__ = "notifications"

    id = Column(String, primary_key=True, index=True)  # Unique notification ID
    event_type = Column(String, nullable=False)  # Type of event (e.g., "AI_Result")
    event_data = Column(String, nullable=False)  # Event data (JSON format)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)  # Timestamp

