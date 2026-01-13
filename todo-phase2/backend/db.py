from sqlmodel import SQLModel, create_engine
import os

# Import with absolute path to avoid relative import issues
from models import Task  # Import all models to register them

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

# Create engine with proper error handling for Vercel deployment
try:
    if DATABASE_URL.startswith("sqlite"):
        engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
    else:
        # For PostgreSQL, using standard connection with proper pool settings for Vercel
        engine = create_engine(
            DATABASE_URL,
            echo=True,
            pool_pre_ping=True,  # Verify connections before use
            pool_recycle=300,    # Recycle connections every 5 minutes
            pool_size=5,         # Number of connection pools
            max_overflow=10      # Maximum overflow connections
        )
except Exception as e:
    print(f"Error creating database engine: {e}")
    print(f"Using fallback SQLite database")
    # Fallback to SQLite if the DATABASE_URL is invalid
    engine = create_engine("sqlite:///./todo_fallback.db", echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)