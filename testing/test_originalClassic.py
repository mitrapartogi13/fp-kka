"""
Test script untuk originalClassic dengan scrolling
"""
import sys
import layout
import pacman
import graphicsDisplay
import keyboardAgents
import ghostAgents

# Load originalClassic
lay = layout.getLayout("originalClassic")
print(f"Layout originalClassic size: {lay.width} x {lay.height}")

# Hitung ukuran window
estimated_width = int((lay.width + 2) * 30)
estimated_height = int((lay.height + 2) * 30 + 35)
print(f"Estimated window size needed: {estimated_width} x {estimated_height} pixels")

# Buat ghost agents
ghosts = [ghostAgents.RandomGhost(i + 1) for i in range(4)]

# Buat display DENGAN scrolling
print("\nCreating display WITH scrolling (800x600 viewport)...")
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
print("Camera will follow Pacman automatically!")

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
