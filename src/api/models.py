from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime

class JobCreate(BaseModel):
    """Schema for job creation"""
    input_data: Dict[str, Any]

class JobStatus(BaseModel):
    """Schema for job status"""
    job_id: str
    status: str
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

class JobResponse(BaseModel):
    """Schema for job response"""
    status: str
    job_id: str
    payment_id: str 