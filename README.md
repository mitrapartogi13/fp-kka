# FP Konsep Kecerdasan Artifisial - Final Praktikum Konsep Kecerdasan Artifisial

> Implementasi 4 algoritma pencarian (DFS, BFS, UCS, A*) untuk permainan Pacman

**Version:** v1.004

**Kelas: KKA C**
**Kelompok:** 
- Mitra Partogi (5025241017)
- Dimas Setiaji (5025241056)
- Indra Wahyu Tirtayasa (5025241108)

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

Final Project ini adalah implementasi dari proyek Pacman AI dari UC Berkeley yang dirancang untuk mengajarkan konsep fundamental dalam Kecerdasan Buatan (AI). Proyek ini mencakup implementasi 4 algoritma pencarian utama untuk agen Pacman.

Pacman harus belajar untuk menavigasi labirin dan mengumpulkan pelet makanan menggunakan 4 algoritma pencarian utama:
- Pencarian mendalam (Depth-First Search / DFS)
- Pencarian meluas (Breadth-First Search / BFS)
- Pencarian seragam biaya (Uniform Cost Search / UCS)
- Pencarian A* dengan heuristik (A* Search)

---

## ✨ Fitur Utama

### Algoritma Pencarian (4 Algoritma Utama)
- **DFS (Depth-First Search)** - Pencarian mendalam untuk eksplorasi ruang keadaan
- **BFS (Breadth-First Search)** - Pencarian meluas untuk menemukan solusi terpendek
- **UCS (Uniform Cost Search)** - Pencarian optimal berdasarkan biaya
- **A* Search** - Pencarian dengan heuristik untuk efisiensi maksimal

### Agen Permainan
- **SearchAgent** - Agen yang menggunakan algoritma pencarian (DFS, BFS, UCS, A*)
- **KeyboardAgent** - Kontrol manual dengan keyboard untuk testing

### Antarmuka Pengguna
- **Launcher GUI** - Interface yang user-friendly untuk menjalankan game dengan mudah
- **Grafis** - Visualisasi permainan real-time
- **Mode Teks** - Interface berbasis teks untuk testing cepat

### Fitur Tambahan
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

### ⭐ Cara Mudah - Menggunakan Launcher GUI (Rekomendasi)
```bash
python launcher.py
```

Aplikasi GUI akan membuka dengan antarmuka yang user-friendly untuk memilih:
1. **Siapa yang main?** - Pilih antara manual (keyboard) atau AI Agents
2. **Pilih Otak AI (Algoritma)** - Pilih salah satu dari:
   - DFS (Depth-First Search)
   - BFS (Breadth-First Search)
   - UCS (Uniform Cost Search)
   - A* (dengan Manhattan Heuristic)
3. **Pengaturan Map** - Pilih layout labirin dan jumlah hantu
4. **Scrolling** - Opsi untuk auto-center pada map besar

Kemudian klik tombol **MULAI GAME** untuk menjalankan game dengan konfigurasi yang dipilih.

### Menjalankan Game Standar (Manual)
```bash
python pacman.py
```
Gunakan tombol arrow atau `W`, `A`, `S`, `D` untuk bergerak.

### Menjalankan dengan SearchAgent via Command Line
Jika ingin menjalankan langsung via command line tanpa GUI:

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

### Memilih Layout/Labirin (Command Line)
```bash
python pacman.py -l tinyMaze
python pacman.py -l smallMaze
python pacman.py -l mediumMaze
python pacman.py -l bigMaze
```

### Opsi Command Line Penting
| Opsi | Deskripsi |
|------|-----------|
| `-p AGENT_TYPE` | Tipe agen Pacman (SearchAgent) |
| `-l LAYOUT` | File layout labirin (di folder `layouts/`) |
| `-a PARAMS` | Parameter untuk agen (fn=algorithm,heuristic=heuristic) |
| `-n NUM` | Jumlah game untuk dijalankan |
| `-q` | Quiet mode (tanpa graphics) |
| `-t` | Text mode (display berbasis teks) |

