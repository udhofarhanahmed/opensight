"""
OpenSight Pro - Streamlit Cloud Entry Point
This file is required for Streamlit Cloud deployment
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Import and run the main app
from frontend.app import *
