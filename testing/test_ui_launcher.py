"""
Test UI launcher dengan input otomatis untuk originalClassic
"""
import subprocess
import sys

# Input yang akan dikirim ke pacman_ui.py:
# 1 - Mode manual
# originalClassic - layout name
# 1 - num games
# 4 - num ghosts
# 30 - timeout
# 1 - RandomGhost
# 1.0 - zoom (default)
# 0.1 - frame time (default)
# Y - aktifkan scrolling
# Y - gunakan viewport default

inputs = """1
originalClassic
1
4
30
1
1.0
0.1
Y
Y
q
"""

print("Testing pacman_ui.py dengan originalClassic dan scrolling enabled...")
print("=" * 60)

# Jalankan dengan input otomatis
result = subprocess.run(
    [sys.executable, "pacman_ui.py"],
    input=inputs,
    text=True,
    capture_output=True,
    cwd=r"c:\Users\Indra\Programming\Kuliah\Semester 3\KKA\search"
)

print("STDOUT:")
print(result.stdout)
if result.stderr:
    print("\nSTDERR:")
    print(result.stderr)
print("\nReturn code:", result.returncode)
