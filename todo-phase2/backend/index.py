import os
from main import app  # Import your FastAPI app

# For Vercel deployment, make sure the app instance is available
# The ASGI application
application = app

# Set the port for Vercel
port = int(os.environ.get("PORT", 8000))