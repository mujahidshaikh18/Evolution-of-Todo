import sys
import os
from pathlib import Path

# Add the backend directory to Python path to handle relative imports
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

# Now import and run the main app
from main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)