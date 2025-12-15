# Fitur Scrolling dan Auto-Center untuk Map Besar

## Deskripsi
Fitur ini mengatasi masalah ketika map Pacman terlalu besar dan tidak muat di layar laptop. Kamera akan secara otomatis mengikuti Pacman saat bergerak.

## Cara Menggunakan

### Melalui launcher.py (GUI - Paling Mudah!) ⭐
1. Jalankan `python launcher.py`
2. Pilih mode bermain (Manual atau AI)
3. Pilih map yang diinginkan (contoh: `originalClassic`)
4. Pastikan checkbox **"Auto-Center mengikuti Pacman"** tercentang ✓
5. Klik **"MULAI GAME"**
6. Jika map besar (>15x15), scrolling otomatis aktif dengan viewport 800x600!

### Melalui pacman_ui.py (CLI - Direkomendasikan)
1. Jalankan `python pacman_ui.py`
2. Pilih mode "Main sendiri (KeyboardAgent)"
3. Masukkan nama layout yang besar, misalnya: `originalClassic`, `bigMaze`, `bigSearch`, `bigCorners`
4. Program akan otomatis mendeteksi jika:
   - Map width > 15 ATAU
   - Map height > 15 ATAU
   - Estimated window height > 650 pixels
5. Ketika ditanya "Map besar terdeteksi. Aktifkan scrolling dan auto-center mengikuti Pacman? [Y/n]:", tekan Enter atau ketik 'Y'
6. Pilih viewport size (default 800x600 atau custom)
7. Window akan muncul dengan scrollbar dan kamera mengikuti Pacman

### Secara Manual (dari kode)
```python
import graphicsDisplay

# Buat display dengan viewport 800x600 dan auto-center aktif
display = graphicsDisplay.PacmanGraphics(
    zoom=1.0, 
    frameTime=0.1,
    viewport_width=800,    # Lebar viewport (window yang terlihat)
    viewport_height=600,   # Tinggi viewport
    auto_center=True       # Aktifkan auto-center mengikuti Pacman
)
```

## Fitur yang Ditambahkan

### 1. Scrollable Canvas (`graphicsUtils.py`)
- Canvas sekarang bisa lebih besar dari window yang ditampilkan
- Scrollbar horizontal dan vertical ditambahkan secara otomatis
- Window bisa di-resize ketika mode scrolling aktif

### 2. Auto-Center Camera (`graphicsDisplay.py`)
- Kamera otomatis mengikuti posisi Pacman
- Pacman selalu di tengah layar saat bergerak
- Smooth scrolling mengikuti pergerakan

### 3. Deteksi Map Besar (`pacman_ui.py`)
- Otomatis mendeteksi map dengan kriteria:
  - Width > 15 ATAU
  - Height > 15 ATAU
  - Estimated window height > 650 pixels
- Menawarkan opsi scrolling kepada user
- User dapat memilih viewport size (default 800x600)
- Maps yang terdeteksi: mediumClassic, originalClassic, bigMaze, bigSearch, dll

## Parameter Baru

### `PacmanGraphics.__init__()`
- `viewport_width` (int, optional): Lebar window yang terlihat. None = full size
- `viewport_height` (int, optional): Tinggi window yang terlihat. None = full size
- `auto_center` (bool, optional): Aktifkan auto-center mengikuti Pacman. Default: False

### `begin_graphics()` di graphicsUtils.py
- `viewport_width` (int, optional): Lebar viewport
- `viewport_height` (int, optional): Tinggi viewport
- `auto_center` (bool, optional): Enable auto-centering

## Contoh Penggunaan

### Test dengan Launcher GUI (Termudah) ⭐
```bash
# Jalankan launcher GUI
python launcher.py

# Di GUI:
# 1. Pilih mode: "Saya Sendiri (Manual)" atau "Komputer (AI)"
# 2. Pilih map: originalClassic
# 3. Pastikan checkbox "Auto-Center mengikuti Pacman" tercentang ✓
# 4. Klik "MULAI GAME"
# 5. Main dengan WASD atau arrow keys (manual mode)
```

### Test dengan Map Besar
```bash
# Jalankan dengan UI launcher
python pacman_ui.py

# Pilih:
# 1. Mode: Main sendiri
# 2. Layout: originalClassic (atau bigMaze)
# 3. Aktifkan scrolling: Y
# 4. Viewport default: Y (800x600)
# 5. Main dengan WASD atau arrow keys
```. Mode: Main sendiri
# 2. Layout: bigMaze
# 3. Aktifkan scrolling: Y
# 4. Main dengan WASD atau arrow keys
```

### Dari Command Line (tanpa UI)
```bash
python pacman.py -l bigMaze -p KeyboardAgent
```

Catatan: Mode scrolling tersedia melalui `launcher.py` (GUI), `pacman_ui.py` (CLI), atau dengan memodifikasi kode secara manual.

## Tips
- Untuk map yang sangat besar, gunakan viewport 800x600 atau lebih kecil
- Auto-center membuat gameplay lebih mudah karena Pacman selalu terlihat
- Scrollbar bisa digunakan secara manual jika auto-center dimatikan
- Window bisa di-resize jika perlu melihat area lebih besar

## File yang Dimodifikasi
1. `graphicsUtils.py` - Menambahkan support scrollable canvas
2. `graphicsDisplay.py` - Menambahkan auto-center camera
3. `pacman_ui.py` - Menambahkan opsi scrolling untuk user
4. `launcher.py` - Menambahkan checkbox scrolling di GUI launcher
