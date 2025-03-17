import asyncpg
import asyncio
import json
from services.realtime.app.helper.websocket import manager
from services.realtime.app.helper.push_notification import send_push_notification
from database.connection import get_db_pool

async def listen_for_notifications():
    """Listens for database NOTIFY events and broadcasts them via WebSockets & Redis"""
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        await conn.execute("LISTEN new_notification;")
        await conn.execute("LISTEN patient_status_update;")

        while True:
            msg = await conn.fetchrow("SELECT pg_sleep(1);")
            notifications = await conn.fetch("SELECT * FROM pg_notification_queue;")
            
            for notification in notifications:
                payload = json.loads(notification["payload"])
                
                # Send WebSocket & Redis notifications
                await manager.send_notification(payload["user_id"], payload)
                send_push_notification(payload["user_id"], payload)

async def notify_on_insert(trigger_type: str, table_name: str):
    """Database trigger function to notify on new inserts"""
    pool = await get_db_pool()
    query = f"""
    CREATE OR REPLACE FUNCTION notify_{table_name}() RETURNS TRIGGER AS $$
    BEGIN
        PERFORM pg_notify('{trigger_type}', row_to_json(NEW)::text);
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    
    DROP TRIGGER IF EXISTS {trigger_type}_trigger ON {table_name};
    CREATE TRIGGER {trigger_type}_trigger
    AFTER INSERT ON {table_name}
    FOR EACH ROW EXECUTE FUNCTION notify_{table_name}();
    """
    async with pool.acquire() as conn:
        await conn.execute(query)

async def setup_database_triggers():
    """Sets up triggers for real-time notifications"""
    await notify_on_insert("new_notification", "notifications")
    await notify_on_insert("patient_status_update", "patient_status")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_database_triggers())
    loop.run_until_complete(listen_for_notifications())

