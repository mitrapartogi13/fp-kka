#!/usr/bin/env python
"""
Main launcher script - wrapper for easy access from root directory
Run this from the project root to launch the Pacman AI Controller GUI
"""

import sys
import os

# Add folders to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_root, 'ui'))
sys.path.insert(0, os.path.join(project_root, 'core_game'))
sys.path.insert(0, os.path.join(project_root, 'search_ai'))

# Import and run the launcher from ui folder
from ui import launcher

if __name__ == '__main__':
    launcher.main()
