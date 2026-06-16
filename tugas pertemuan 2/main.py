import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def scraping_kompas_to_file():

    url = "https://www.kompas.com/tag/inet"

    folder = "Scraping_Data"

    # cek folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    # nama file dengan tanggal
    tanggal = datetime.now().strftime("%Y_%m_%d")
    nama_file = f"hasil_{tanggal}.txt"

    path_file = os.path.join(folder, nama_file)

    # request website
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        # ambil semua link berita
        berita = soup.find_all('a')

        hasil = []
        jumlah = 0

        for item in berita:

            judul = item.get_text(strip=True)
            link = item.get('href')

            # filter agar hanya berita valid
            if judul and link and "kompas.com" in link:

                hasil.append(f"Judul : {judul}")
                hasil.append(f"Link   : {link}")
                hasil.append("")

                jumlah += 1

            if jumlah == 10:
                break

        # simpan file
        with open(path_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(hasil))

        print("Berhasil disimpan:")
        print(path_file)

    else:
        print("Gagal mengambil data.")

scraping_kompas_to_file()