**⭐ Rekomendasi:** Gunakan `python launcher.py` untuk cara yang paling mudah!

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
│   ├── search.py              # Implementasi algoritma pencarian (DFS, BFS, UCS, A*)
│   ├── searchAgents.py        # Agen yang menggunakan pencarian
│   ├── pacmanAgents.py        # Agen Pacman lainnya
│   ├── keyboardAgents.py      # Agen kontrol keyboard
│   └── eightpuzzle.py         # Problem 8-puzzle untuk testing
│
├── User Interface
│   ├── graphicsDisplay.py     # Rendering grafis
│   ├── graphicsUtils.py       # Utility grafis
│   ├── textDisplay.py         # Display berbasis teks
│   ├── launcher.py            # GUI Launcher (main entry point)
│   └── pacman_ui.py           # UI utilities
│
├── Testing & Grading
│   ├── autograder.py          # Sistem grading otomatis
│   ├── grading.py             # Helper untuk grading
│   ├── searchTestClasses.py   # Test cases untuk search
│   ├── testClasses.py         # Test classes umum
│   ├── testParser.py          # Parser untuk test files
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
└── Documentation & Configuration
    ├── README.md              # File ini
    ├── VERSION                # Versi proyek (v1.004)
    ├── projectParams.py       # Parameter proyek
    └── SCROLLING_FEATURE.md   # Dokumentasi fitur scrolling
```

---

## 🔍 Algoritma Pencarian (4 Algoritma Kelompok)

### 1. Depth-First Search (DFS)
**Deskripsi:**
- Algoritma pencarian yang menggunakan **stack** (Last-In-First-Out) untuk menyimpan state
- Mengeksplorasi setiap cabang sejauh mungkin sebelum backtrack
- Cocok untuk labirin yang dalam dengan memori terbatas

**Karakteristik:**
- Completeness: Ya (untuk finite graphs)
- Optimality: Tidak menjamin solusi optimal
- Time Complexity: O(b^d) di mana b adalah branching factor dan d adalah kedalaman
- Space Complexity: O(bd) - lebih efisien dari BFS

### 2. Breadth-First Search (BFS)
**Deskripsi:**
- Algoritma pencarian yang menggunakan **queue** (First-In-First-Out) untuk menyimpan state
- Mengeksplorasi semua state pada level kedalaman n sebelum mengeksplorasi level n+1
- Menjamin menemukan solusi terpendek (dalam jumlah langkah)

**Karakteristik:**
- Completeness: Ya (untuk finite graphs)
- Optimality: Ya (untuk uniform cost)
- Time Complexity: O(b^d) - dapat membesar dengan cepat
- Space Complexity: O(b^d) - membutuhkan lebih banyak memori

### 3. Uniform Cost Search (UCS)
**Deskripsi:**
- Algoritma pencarian yang menggunakan **priority queue** berdasarkan cost kumulatif
- Mengeksplorasi state dengan cost terendah terlebih dahulu
- Menjamin solusi dengan cost total terendah (path cost)

**Karakteristik:**
- Completeness: Ya (untuk finite graphs dengan biaya positif)
- Optimality: Ya (menjamin cost minimal)
- Time Complexity: O(b^(1+⌊C*/ε⌋)) di mana C* adalah cost solusi optimal
- Space Complexity: Sama dengan time complexity

### 4. A* Search
**Deskripsi:**
- Algoritma pencarian yang menggabungkan **actual cost** (dari UCS) dengan **heuristik estimate**
- Menggunakan fungsi evaluasi: `f(n) = g(n) + h(n)`
  - `g(n)` = actual cost dari start node ke current node
  - `h(n)` = estimated cost dari current node ke goal node
- Optimal dan lebih efisien dari UCS jika heuristik admissible

**Karakteristik:**
- Completeness: Ya
- Optimality: Ya (jika heuristik admissible dan consistent)
- Time Complexity: Tergantung pada kualitas heuristik
- Space Complexity: Tergantung pada kualitas heuristik

**Heuristik yang Digunakan:**
- **manhattanHeuristic** - Jarak Manhattan: |x1-x2| + |y1-y2|
  - Cocok untuk grid dengan movement ke 4 arah (up, down, left, right)

---

## 📊 Perbandingan Algoritma

| Aspek | DFS | BFS | UCS | A* |
|-------|-----|-----|-----|-----|
| **Data Structure** | Stack | Queue | Priority Queue | Priority Queue |
| **Completeness** | ✓ | ✓ | ✓ | ✓ |
| **Optimality** | ✗ | ✓* | ✓ | ✓** |
| **Space** | O(bd) | O(b^d) | O(b^d) | O(b^d) |
| **Time** | O(b^d) | O(b^d) | O(b^(1+C*/ε)) | Tergantung h |
| **Praktis** | Cepat tapi tidak optimal | Optimal untuk cost uniform | Optimal dengan cost variabel | Optimal dan cepat |

*Optimal untuk uniform cost  
**Optimal jika heuristik admissible

---

## 🤖 Agen AI

### SearchAgent
Agen yang menggunakan salah satu dari 4 algoritma pencarian untuk menemukan path menuju goal secara otomatis.

**Menggunakan Launcher GUI (Rekomendasi):**
1. Jalankan `python launcher.py`
2. Pilih "Komputer (AI Agents)" pada opsi "Siapa yang main?"
3. Pilih salah satu algoritma: DFS, BFS, UCS, atau A*
4. Pilih map dan setting lainnya
5. Klik "MULAI GAME"

**Atau via Command Line:**
```bash
# DFS
python pacman.py -p SearchAgent -a fn=depthFirstSearch -l tinyMaze

