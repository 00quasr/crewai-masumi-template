from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    """
    Database model for tracking agent jobs.
    
    Attributes:
        id (int): Primary key for the job
        status (str): Current job status (pending/running/completed/error)
        payment_id (str): Masumi Network payment identifier
        created_at (datetime): When the job was created
        started_at (datetime): When job execution began
        completed_at (datetime): When job finished
        result (json): Job results in JSON format
        error (str): Error message if job failed
    """
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True)
    status = Column(String, default="pending")
    payment_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    result = Column(JSON, nullable=True)
    error = Column(String, nullable=True) 