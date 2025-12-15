#!/usr/bin/env python
"""
Root wrapper for Pacman CLI and module access.
- When run: forwards CLI args to core_game.pacman
- When imported: re-exports symbols from core_game.pacman (e.g., runGames)
"""
import os
import sys

# Ensure packages are on path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(PROJECT_ROOT, 'core_game')
SEARCH_DIR = os.path.join(PROJECT_ROOT, 'search_ai')
UI_DIR = os.path.join(PROJECT_ROOT, 'ui')
if CORE_DIR not in sys.path:
    sys.path.insert(0, CORE_DIR)
if SEARCH_DIR not in sys.path:
    sys.path.insert(0, SEARCH_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if UI_DIR not in sys.path:
    sys.path.insert(0, UI_DIR)

# Import the real pacman module from core_game and re-export
from core_game import pacman as _core_pacman  # type: ignore
from core_game.pacman import *  # re-export public API

if __name__ == '__main__':
    # Ensure loadAgent in core_game/pacman can discover agents under search_ai
    existing = os.environ.get('PYTHONPATH', '')
    sep = ';' if os.name == 'nt' else ':'
    add_paths = [SEARCH_DIR, CORE_DIR, UI_DIR, PROJECT_ROOT]
    to_add = sep.join([p for p in add_paths if p and p not in existing])
    os.environ['PYTHONPATH'] = (existing + (sep if existing and to_add else '') + to_add) if (existing or to_add) else ''

    # Mirror core_game/pacman __main__ behavior
    args = _core_pacman.readCommand(sys.argv[1:])
    _core_pacman.runGames(**args)
