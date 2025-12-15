"""
CLI launcher for Pacman that lets users pick manual play or search-driven agents.
Run with: python pacman_ui.py
"""
from __future__ import annotations

import sys
import layout
import pacman
import graphicsDisplay
import textDisplay
import ghostAgents
import searchAgents
import keyboardAgents

# Preset search-agent configurations the menu can offer.
SEARCH_AGENT_PRESETS = [
    ("DFS (PositionSearch)", dict(fn="depthFirstSearch", prob="PositionSearchProblem")),
    ("BFS (PositionSearch)", dict(fn="breadthFirstSearch", prob="PositionSearchProblem")),
    ("Uniform Cost (PositionSearch)", dict(fn="uniformCostSearch", prob="PositionSearchProblem")),
    ("A* Manhattan (PositionSearch)", dict(fn="aStarSearch", prob="PositionSearchProblem", heuristic="manhattanHeuristic")),
    ("A* Corners (cornersHeuristic)", dict(fn="aStarSearch", prob="CornersProblem", heuristic="cornersHeuristic")),
    ("A* Food (foodHeuristic)", dict(fn="aStarSearch", prob="FoodSearchProblem", heuristic="foodHeuristic")),
]

GHOST_OPTIONS = [
    ("RandomGhost", ghostAgents.RandomGhost),
    ("DirectionalGhost", ghostAgents.DirectionalGhost),
]


def prompt_choice(title: str, options, default_index: int = 0):
    """Generic numbered menu helper."""
    print(f"\n{title}")
    for idx, (label, _) in enumerate(options, start=1):
        print(f"  {idx}. {label}")
    while True:
        raw = input(f"Pilih opsi [default {default_index + 1}]: ").strip()
        if not raw:
            return options[default_index]
        if raw.isdigit():
            pos = int(raw) - 1
            if 0 <= pos < len(options):
                return options[pos]
        print("Input tidak valid, coba lagi.")


def prompt_int(prompt: str, default: int):
    raw = input(f"{prompt} [default {default}]: ").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        print("Bukan angka, memakai default.")
        return default


def prompt_float(prompt: str, default: float):
    raw = input(f"{prompt} [default {default}]: ").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        print("Bukan angka, memakai default.")
        return default


def build_display(use_text: bool, zoom: float, frame_time: float, viewport_width=None, viewport_height=None, auto_center=False):
    if use_text:
        textDisplay.SLEEP_TIME = frame_time
        return textDisplay.PacmanGraphics()
    return graphicsDisplay.PacmanGraphics(zoom=zoom, frameTime=frame_time, 
                                         viewport_width=viewport_width, 
                                         viewport_height=viewport_height,
                                         auto_center=auto_center)


def main():
    print("=== Pacman Launcher ===")
    mode_options = [
        ("Main sendiri (KeyboardAgent)", "manual"),
        ("Pakai SearchAgent", "search"),
    ]
    _, mode = prompt_choice("Pilih mode bermain", mode_options)

    layout_name = input("Nama layout (lihat folder layouts) [default mediumClassic]: ").strip() or "mediumClassic"
    lay = layout.getLayout(layout_name)
    if lay is None:
        print(f"Layout {layout_name} tidak ditemukan. Keluar.")
        sys.exit(1)

    num_games = prompt_int("Berapa kali dimainkan", 1)
    num_ghosts = prompt_int("Jumlah ghost", 4)
    timeout = prompt_int("Timeout per game (detik)", 30)

    ghost_label, ghost_class = prompt_choice("Pilih tipe ghost", GHOST_OPTIONS)
    ghosts = [ghost_class(i + 1) for i in range(num_ghosts)]

    viewport_width = None
    viewport_height = None
    auto_center = False

    if mode == "manual":
        print("Mode manual membutuhkan jendela grafis. Gunakan WASD atau panah.")
        pacman_agent = keyboardAgents.KeyboardAgent()
        use_text = False
        zoom = prompt_float("Zoom window", 1.0)
        frame_time = prompt_float("Frame time (detik)", 0.1)
        
        # Cek apakah map besar, tawarkan opsi scrolling
        map_width = lay.width
        map_height = lay.height
        
        # Hitung ukuran window yang dibutuhkan (approximation)
        # DEFAULT_GRID_SIZE = 30, dengan zoom dan margin
        estimated_width = int((map_width + 2) * 30 * zoom)
        estimated_height = int((map_height + 2) * 30 * zoom + 35)  # +35 untuk info pane
        
        print(f"\nUkuran map: {map_width} x {map_height}")
        print(f"Ukuran window yang dibutuhkan: ~{estimated_width} x {estimated_height} pixels")
        
        # Threshold lebih rendah: 15x15 atau estimated height > 650
        if map_width > 15 or map_height > 15 or estimated_height > 650:
            scroll_choice = input("Map besar terdeteksi. Aktifkan scrolling dan auto-center mengikuti Pacman? [Y/n]: ").strip().lower()
            if scroll_choice != "n":
                auto_center = True
                
                # Tanyakan apakah user ingin custom viewport atau pakai default
                custom_viewport = input("Gunakan viewport default 800x600? [Y/n]: ").strip().lower()
                if custom_viewport == "n":
                    viewport_width = prompt_int("Lebar viewport (pixels)", 800)
                    viewport_height = prompt_int("Tinggi viewport (pixels)", 600)
                else:
                    viewport_width = 800
                    viewport_height = 600
                
                print("Mode scrolling aktif - kamera akan mengikuti Pacman")
                print(f"Viewport: {viewport_width}x{viewport_height} (dengan scrollbar untuk navigasi)")
    else:
        label, preset = prompt_choice("Pilih SearchAgent", SEARCH_AGENT_PRESETS)
        print(f"Memakai {label}")
        pacman_agent = searchAgents.SearchAgent(**preset)
        # User dapat memilih ingin teks atau grafis.
        text_mode_choice = input("Pakai text-only display? [y/N]: ").strip().lower()
        use_text = text_mode_choice == "y"
        zoom = 1.0
        frame_time = prompt_float("Frame time (detik)", 0.1)

    display = build_display(use_text, zoom, frame_time, viewport_width, viewport_height, auto_center)

    print("\nMenjalankan game...\n")
    pacman.runGames(
        layout=lay,
        pacman=pacman_agent,
        ghosts=ghosts,
        display=display,
        numGames=num_games,
        record=False,
        numTraining=0,
        catchExceptions=False,
        timeout=timeout,
    )


if __name__ == "__main__":
    main()
