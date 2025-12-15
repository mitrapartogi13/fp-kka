"""
Quick verification - menampilkan info map dan rekomendasi
"""
import layout

maps_to_check = [
    "tinyMaze",
    "mediumClassic", 
    "originalClassic",
    "bigMaze",
    "bigSearch"
]

print("=" * 70)
print("MAP SIZE ANALYSIS - Rekomendasi Scrolling")
print("=" * 70)

for map_name in maps_to_check:
    try:
        lay = layout.getLayout(map_name)
        width = lay.width
        height = lay.height
        
        # Hitung ukuran window
        estimated_width = (width + 2) * 30
        estimated_height = (height + 2) * 30 + 35
        
        # Tentukan apakah perlu scrolling
        needs_scroll = width > 15 or height > 15 or estimated_height > 650
        
        print(f"\n{map_name}:")
        print(f"  Size: {width} x {height}")
        print(f"  Window: ~{estimated_width} x {estimated_height} px")
        print(f"  Scrolling: {'✓ RECOMMENDED' if needs_scroll else '✗ Not needed'}")
        
    except Exception as e:
        print(f"\n{map_name}: ERROR - {e}")

print("\n" + "=" * 70)
print("Threshold: width > 15 OR height > 15 OR estimated_height > 650")
print("Default viewport: 800x600 pixels")
print("=" * 70)
