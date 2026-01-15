import os
import sys
from pathlib import Path

# Add the backend directory to Python path to ensure relative imports work
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Change to the backend directory to ensure relative imports work properly
os.chdir(backend_dir)

# Now import and run the main app
try:
    from main import app
    import uvicorn

    print("Starting the Todo API server...")
    print("Server will be available at: http://localhost:8000")
    print("Press Ctrl+C to stop the server")

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure all dependencies are installed with: pip install -r requirements.txt")
except Exception as e:
    print(f"Error starting server: {e}")