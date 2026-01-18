from sqlmodel import SQLModel, create_engine, Session
import os
from config import settings

# Get database URL from environment variable
database_url = settings.DATABASE_URL

# Create engine with proper error handling for Vercel deployment

if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
if "neon.tech" in database_url and "sslmode=" not in database_url:
        # For Neon PostgreSQL, enforce SSL connection
        connector = "&" if "?" in database_url else "?"
        database_url += f"{connector}sslmode=require"

# Create the database engine
engine = create_engine(
    database_url, 
    echo=True,
    pool_pre_ping=True,  
    pool_recycle=300,   
    connect_args={"sslmode": "require"} 
)

def create_db_and_tables():
    """ ---Create database and tables based on the models defined.--- """
    SQLModel.metadata.create_all(engine)
    """ ---Database and tables created successfully.--- """

def get_session():
    """ ---Get a new database session.--- """
    with Session(engine) as session:
        yield session
    """ ---Database session closed.--- """