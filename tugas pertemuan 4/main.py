import pandas as pd
import re

print("Program berjalan...")

def bersihkan_judul(teks):

    teks = teks.strip()

    teks = " ".join(teks.split())

    teks = teks.lower()

    teks = re.sub(r'[^a-zA-Z0-9\s]', '', teks)

    return teks

def format_tanggal(tanggal_text):

    bulan = {
        "Januari": "01",
        "Februari": "02",
        "Maret": "03",
        "April": "04",
        "Mei": "05",
        "Juni": "06",
        "Juli": "07",
        "Agustus": "08",
        "September": "09",
        "Oktober": "10",
        "November": "11",
        "Desember": "12"
    }

    bagian = tanggal_text.split()

    hari = bagian[0].zfill(2)

    nama_bulan = bagian[1]

    tahun = bagian[2]

    bulan_angka = bulan[nama_bulan]

    return f"{tahun}{bulan_angka}{hari}"

raw_data = [

    {
        "Judul": "  Teknologi AI Semakin Canggih!!! ",
        "Waktu_Public": "18 Mei 2026"
    },

    {
        "Judul": "\nHarga Laptop Gaming Turun Drastis\t",
        "Waktu_Public": "10 Juni 2026"
    },

    {
        "Judul": "Diskon Smartphone 50%!!!",
        "Waktu_Public": "01 Januari 2026"
    },

    {
        "Judul": " Berita Ekonomi Hari Ini ",
        "Waktu_Public": "25 Februari 2026"
    },

    {
        "Judul": "Update Teknologi Terbaru@@@",
        "Waktu_Public": "12 Maret 2026"
    },

    {
        "Judul": "Internet Cepat untuk Semua!!!",
        "Waktu_Public": "30 April 2026"
    },

    {
        "Judul": " AI Membantu Dunia Pendidikan ",
        "Waktu_Public": "15 Mei 2026"
    },

    {
        "Judul": "Tutorial Python untuk Pemula###",
        "Waktu_Public": "20 Juni 2026"
    },

    {
        "Judul": " Cloud Computing Modern ",
        "Waktu_Public": "07 Juli 2026"
    },

    {
        "Judul": "Keamanan Data di Era Digital!!!",
        "Waktu_Public": "09 Agustus 2026"
    }

]

hasil_cleaning = []

for data in raw_data:

    judul_asli = data["Judul"]

    waktu_asli = data["Waktu_Public"]

    judul_clean = bersihkan_judul(judul_asli)

    tanggal_clean = format_tanggal(waktu_asli)

    hasil_cleaning.append({

        "Judul_Asli": judul_asli,

        "Judul_Clean": judul_clean,

        "Waktu_Public": waktu_asli,

        "Tanggal_Format": tanggal_clean
    })

df = pd.DataFrame(hasil_cleaning)

print("\nHASIL CLEANSED DATA\n")

print(df)

nama_file = "Hasil_Analisis.xlsx"

df.to_excel(nama_file, index=False)

print(f"\nData berhasil diekspor ke {nama_file}")