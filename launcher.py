import tkinter as tk
from tkinter import ttk, messagebox
import sys

# Import modul pacman yang dibutuhkan
import layout
import pacman
import graphicsDisplay
import searchAgents
import ghostAgents
import keyboardAgents

class PacmanLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Pacman AI Controller - ITS C28")
        self.root.geometry("500x600")
        
        # Style Configuration
        style = ttk.Style()
        style.theme_use('clam')
        
        # --- Header ---
        header_frame = tk.Frame(root, bg="#fcebb6")
        header_frame.pack(fill="x", pady=0)
        title_label = tk.Label(header_frame, text="PACMAN AI CONTROLLER", 
                               font=("Courier", 20, "bold"), bg="#fcebb6", fg="#333")
        title_label.pack(pady=15)
        subtitle_label = tk.Label(header_frame, text="Project 1: Search - Indra Wahyu Tirtayasa", 
                                  font=("Helvetica", 10), bg="#fcebb6", fg="#555")
        subtitle_label.pack(pady=(0, 10))

        # --- 1. Mode Selection ---
        mode_frame = ttk.LabelFrame(root, text="1. Siapa yang main?")
        mode_frame.pack(fill="x", padx=20, pady=10)
        
        self.mode_var = tk.StringVar(value="ai")
        
        # Pilihan Player Manual
        rb_manual = ttk.Radiobutton(mode_frame, text="Saya Sendiri (Manual - WASD)", 
                                   variable=self.mode_var, value="manual", command=self.update_ui_state)
        rb_manual.pack(anchor="w", padx=10, pady=5)
        
        # Pilihan AI
        rb_ai = ttk.Radiobutton(mode_frame, text="Komputer (AI Agents)", 
                               variable=self.mode_var, value="ai", command=self.update_ui_state)
        rb_ai.pack(anchor="w", padx=10, pady=5)

        # --- 2. AI Strategy Selection ---
        self.algo_frame = ttk.LabelFrame(root, text="2. Pilih Otak AI (Algoritma)")
        self.algo_frame.pack(fill="x", padx=20, pady=5)
        
        # Preset Algoritma
        # Format: (Nama Tampilan, {Parameter SearchAgent})
        self.search_presets = [
            # Opsi Terbaik untuk Map Classic
            (">> BEST FOR CLASSIC MAP (Greedy/Q8) <<", 
             {"module": searchAgents.ClosestDotSearchAgent}), 
            
            ("-----------------------------------", None),
            
            # Algoritma Standar (Hanya bagus untuk demo Pathfinding)
            ("DFS - Buta & Nekat", 
             {"fn": "depthFirstSearch", "prob": "PositionSearchProblem"}),
            ("BFS - Terpendek (Lambat)", 
             {"fn": "breadthFirstSearch", "prob": "PositionSearchProblem"}),
            ("A* - Cerdas (Manhattan)", 
             {"fn": "aStarSearch", "prob": "PositionSearchProblem", "heuristic": "manhattanHeuristic"}),
             
            ("-----------------------------------", None),
            
            # Algoritma Puzzle (Q7) - Berat untuk Classic Map
            ("A* - Food Search (Q7 - Berat!)", 
             {"fn": "aStarSearch", "prob": "FoodSearchProblem", "heuristic": "foodHeuristic"}),
        ]
        
        self.algo_combo = ttk.Combobox(self.algo_frame, values=[x[0] for x in self.search_presets], state="readonly")
        self.algo_combo.current(0) # Default ke Q8 (Playable)
        self.algo_combo.pack(fill="x", padx=10, pady=10)
        
        lbl_hint = tk.Label(self.algo_frame, text="*Gunakan opsi pertama untuk map Classic agar tidak lag", 
                           font=("Arial", 8, "italic"), fg="gray")
        lbl_hint.pack(anchor="w", padx=10)

        # --- 3. Map & Ghost Settings ---
        settings_frame = ttk.LabelFrame(root, text="3. Pengaturan Map")
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        # Map Layout
        ttk.Label(settings_frame, text="Pilih Map:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.layout_options = [
            "mediumClassic", "originalClassic", "smallClassic", "minimaxClassic", # Map Game Asli
            "trickySearch", "bigSearch", # Map Puzzle Search
            "openClassic", "capsuleClassic"
        ]
        self.map_combo = ttk.Combobox(settings_frame, values=self.layout_options)
        self.map_combo.set("mediumClassic") # Default Classic
        self.map_combo.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        
        # Ghost Count
        ttk.Label(settings_frame, text="Jumlah Musuh (Ghost):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.ghost_scale = tk.Scale(settings_frame, from_=0, to=4, orient="horizontal")
        self.ghost_scale.set(1) # Default ada musuh
        self.ghost_scale.grid(row=1, column=1, sticky="we", padx=10, pady=5)
        
        lbl_ghost_hint = tk.Label(settings_frame, text="*AI Project 1 belum bisa melihat hantu (bisa mati)", 
                                 font=("Arial", 7), fg="red")
        lbl_ghost_hint.grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        
        # Scrolling & Auto-Center Option
        ttk.Label(settings_frame, text="Scrolling (Map Besar):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.scrolling_var = tk.BooleanVar(value=True)  # Default enabled
        scrolling_check = ttk.Checkbutton(settings_frame, text="Auto-Center mengikuti Pacman", 
                                         variable=self.scrolling_var)
        scrolling_check.grid(row=3, column=1, sticky="w", padx=10, pady=5)
        
        lbl_scroll_hint = tk.Label(settings_frame, text="*Aktifkan untuk map besar agar kamera mengikuti Pacman", 
                                   font=("Arial", 7), fg="blue")
        lbl_scroll_hint.grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

        # --- Start Button ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        
        start_btn = tk.Button(btn_frame, text="MULAI GAME ▶", bg="#4CAF50", fg="white", 
                             font=("Arial", 12, "bold"), padx=20, pady=10,
                             command=self.start_game)
        start_btn.pack()

    def update_ui_state(self):
        """Enable/Disable dropdown algoritma berdasarkan mode"""
        if self.mode_var.get() == "manual":
            self.algo_frame.pack_forget() # Sembunyikan frame algoritma
        else:
            self.algo_frame.pack(fill="x", padx=20, pady=5, after=self.root.winfo_children()[1]) # Munculkan lagi

    def start_game(self):
        # 1. Validasi Layout
        layout_name = self.map_combo.get()
        lay = layout.getLayout(layout_name)
        if lay is None:
            messagebox.showerror("Error", f"Map '{layout_name}' tidak ditemukan!")
            return

        # 2. Setup Agent Pacman
        mode = self.mode_var.get()
        pacman_agent = None
        
        if mode == "manual":
            pacman_agent = keyboardAgents.KeyboardAgent()
        else:
            selected_name = self.algo_combo.get()
            
            # Handle separator selection
            if "---" in selected_name:
                messagebox.showwarning("Warning", "Pilih algoritma yang valid!")
                return
                
            selected_data = next(p for p in self.search_presets if p[0] == selected_name)[1]
            
            if "module" in selected_data:
                # Ini untuk Q8 (ClosestDot)
                pacman_agent = selected_data["module"]()
            else:
                # Ini untuk Search Agent biasa
                pacman_agent = searchAgents.SearchAgent(**selected_data)

        # 3. Setup Ghosts
        # Kita pakai RandomGhost supaya musuh bergerak acak tapi tidak terlalu agresif
        num_ghosts = self.ghost_scale.get()
        ghosts = [ghostAgents.RandomGhost(i + 1) for i in range(num_ghosts)]

        # 4. Display & Run
        # Check if map needs scrolling
        viewport_width = None
        viewport_height = None
        auto_center = False
        
        if self.scrolling_var.get():
            # Hitung ukuran window yang dibutuhkan
            map_width = lay.width
            map_height = lay.height
            estimated_height = (map_height + 2) * 30 + 35
            
            # Enable scrolling untuk map besar
            if map_width > 15 or map_height > 15 or estimated_height > 650:
                viewport_width = 800
                viewport_height = 600
                auto_center = True
                print(f"Map besar terdeteksi ({map_width}x{map_height}). Scrolling aktif dengan viewport 800x600.")
        
        display = graphicsDisplay.PacmanGraphics(zoom=1.0, frameTime=0.1,
                                                viewport_width=viewport_width,
                                                viewport_height=viewport_height,
                                                auto_center=auto_center)

        self.root.destroy() # Tutup launcher
        
        print(f"\n--- Starting Game: {layout_name} ---")
        pacman.runGames(
            layout=lay,
            pacman=pacman_agent,
            ghosts=ghosts,
            display=display,
            numGames=1,
            record=False,
            catchExceptions=False,
            timeout=120 # Timeout lebih lama untuk map besar
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PacmanLauncher(root)
    root.mainloop()