# BFS
python pacman.py -p SearchAgent -a fn=breadthFirstSearch -l tinyMaze

# UCS
python pacman.py -p SearchAgent -a fn=uniformCostSearch -l tinyMaze

# A* dengan Manhattan Heuristic
python pacman.py -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic -l tinyMaze
```

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
python autograder.py -q q3
python autograder.py -q q4
```

### Menjalankan Test Spesifik
```bash
python autograder.py -q q1 -t test_name
```

### Verbose Mode (Lihat Detail)
```bash
python autograder.py -q q1 -v
```

---

## 📊 Struktur Test Cases

Test cases tersimpan di direktori `test_cases/` dengan struktur:

```
test_cases/
├── q1/                    # Question 1 - DFS Implementation
├── q2/                    # Question 2 - BFS Implementation
├── q3/                    # Question 3 - UCS Implementation
├── q4/                    # Question 4 - A* Search Implementation
├── q5/                    # Question 5 - Heuristics (Bonus)
├── q6/                    # Question 6 - Minimax (Opsional)
├── q7/                    # Question 7 - Alpha-Beta Pruning (Opsional)
├── q8/                    # Question 8 - Expectimax (Opsional)
└── CONFIG                 # Konfigurasi global test
```

**Fokus Kelompok:** Q1-Q4 (DFS, BFS, UCS, A*)

Setiap question memiliki:
- `*.test` - File test case dengan input
- `*.solution` - File solusi expected output
- `CONFIG` - Konfigurasi untuk question tersebut

---

## 🎯 Pembelajaran Utama

Melalui proyek ini, kami mempelajari:

1. **Representasi Masalah** - Bagaimana merepresentasikan maze sebagai search space
2. **Algoritma Pencarian Uninformed** 
   - DFS (Depth-First Search) - Pencarian mendalam
   - BFS (Breadth-First Search) - Pencarian meluas
   - UCS (Uniform Cost Search) - Pencarian berdasarkan biaya
3. **Algoritma Pencarian Informed** 
   - A* Search - Pencarian dengan heuristik Manhattan
4. **Heuristik dan Admissibility** - Evaluasi dan pemilihan fungsi heuristik yang tepat
5. **Design Patterns** - Inheritance, abstraction, dan object-oriented design
6. **Performance Analysis** - Evaluasi efisiensi algoritma dalam hal waktu dan memori

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
