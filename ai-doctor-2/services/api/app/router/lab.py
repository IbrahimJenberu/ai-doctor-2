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

@router.post("/lab/process_result", dependencies=[Depends(check_role("process_tests"))])
async def process_lab_result(patient_id: int, test_type: str, test_result: str):
    """
    Process a lab test result for a given patient and update the lab database.
    Ensures that the test was requested before processing the result.
    """
    async with database.acquire() as conn:
        # Check if the lab request exists and is still pending
        request = await conn.fetchrow("SELECT * FROM lab_requests WHERE patient_id=$1 AND test_type=$2 AND status='Pending'", patient_id, test_type)
        if not request:
            raise HTTPException(status_code=404, detail="No pending lab test request found")
        
        # Insert lab result into the results table
        await conn.execute(
            """
            INSERT INTO lab_results (patient_id, test_type, result) VALUES ($1, $2, $3)
            """, patient_id, test_type, test_result
        )
        
        # Update lab request status to 'Completed'
        await conn.execute("UPDATE lab_requests SET status='Completed' WHERE patient_id=$1 AND test_type=$2", patient_id, test_type)
        
    return {"message": "Lab test result successfully recorded"}

@router.get("/lab/results/{patient_id}", dependencies=[Depends(check_role("receive_lab_results"))])
async def get_lab_results(patient_id: int):
    """
    Retrieve lab results for a specific patient.
    """
    async with database.acquire() as conn:
        results = await conn.fetch("SELECT * FROM lab_results WHERE patient_id=$1", patient_id)
        if not results:
            raise HTTPException(status_code=404, detail="No lab results found for this patient")
    
    return {"lab_results": [dict(r) for r in results]}

