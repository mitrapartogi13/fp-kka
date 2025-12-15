"""
Test script untuk memastikan backward compatibility (tanpa scrolling)
"""
import sys
import layout
import pacman
import graphicsDisplay
import keyboardAgents
import ghostAgents

# Load layout kecil
lay = layout.getLayout("mediumClassic")
print(f"Layout mediumClassic size: {lay.width} x {lay.height}")

# Buat ghost agents
ghosts = [ghostAgents.RandomGhost(i + 1) for i in range(2)]

# Buat display TANPA scrolling (default behavior)
print("Creating display without scrolling (normal mode)...")
display = graphicsDisplay.PacmanGraphics(
    zoom=1.0,
    frameTime=0.1
)

# Buat keyboard agent
pacman_agent = keyboardAgents.KeyboardAgent()

print("Starting game... Use WASD or arrow keys to move Pacman.")
print("This should work exactly like before (no scrolling).")

# Run game
pacman.runGames(
    layout=lay,
    pacman=pacman_agent,
    ghosts=ghosts,
    display=display,
    numGames=1,
    record=False,
    numTraining=0,
    catchExceptions=False,
    timeout=30
)
