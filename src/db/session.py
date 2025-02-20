from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .models import Base
from ..core.config import settings

# Create async database engine with SQLAlchemy
# Uses asyncpg driver for better performance
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # SQL query logging
    future=True  # Use SQLAlchemy 2.0 features
)

# Session factory for creating database sessions
# expire_on_commit=False prevents detached instance errors
async_session = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def init_db():
    """Initialize database tables on startup"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    """Dependency for getting database sessions in FastAPI endpoints"""
    async with async_session() as session:
        yield session 