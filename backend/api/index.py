import sys
import os

# Add the backend directory to sys.path so we can import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# This is required for Vercel
# The 'app' object will be handled by Vercel's Python runtime
