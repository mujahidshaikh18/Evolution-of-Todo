import sys
import os
from pathlib import Path

# Add parent directory to path for imports
repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from main import app

# Vercel expects the FastAPI app instance to be available as 'app'
# The Vercel Python runtime will automatically serve this