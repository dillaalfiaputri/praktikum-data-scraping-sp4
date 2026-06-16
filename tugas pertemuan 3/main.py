import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import os

def scraping_detik_to_database():

    # URL target
    url = "https://inet.detik.com/"

    # Header browser
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Konfigurasi database
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "db_scraping"
    }

    # Folder log
    folder_log = "Scraping_Log"

    # Cek folder
    if not os.path.exists(folder_log):
        os.makedirs(folder_log)

    # File log
    log_file = os.path.join(folder_log, "log_db.txt")

    conn = None

    try:

        # Koneksi database
        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()

        print("Terhubung ke database")

        # Request website
        response = requests.get(url, headers=headers)

        # Validasi website
        if response.status_code == 200:

            # Parsing HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Ambil semua link
            semua_link = soup.find_all('a')

            berita_unik = []

            # Filter link berita detik
            for item in semua_link:

                link = item.get('href')

                if link:

                    if "detik.com" in link and "/d-" in link:

                        if link not in berita_unik:

                            berita_unik.append(link)

                # Ambil 20 berita
                if len(berita_unik) == 20:
                    break

            # Jika tidak ada berita
            if not berita_unik:

                print("Berita tidak ditemukan")

            else:

                print(f"Ditemukan {len(berita_unik)} berita")

                jumlah_insert = 0

                waktu_scraping = datetime.now()

                # Proses detail berita
                for link in berita_unik:

                    try:

                        # Request detail berita
                        detail = requests.get(
                            link,
                            headers=headers
                        )

                        detail_soup = BeautifulSoup(
                            detail.text,
                            'html.parser'
                        )

                        # Ambil judul
                        title_tag = detail_soup.find('title')

                        if title_tag:
                            judul = title_tag.text.strip()
                        else:
                            judul = "Tidak ada judul"

                        # Ambil gambar
                        img_tag = detail_soup.find('img')

                        if img_tag:
                            url_gambar = img_tag.get('src')
                        else:
                            url_gambar = None

                        # Ambil isi berita
                        paragraf = detail_soup.find_all('p')

                        isi_list = []

                        for p in paragraf[:10]:

                            teks = p.get_text(strip=True)

                            if teks:
                                isi_list.append(teks)

                        isi_berita = " ".join(isi_list)

                        # Jika data belum ada
                        if True:

                            sql = """
                            INSERT INTO tbl_berita
                            (
                                judul,
                                url_link,
                                url_gambar,
                                isi_berita,
                                tanggal_scraping
                            )
                            VALUES (%s, %s, %s, %s, %s)
                            """

                            val = (
                                judul,
                                link,
                                url_gambar,
                                isi_berita,
                                waktu_scraping
                            )

                            cursor.execute(sql, val)

                            jumlah_insert += 1

                            print("\n========================")
                            print("Judul          :", judul)
                            print("URL Link       :", link)
                            print("URL Gambar     :", url_gambar)
                            print("Tanggal        :", waktu_scraping)
                            print("Isi Berita     :", isi_berita[:200])
                            print("========================")

                            # Simpan log
                            with open(
                                log_file,
                                'a',
                                encoding='utf-8'
                            ) as log:

                                log.write(
                                    f"Berhasil simpan: {judul}\n"
                                )

                            print(
                                f"Berhasil simpan: {judul}"
                            )

                        else:

                            print(
                                f"Duplicate: {judul}"
                            )

                    except Exception as e:

                        print(
                            f"Gagal mengambil detail berita: {e}"
                        )

                # Simpan database
                conn.commit()

                print(
                    f"\nBerhasil menyimpan "
                    f"{jumlah_insert} data berita"
                )

        else:

            print(
                f"Gagal mengambil website "
                f"(Status: {response.status_code})"
            )

    # Error database
    except mysql.connector.Error as err:

        print(f"Error Database: {err}")

    # Error umum
    except Exception as e:

        print(f"Error: {e}")

    finally:

        # Tutup koneksi
        if conn and conn.is_connected():

            cursor.close()

            conn.close()

            print("Koneksi database ditutup")

# Jalankan program
scraping_detik_to_database()