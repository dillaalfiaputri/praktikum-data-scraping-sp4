import os

# FUNGSI VALIDASI DAN PEMBUATAN FOLDER

def buat_folder(nama_folder):
    """Membuat folder baru dengan validasi os.path.exists"""
    sudah_ada = os.path.exists(nama_folder)
    print(f"Validasi folder '{nama_folder}': {sudah_ada}")

    if not sudah_ada:
        os.mkdir(nama_folder)
        print(f"  => Folder '{nama_folder}' berhasil dibuat.\n")
    else:
        print(f"  => Folder '{nama_folder}' sudah ada, dilewati.\n")

# FUNGSI VALIDASI DAN PEMBUATAN FILE

def buat_file(path_file, isi_teks):
    """Membuat file teks baru dengan validasi os.path.exists"""
    sudah_ada = os.path.exists(path_file)
    print(f"  Validasi file '{path_file}': {sudah_ada}")

    if not sudah_ada:
        with open(path_file, 'w') as f:
            f.write(isi_teks + "\n")
        print(f"    => File '{path_file}' berhasil dibuat.")
    else:
        print(f"    => File '{path_file}' sudah ada, dilewati.")

# DATA: 5 KATEGORI DAN 5 FILE PER KATEGORI

kategori = {
    "Kategori_1": {
        "tema": "Elektronik",
        "file": [
            ("produk_laptop.txt",     "Data scraping: daftar harga laptop terbaru dari tokopedia.com"),
            ("produk_hp.txt",         "Data scraping: daftar harga smartphone dari shopee.com"),
            ("produk_tablet.txt",     "Data scraping: spesifikasi tablet terpopuler 2024"),
            ("produk_aksesoris.txt",  "Data scraping: aksesoris elektronik best seller"),
            ("produk_audio.txt",      "Data scraping: headphone dan speaker trending"),
        ]
    },
    "Kategori_2": {
        "tema": "Fashion",
        "file": [
            ("baju_pria.txt",         "Data scraping: koleksi baju pria terlaris di zalora.com"),
            ("baju_wanita.txt",       "Data scraping: koleksi baju wanita terpopuler"),
            ("sepatu.txt",            "Data scraping: daftar harga sepatu branded diskon"),
            ("tas.txt",               "Data scraping: tas import murah rekomendasi"),
            ("aksesoris.txt",         "Data scraping: aksesoris fashion trending 2024"),
        ]
    },
    "Kategori_3": {
        "tema": "Kuliner",
        "file": [
            ("restoran_jember.txt",   "Data scraping: daftar restoran populer di Jember"),
            ("menu_harga.txt",        "Data scraping: perbandingan harga menu makanan online"),
            ("rating_tempat.txt",     "Data scraping: rating tempat makan dari Google Maps"),
            ("promo_makanan.txt",     "Data scraping: promo GoFood dan GrabFood hari ini"),
            ("resep_viral.txt",       "Data scraping: resep masakan viral dari TikTok"),
        ]
    },
    "Kategori_4": {
        "tema": "Berita",
        "file": [
            ("berita_teknologi.txt",  "Data scraping: headline berita teknologi dari detik.com"),
            ("berita_ekonomi.txt",    "Data scraping: berita ekonomi terkini dari kompas.com"),
            ("berita_olahraga.txt",   "Data scraping: hasil pertandingan sepakbola hari ini"),
            ("berita_pendidikan.txt", "Data scraping: info beasiswa dan pendidikan terbaru"),
            ("berita_lokal.txt",      "Data scraping: berita lokal Jember dari radar jember"),
        ]
    },
    "Kategori_5": {
        "tema": "Quotes",
        "file": [
            ("quotes_motivasi.txt",   "Data scraping: quotes motivasi dari quotes.toscrape.com"),
            ("quotes_inspirasi.txt",  "Data scraping: quotes inspirasi tokoh dunia"),
            ("quotes_humor.txt",      "Data scraping: quotes humor dan lucu"),
            ("quotes_cinta.txt",      "Data scraping: quotes cinta dan persahabatan"),
            ("quotes_bijak.txt",      "Data scraping: quotes bijak para filsuf"),
        ]
    },
}

# PROGRAM UTAMA

print("=" * 60)
print("   SIMULASI PERSIAPAN PENYIMPANAN DATA HASIL SCRAPING")
print("=" * 60)

for nama_kategori, data in kategori.items():
    print(f"\n{'─' * 60}")
    print(f"  KATEGORI: {nama_kategori} | Tema: {data['tema']}")
    print(f"{'─' * 60}")

    # Buat folder
    buat_folder(nama_kategori)

    # Buat 5 file di dalam folder tersebut
    for nama_file, isi in data["file"]:
        path_lengkap = os.path.join(nama_kategori, nama_file)
        buat_file(path_lengkap, isi)

    print()  # baris kosong antar kategori

print("\n" + "=" * 60)
print("   SEMUA FOLDER DAN FILE BERHASIL DIPROSES!")
print("=" * 60)