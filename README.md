# FPKKA - Final Praktikum Konsep Kecerdasan Artifisial

> Implementasi algoritma pencarian dan agen AI untuk permainan Pacman

**Version:** v1.004

---

## 📋 Daftar Isi
- [Deskripsi Proyek](#deskripsi-proyek)
- [Fitur Utama](#fitur-utama)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [Algoritma Pencarian](#algoritma-pencarian)
- [Agen AI](#agen-ai)
- [Menjalankan Tes](#menjalankan-tes)
- [Kontribusi & Lisensi](#kontribusi--lisensi)

---

## 🎮 Deskripsi Proyek

FPKKA adalah implementasi dari proyek Pacman AI dari UC Berkeley yang dirancang untuk mengajarkan konsep fundamental dalam Kecerdasan Buatan (AI). Proyek ini mencakup implementasi berbagai algoritma pencarian dan strategi permainan untuk agen Pacman.

Pacman harus belajar untuk menavigasi labirin, mengumpulkan pelet makanan, dan menghindari hantu menggunakan berbagai teknik AI termasuk:
- Pencarian mendalam (Depth-First Search)
- Pencarian meluas (Breadth-First Search)
- Pencarian seragam biaya (Uniform Cost Search)
- Pencarian A* dengan heuristik
- Minimax dan Alpha-Beta Pruning
- Expectimax Algorithm

---

## ✨ Fitur Utama

### Algoritma Pencarian
- **DFS (Depth-First Search)** - Pencarian mendalam untuk eksplorasi ruang keadaan
- **BFS (Breadth-First Search)** - Pencarian meluas untuk menemukan solusi terpendek
- **UCS (Uniform Cost Search)** - Pencarian optimal berdasarkan biaya
- **A* Search** - Pencarian dengan heuristik untuk efisiensi maksimal
- **Minimax** - Algoritma permainan adversarial
- **Alpha-Beta Pruning** - Optimasi minimax dengan pengurangan cabang

### Agen Permainan
- **SearchAgent** - Agen yang menggunakan algoritma pencarian
- **PacmanAgent** - Agen Pacman standar
- **GhostAgents** - Berbagai strategi agen hantu (random, greedy, intelligent)
- **KeyboardAgent** - Kontrol manual dengan keyboard

### Antarmuka Pengguna
- **Grafis** - Visualisasi permainan real-time
- **Mode Teks** - Interface berbasis teks untuk testing
- **Launcher UI** - Interface GUI untuk menjalankan eksperimen

### Fitur Tambahan
- **Scrolling Layout** - Dukungan untuk labirin berukuran besar
- **Multiple Mazes** - 30+ labirin dengan tingkat kesulitan berbeda
- **Autograder** - Sistem penilaian otomatis untuk validasi solusi

---

## 💻 Persyaratan Sistem

- **Python:** 3.6 atau lebih tinggi
- **OS:** Windows, macOS, atau Linux
- **Dependencies:** 
  - tkinter (untuk GUI, biasanya built-in dengan Python)
  - Tidak ada library eksternal yang diperlukan

---

## 🚀 Instalasi

### 1. Clone atau Download Proyek
```bash
git clone <repository-url>
cd FPKKA
```

### 2. Verifikasi Python
```bash
python --version
```

### 3. (Opsional) Buat Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Tidak perlu instalasi dependencies tambahan karena proyek hanya menggunakan library standard Python.

---

## 📖 Cara Penggunaan

### Menjalankan Game Standar
```bash
python pacman.py
```
Gunakan tombol arrow atau `W`, `A`, `S`, `D` untuk bergerak.

### Menjalankan dengan SearchAgent
```bash
# Depth-First Search
python pacman.py -p SearchAgent -a fn=depthFirstSearch

# Breadth-First Search
python pacman.py -p SearchAgent -a fn=breadthFirstSearch

# Uniform Cost Search
python pacman.py -p SearchAgent -a fn=uniformCostSearch

# A* Search
python pacman.py -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic
```

### Memilih Layout/Labirin
```bash
python pacman.py -l tinyMaze
python pacman.py -l smallMaze
python pacman.py -l mediumMaze
python pacman.py -l bigMaze
```

### Menjalankan dengan Hantu
```bash
python pacman.py -p SearchAgent -a fn=depthFirstSearch -l smallMaze -g GhostAgent
```

### Opsi Command Line Penting
| Opsi | Deskripsi |
|------|-----------|
| `-p AGENT_TYPE` | Tipe agen Pacman |
| `-l LAYOUT` | File layout labirin (di folder `layouts/`) |
| `-g GHOST_TYPE` | Tipe agen hantu |
| `-a PARAMS` | Parameter untuk agen |
| `-n NUM` | Jumlah game untuk dijalankan |
| `-q` | Quiet mode (tanpa graphics) |

---

## 📁 Struktur Proyek

```
FPKKA/
├── Core Game Files
│   ├── pacman.py              # Logika permainan utama
│   ├── game.py                # Framework permainan
│   ├── layout.py              # Parser labirin
│   └── util.py                # Utility functions
│
├── Search & AI
│   ├── search.py              # Implementasi algoritma pencarian
│   ├── searchAgents.py        # Agen yang menggunakan pencarian
│   ├── ghostAgents.py         # Implementasi agen hantu
│   ├── pacmanAgents.py        # Agen Pacman lainnya
│   ├── keyboardAgents.py      # Agen kontrol keyboard
│   └── eightpuzzle.py         # Problem 8-puzzle untuk testing
│
├── User Interface
│   ├── graphicsDisplay.py     # Rendering grafis
│   ├── graphicsUtils.py       # Utility grafis
│   ├── textDisplay.py         # Display berbasis teks
│   ├── pacman_ui.py           # UI utilities
│   └── launcher.py            # GUI launcher
│
├── Testing & Grading
│   ├── autograder.py          # Sistem grading otomatis
│   ├── grading.py             # Helper untuk grading
│   ├── searchTestClasses.py   # Test cases untuk search
│   ├── testClasses.py         # Test classes umum
│   ├── testParser.py          # Parser untuk test files
│   ├── test_*.py              # Various test scripts
│   └── test_cases/            # Direktori berisi test cases
│       ├── q1/ - q8/          # Questions/problems per bagian
│       └── CONFIG             # Konfigurasi test
│
├── Game Assets
│   ├── layouts/               # 30+ file layout labirin
│   │   ├── tinyMaze.lay
│   │   ├── smallMaze.lay
│   │   ├── mediumMaze.lay
│   │   └── ... (30+ layouts)
│   └── __pycache__/           # Python cache
│
├── Documentation & Configuration
│   ├── README.md              # File ini
│   ├── VERSION                # Versi proyek (v1.004)
│   ├── projectParams.py       # Parameter proyek
│   ├── SCROLLING_FEATURE.md   # Dokumentasi fitur scrolling
│   ├── VERIFICATION.py        # Verifikasi proyek
│   └── check_map_sizes.py     # Checker ukuran map

```

---

## 🔍 Algoritma Pencarian

### 1. Depth-First Search (DFS)
- Menggunakan **stack** untuk penyimpanan state
- Cocok untuk labirin yang dalam
- Fungsi: `search.depthFirstSearch(problem)`

### 2. Breadth-First Search (BFS)
- Menggunakan **queue** untuk penyimpanan state
- Menjamin solusi terpendek (dalam jumlah langkah)
- Fungsi: `search.breadthFirstSearch(problem)`

### 3. Uniform Cost Search (UCS)
- Menggunakan **priority queue** berdasarkan cost
- Menjamin solusi dengan cost terendah
- Fungsi: `search.uniformCostSearch(problem)`

### 4. A* Search
- Menggabungkan UCS dengan heuristik
- Formula: `f(n) = g(n) + h(n)`
  - `g(n)` = actual cost dari start ke node n
  - `h(n)` = estimated cost dari n ke goal
- Fungsi: `search.aStarSearch(problem, heuristic)`

### Heuristik yang Tersedia
- **nullHeuristic** - Heuristik trivial (h=0)
- **manhattanHeuristic** - Manhattan distance
- **euclideanHeuristic** - Euclidean distance

---

## 🤖 Agen AI

### SearchAgent
Agen yang menggunakan algoritma pencarian untuk menemukan path menuju goal.

```bash
python pacman.py -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic
```

### Ghost Agents
Berbagai implementasi agen hantu:
- **RandomGhost** - Bergerak secara acak
- **DirectionalGhost** - Bergerak ke arah tertentu
- **SmartGhost** - Menggunakan strategi pintar untuk mengejar Pacman

---

## 🧪 Menjalankan Tes

### Menjalankan Semua Test Cases
```bash
python autograder.py
```

### Menjalankan Test untuk Question Tertentu
```bash
python autograder.py -q q1
python autograder.py -q q2
```

### Menjalankan Test Spesifik
```bash
python autograder.py -q q1 -t test_name
```

### Verbose Mode (Lihat Detail)
```bash
python autograder.py -q q1 -v
```

### Test Manual untuk Launcher
```bash
python test_launcher_manual.py
python test_ui_launcher.py
```

### Test Scrolling Feature
```bash
python test_scrolling.py
```

### Check Map Sizes
```bash
python check_map_sizes.py
```

---

## 📊 Struktur Test Cases

Test cases tersimpan di direktori `test_cases/` dengan struktur:

```
test_cases/
├── q1/                    # Question 1 - Basic Search
├── q2/                    # Question 2 - DFS/BFS Implementation
├── q3/                    # Question 3 - UCS
├── q4/                    # Question 4 - A* Search
├── q5/                    # Question 5 - Heuristics
├── q6/                    # Question 6 - Minimax
├── q7/                    # Question 7 - Alpha-Beta Pruning
├── q8/                    # Question 8 - Expectimax
└── CONFIG                 # Konfigurasi global test

```

Setiap question memiliki:
- `*.test` - File test case dengan input
- `*.solution` - File solusi expected output
- `CONFIG` - Konfigurasi untuk question tersebut

---

## 🎯 Pembelajaran Utama

Melalui proyek ini, Anda akan mempelajari:

1. **Representasi Masalah** - Bagaimana merepresentasikan problem sebagai search space
2. **Algoritma Pencarian Uninformed** - DFS, BFS, UCS
3. **Algoritma Pencarian Informed** - A* dengan berbagai heuristik
4. **Adversarial Search** - Minimax, Alpha-Beta Pruning
5. **Expectimax** - Keputusan di bawah uncertainty
6. **Design Patterns** - Inheritance, abstraction, dan object-oriented design
7. **Performance Analysis** - Evaluasi efisiensi algoritma

---

## 🔧 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'tkinter'`
**Solusi:** Install python-tk
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (dengan Homebrew)
brew install python-tk

# Windows: Tkinter biasanya sudah included
```

### Error: Graphics tidak muncul
Jalankan dengan opsi `-t` (text mode) untuk text display:
```bash
python pacman.py -t
```

### Test cases tidak ditemukan
Pastikan Anda menjalankan command dari root directory proyek:
```bash
cd path/to/FPKKA
python autograder.py
```

---

## 📝 Catatan Penting

- **Jangan** modifikasi file yang bukan bagian dari assignment
- Fokus pada implementasi di `search.py` dan `searchAgents.py`
- Pastikan solusi Anda melewati semua test cases sebelum submission
- Gunakan `autograder.py` untuk validasi sebelum final submission

---

## 🔗 Referensi

- **UC Berkeley AI Projects:** http://ai.berkeley.edu
- **Project Attribution:** 
  - John DeNero (denero@cs.berkeley.edu)
  - Dan Klein (klein@cs.berkeley.edu)
  - Brad Miller, Nick Hay, Pieter Abbeel

---

## 📜 Lisensi

Proyek ini adalah bagian dari UC Berkeley Pacman AI Projects. 
- Anda bebas menggunakan dan memperluas proyek ini untuk tujuan pendidikan
- Jangan distribusikan atau publikasikan solusi
- Pertahankan atribusi ke UC Berkeley

---

## 👨‍💻 Kontribusi

Untuk berkontribusi atau melaporkan bug:
1. Buat branch baru untuk fitur/fix Anda
2. Commit dengan pesan yang deskriptif
3. Push ke repository
4. Buat Pull Request dengan penjelasan detail

---

**Last Updated:** December 2025 | **Version:** v1.004
