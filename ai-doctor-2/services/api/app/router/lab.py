from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from app.helper.security import check_role
from app.helper.db import database
import asyncpg

router = APIRouter()

@router.get("/lab/requests", dependencies=[Depends(check_role("view_lab_requests"))])
async def view_lab_requests(status: Optional[str] = Query(None, description="Filter by status")):
    """
    Retrieve all lab test requests from OPD.
    Optionally, filter by request status (Pending, Completed, etc.).
    """
    query = "SELECT * FROM lab_requests"
    params = []
    
    if status:
        query += " WHERE status=$1"
        params.append(status)
    
    async with database.acquire() as conn:
        requests = await conn.fetch(query, *params) if params else await conn.fetch(query)
    
    return {"lab_requests": [dict(r) for r in requests]}
