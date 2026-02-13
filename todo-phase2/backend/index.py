<<<<<<< HEAD

=======
import os
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
from main import app  # Import your FastAPI app

# For Vercel deployment, make sure the app instance is available
# The ASGI application
<<<<<<< HEAD
app = app
=======
application = app

# Set the port for Vercel
port = int(os.environ.get("PORT", 8000))
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
