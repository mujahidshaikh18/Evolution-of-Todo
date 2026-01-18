from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from config import settings

# Import with absolute paths to avoid relative import issues
import db
import routes.tasks
import routes.auth

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="RESTful API for Todo Full-Stack Web Application",
    version="1.0.0"
)

# Add CORS middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.auth.router)
app.include_router(routes.tasks.router, prefix="/api/{user_id}")

@app.on_event("startup")
def startup_event():
    db.create_db_and_tables()

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