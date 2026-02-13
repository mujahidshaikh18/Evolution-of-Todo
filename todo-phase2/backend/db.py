from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession as SqlAlchemyAsyncSession
import os
from config import settings
from models import ChatHistory  # Import ChatHistory to include it in the metadata

# Get database URL from environment variable
database_url = settings.DATABASE_URL

# Update to use asyncpg driver
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    # If it's already asyncpg, keep as is
    pass

if "?sslmode" in database_url or "&sslmode=" in database_url:
    import re
    database_url = re.sub(r'[\?&]sslmode=[^&]+', '', database_url)

# Create the async database engine
engine = create_async_engine(
    database_url,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=60,
    pool_size=5,
    max_overflow=10,
    connect_args={"ssl": "require", "server_settings": {"tcp_keepalive_idle": "600"}}
)

async def create_db_and_tables():
    """ ---Create database and tables based on the models defined.--- """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    """ ---Database and tables created successfully.--- """

async def get_session():
    """ ---Get a new async database session.--- """
    async with AsyncSession(engine) as session:
        try:
            yield session
        finally:
            await session.close()
    """ ---Async database session closed.--- """


def get_engine():
    """ ---Get the database engine for Alembic migrations.--- """
    return engine
