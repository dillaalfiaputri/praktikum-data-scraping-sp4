@echo off
:: Mengatur direktori kerja ke lokasi file bat ini berada
cd /d "%~dp0"

echo Menjalankan Script Otomasi Scraper STIKOM...
echo.

:: Mengaktifkan virtual environment (pastikan folder venv ada di dalam folder yang sama)
call venv\Scripts\activate

:: Menjalankan file Python
python index.py

echo.
echo ============================================
echo Proses selesai. Jendela ini TIDAK akan tertutup otomatis.
echo Tekan tombol apa saja untuk menutup jendela ini secara manual.
echo ============================================
pause