from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
from pathlib import Path
from contextlib import asynccontextmanager

# Add the project root to the Python path
file_path = Path(__file__).resolve().parent / "phase3_ai_engine"
sys.path.append(str(file_path))

from phase3_ai_engine.services.chat_service import ChatService

from config import settings

# Import with absolute paths to avoid relative import issues
import db
import routes.tasks
import routes.auth
import routes.chat  # Enable chat routes

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_db_and_tables()
    yield

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="RESTful API for Todo Full-Stack Web Application",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
origins = [
    "https://todo-mujahidshaikh18.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.auth.router)
app.include_router(routes.tasks.router, prefix="/api/{user_id}")
app.include_router(routes.chat.router)  # Enable chat router

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))