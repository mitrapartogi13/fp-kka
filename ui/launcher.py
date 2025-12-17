import customtkinter as ctk
from tkinter import messagebox
import sys

# Import modul pacman yang dibutuhkan
import layout
import pacman
import graphicsDisplay
import searchAgents
import ghostAgents
import keyboardAgents

# Konfigurasi awal CustomTkinter
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("Dark")


class PacmanLauncher:
    def __init__(self, root):
        self.root = root

        # WINDOW CONFIG
        self.root.title("Pacman AI Controller - ITS C28")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.resizable(True, True)

        # Fullscreen windowed (mirip maximize)
        try:
            self.root.state("zoomed")
        except:
            pass

        # LAYOUT UTAMA
        main = ctk.CTkFrame(root)
        main.pack(fill="both", expand=True)

        # SIDEBAR
        sidebar = ctk.CTkFrame(main, width=260, corner_radius=0)
        sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            sidebar,
            text="PACMAN AI",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=(30, 5))

        ctk.CTkLabel(
            sidebar,
            text="FP KKA C-10\nProject 1: Search",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        ).pack(pady=(0, 30))

        # Switch tema Light / Dark
        self.theme_switch = ctk.CTkSwitch(
            sidebar,
            text="Dark Mode",
            command=self.toggle_theme
        )
        self.theme_switch.select()
        self.theme_switch.pack(side="bottom", pady=15)

        # Tombol Start Game
        self.start_btn = ctk.CTkButton(
            sidebar,
            text="▶ PLAY",
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.start_game
        )
        self.start_btn.pack(side="bottom", fill="x", padx=20, pady=30)

        # CONTENT
        content = ctk.CTkScrollableFrame(main)
        content.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # MODE SELECTION
        self.section_title(content, "Mode Permainan")

        self.mode_var = ctk.StringVar(value="ai")

        ctk.CTkRadioButton(
            content,
            text="Saya Sendiri (Manual - WASD)",
            variable=self.mode_var,
            value="manual",
            command=self.update_ui_state
        ).pack(anchor="w", padx=10, pady=4)

        ctk.CTkRadioButton(
            content,
            text="Komputer (AI Agents)",
            variable=self.mode_var,
            value="ai",
            command=self.update_ui_state
        ).pack(anchor="w", padx=10, pady=(0, 10))

        # AI STRATEGY
        self.algo_container = ctk.CTkFrame(content)
        self.algo_container.pack(fill="x", pady=10)

        self.section_title(self.algo_container, "Pilih Otak AI (Algoritma)")

        # Preset Algoritma
        self.search_presets = [
            (">> BEST FOR CLASSIC MAP (Greedy/Q8) <<",
             {"module": searchAgents.ClosestDotSearchAgent}),
            ("DFS - Buta & Nekat",
             {"fn": "depthFirstSearch", "prob": "PositionSearchProblem"}),
            ("BFS - Terpendek (Lambat)",
             {"fn": "breadthFirstSearch", "prob": "PositionSearchProblem"}),
            ("A* - Cerdas (Manhattan)",
             {"fn": "aStarSearch", "prob": "PositionSearchProblem", "heuristic": "manhattanHeuristic"}),
            ("A* - Food Search (Q7 - Berat!)",
             {"fn": "aStarSearch", "prob": "FoodSearchProblem", "heuristic": "foodHeuristic"}),
        ]

        self.algo_combo = ctk.CTkComboBox(
            self.algo_container,
            values=[x[0] for x in self.search_presets],
            state="readonly"
        )
        self.algo_combo.set(self.search_presets[0][0])
        self.algo_combo.pack(fill="x", padx=12, pady=10)

        # MAP SETTINGS
        self.section_title(content, "Pengaturan Map")

        # Map Layout
        self.layout_options = [
            "mediumClassic", "originalClassic", "smallClassic", "minimaxClassic",
            "openClassic", "capsuleClassic",
            "tinyMaze", "smallMaze", "mediumMaze", "bigMaze",
            "trickySearch", "bigSearch"
        ]

        self.map_combo = ctk.CTkComboBox(
            content,
            values=self.layout_options,
            state="readonly",
            command=self.update_map_preview
        )
        self.map_combo.set("mediumClassic")
        self.map_combo.pack(fill="x", padx=10, pady=6)

        # MAP PREVIEW
        self.section_title(content, "Preview Map")

        self.preview_canvas = ctk.CTkCanvas(
            content,
            width=360,
            height=220,
            bg="#111111",
            highlightthickness=0
        )
        self.preview_canvas.pack(padx=10, pady=(0, 15))

        self.update_map_preview(self.map_combo.get())

        # GHOST SETTINGS
        self.section_title(content, "Musuh (Ghost)")

        self.ghost_var = ctk.IntVar(value=1)

        ghost_row = ctk.CTkFrame(content, fg_color="transparent")
        ghost_row.pack(fill="x", padx=10)

        ctk.CTkLabel(ghost_row, text="Jumlah Ghost:").pack(side="left")

        self.ghost_value_label = ctk.CTkLabel(
            ghost_row,
            text="1",
            font=ctk.CTkFont(weight="bold")
        )
        self.ghost_value_label.pack(side="right")

        self.ghost_slider = ctk.CTkSlider(
            content,
            from_=0,
            to=4,
            number_of_steps=4,
            variable=self.ghost_var,
            command=self.update_ghost_label
        )
        self.ghost_slider.pack(fill="x", padx=10, pady=(0, 10))

        # ZOOM
        self.section_title(content, "Zoom (setara -z)")

        self.zoom_slider = ctk.CTkSlider(content, from_=0.3, to=2.0)
        self.zoom_slider.set(1.0)
        self.zoom_slider.pack(fill="x", padx=10, pady=(0, 20))

    # UI HELPERS
    def section_title(self, parent, text):
        ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=10, pady=(12, 6))

    def toggle_theme(self):
        if self.theme_switch.get():
            ctk.set_appearance_mode("Dark")
            self.theme_switch.configure(text="Dark Mode")
        else:
            ctk.set_appearance_mode("Light")
            self.theme_switch.configure(text="Light Mode")

    def update_ui_state(self):
        if self.mode_var.get() == "manual":
            self.algo_container.pack_forget()
        else:
            self.algo_container.pack(fill="x", pady=10)

    def update_ghost_label(self, value):
        self.ghost_value_label.configure(text=str(int(float(value))))

    def update_map_preview(self, map_name):
        self.preview_canvas.delete("all")
        lay = layout.getLayout(map_name)
        if lay is None:
            return

        walls = lay.walls
        width = walls.width
        height = walls.height

        canvas_w = int(self.preview_canvas["width"])
        canvas_h = int(self.preview_canvas["height"])
        cell = min(canvas_w // width, canvas_h // height)

        off_x = (canvas_w - width * cell) // 2
        off_y = (canvas_h - height * cell) // 2

        for x in range(width):
            for y in range(height):
                x1 = off_x + x * cell
                y1 = off_y + (height - y - 1) * cell
                x2 = x1 + cell
                y2 = y1 + cell

                color = "#2563eb" if walls[x][y] else "#111827"

                self.preview_canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline=""
                )

    # START GAME
    def start_game(self):
        layout_name = self.map_combo.get()
        lay = layout.getLayout(layout_name)
        if lay is None:
            messagebox.showerror("Error", f"Map '{layout_name}' tidak ditemukan!")
            return

        # Setup Agent Pacman
        if self.mode_var.get() == "manual":
            pacman_agent = keyboardAgents.KeyboardAgent()
        else:
            name = self.algo_combo.get()
            data = next(p for p in self.search_presets if p[0] == name)[1]
            pacman_agent = data["module"]() if "module" in data else searchAgents.SearchAgent(**data)

        # Setup Ghosts
        ghosts = [
            ghostAgents.RandomGhost(i + 1)
            for i in range(int(self.ghost_var.get()))
        ]

        display = graphicsDisplay.PacmanGraphics(
            zoom=self.zoom_slider.get(),
            frameTime=0.1
        )

        # Jangan destroy root, supaya window state tidak rusak
        self.root.withdraw()

        pacman.runGames(
            layout=lay,
            pacman=pacman_agent,
            ghosts=ghosts,
            display=display,
            numGames=1,
            record=False,
            catchExceptions=False,
            timeout=120
        )

        # Setelah game selesai, launcher muncul lagi
        self.root.deiconify()


if __name__ == "__main__":
    root = ctk.CTk()
    PacmanLauncher(root)
    root.mainloop()
