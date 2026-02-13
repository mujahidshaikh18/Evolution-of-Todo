from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
<<<<<<< HEAD
import sys
from pathlib import Path
from contextlib import asynccontextmanager

# Add the project root to the Python path to enable imports from phase3_ai_engine
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config import settings
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

# Import with absolute paths to avoid relative import issues
import db
import routes.tasks
import routes.auth
<<<<<<< HEAD
import routes.chat  # Enable chat routes

from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_db_and_tables()
    yield
=======
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="RESTful API for Todo Full-Stack Web Application",
<<<<<<< HEAD
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
=======
    version="1.0.0"
)

# Add CORS middleware
allowed_origins_raw = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
allowed_origins = allowed_origins_raw.split(",") if allowed_origins_raw else ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.auth.router)
app.include_router(routes.tasks.router, prefix="/api/{user_id}")
<<<<<<< HEAD
app.include_router(routes.chat.router)  # Enable chat router
=======

@app.on_event("startup")
def startup_event():
    db.create_db_and_tables()
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# For Vercel deployment, make the app available at the module level
# Vercel will automatically use the 'app' variable as the ASGI application
try:
    # This is needed for Vercel Python runtime
    import uvicorn
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
except ImportError:
    # When deployed to Vercel, uvicorn might not be available
    pass