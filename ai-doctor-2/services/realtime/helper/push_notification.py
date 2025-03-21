import redis
import asyncpg
import json
from datetime import datetime
from app.helper.websocket import manager

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def send_push_notification(user_id: int, message: dict):
    notification_data = json.dumps(message)
    redis_client.publish("notifications", notification_data)

async def listen_notifications():
    pubsub = redis_client.pubsub()
    pubsub.subscribe("notifications")

    for message in pubsub.listen():
        if message["type"] == "message":
            data = json.loads(message["data"])
            await manager.send_notification(data["user_id"], data)


async def create_notification(conn: asyncpg.Connection, patient_id: int, message: dict, recipient_role: str, recipient_id: int):
    """
    Inserts a new notification into the database.
    - patient_id: Optional, links notification to a patient
    - message: JSON object containing details (lab request, OPD assignment, etc.)
    - recipient_role: Role of recipient ("doctor", "lab_technician")
    - recipient_id: ID of recipient user
    """
    query = """
    INSERT INTO notifications (patient_id, message, recipient_role, recipient_id, created_at, read)
    VALUES ($1, $2, $3, $4, $5, false)
    RETURNING id;
    """
    notification_id = await conn.fetchval(query, patient_id, json.dumps(message), recipient_role, recipient_id, datetime.utcnow())
    return notification_id

async def get_unread_notifications(conn: asyncpg.Connection, recipient_role: str, recipient_id: int):
    """
    Fetches unread notifications for a specific recipient.
    """
    query = "SELECT * FROM notifications WHERE recipient_role = $1 AND recipient_id = $2 AND read = false ORDER BY created_at DESC"
    return await conn.fetch(query, recipient_role, recipient_id)

async def mark_notification_as_read(conn: asyncpg.Connection, notification_id: int):
    """
    Marks a notification as read.
    """
    query = "UPDATE notifications SET read = true WHERE id = $1"
    await conn.execute(query, notification_id)


