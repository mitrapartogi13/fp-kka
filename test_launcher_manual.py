"""
Test launcher.py secara programmatic dengan originalClassic dan manual mode
"""
import tkinter as tk
import sys
import os

# Simulasi klik button via code
def auto_test_launcher():
    # Import setelah tkinter ready
    sys.path.insert(0, r'c:\Users\Indra\Programming\Kuliah\Semester 3\KKA\search')
    
    import launcher
    
    root = tk.Tk()
    app = launcher.PacmanLauncher(root)
    
    # Set mode manual
    app.mode_var.set("manual")
    app.update_ui_state()
    
    # Set map ke originalClassic
    app.map_combo.set("originalClassic")
    
    # Set ghost count
    app.ghost_scale.set(2)
    
    # Enable scrolling
    app.scrolling_var.set(True)
    
    print("Testing launcher.py configuration:")
    print(f"  Mode: {app.mode_var.get()}")
    print(f"  Map: {app.map_combo.get()}")
    print(f"  Ghosts: {app.ghost_scale.get()}")
    print(f"  Scrolling: {app.scrolling_var.get()}")
    print("\nClick 'MULAI GAME' button to start...")
    print("(Window akan muncul dengan scrolling enabled)")
    
    root.mainloop()

if __name__ == "__main__":
    auto_test_launcher()
