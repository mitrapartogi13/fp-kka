"""
Test script untuk menguji fitur scrolling dan auto-center
"""
import sys
import layout
import pacman
import graphicsDisplay
import keyboardAgents
import ghostAgents

# Load layout besar
lay = layout.getLayout("bigMaze")
print(f"Layout bigMaze size: {lay.width} x {lay.height}")

# Buat ghost agents
ghosts = [ghostAgents.RandomGhost(i + 1) for i in range(2)]

# Buat display dengan scrolling enabled
print("Creating display with scrolling (viewport 800x600, auto-center enabled)...")
display = graphicsDisplay.PacmanGraphics(
    zoom=1.0,
    frameTime=0.1,
    viewport_width=800,
    viewport_height=600,
    auto_center=True
)

# Buat keyboard agent
pacman_agent = keyboardAgents.KeyboardAgent()

print("Starting game... Use WASD or arrow keys to move Pacman.")
print("The camera should follow Pacman automatically.")

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
