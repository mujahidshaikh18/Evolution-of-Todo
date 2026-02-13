import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app

# Vercel expects the FastAPI app instance to be available as 'app'
# The Vercel Python runtime will automatically serve this