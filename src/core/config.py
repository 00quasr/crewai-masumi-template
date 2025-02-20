from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Masumi Agent"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/masumi_agent")
    
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    
    # Masumi
    MASUMI_AGENT_ID: Optional[str] = os.getenv("MASUMI_AGENT_ID")
    MASUMI_API_KEY: Optional[str] = os.getenv("MASUMI_API_KEY")
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 