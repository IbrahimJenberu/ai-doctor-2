# realtime/app/helper/websocket.py
from fastapi import WebSocket, WebSocketDisconnect
import asyncio

class ConnectionManager:
    """
    Manages active WebSocket connections.
    """
    def __init__(self):
        self.active_connections = []  # Store connected clients

    async def connect(self, websocket: WebSocket):
        """
        Accepts a WebSocket connection and adds it to the list.
        """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """
        Removes a WebSocket connection when disconnected.
        """
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """
        Sends a message to all connected clients.
        """
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

# Instantiate the connection manager
manager = ConnectionManager()
