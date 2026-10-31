import os
import sys

# Set VERCEL environment flag
os.environ["VERCEL"] = "1"

# Ensure backend directory is in sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.join(root_dir, "backend")

if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Import FastAPI application
from app.main import app

