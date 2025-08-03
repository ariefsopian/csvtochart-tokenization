📊 Proyek CSV to Chart Tokenization
<div align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python Version">
<img src="https://img.shields.io/badge/Flask-2.x-lightgray" alt="Flask Version">
<img src="https://img.shields.io/badge/Matplotlib-Graph-green" alt="Matplotlib">
</div>

📝 Deskripsi Proyek
Proyek ini adalah aplikasi web sederhana yang dibangun menggunakan framework Python Flask. Aplikasi ini dirancang untuk mempermudah visualisasi data dari file CSV. Pengguna dapat mengunggah file CSV yang berisi data Tokenize dan Detokenize, dan aplikasi akan secara otomatis membuat grafik garis yang interaktif dan informatif.

Fitur utama:

Unggah File CSV: Antarmuka yang mudah digunakan untuk mengunggah file CSV.

Visualisasi Otomatis: Program akan memproses data CSV yang diunggah dan membuat grafik garis.

Penyesuaian Judul: Pengguna dapat memberikan judul khusus untuk setiap grafik yang dihasilkan.

Tampilan Grafik: Grafik yang dihasilkan akan ditampilkan di halaman web baru, siap untuk dilihat dan dianalisis.

🚀 Persyaratan dan Instalasi
1. Prasyarat
Pastikan Anda memiliki Python dan Git terinstal di sistem Anda.

2. Kloning Repositori
Bash

git clone https://github.com/ariefsopian/csvtochart-tokenization.git
cd csvtochart-tokenization
3. Instalasi Dependensi
Proyek ini memerlukan beberapa library Python. Disarankan untuk menggunakan virtual environment (venv) untuk mengelola dependensi.

Bash

# Buat dan aktifkan virtual environment (opsional tapi direkomendasikan)
python -m venv venv
# Untuk Windows:
venv\Scripts\activate
# Untuk macOS/Linux:
source venv/bin/activate

# Instal dependensi yang diperlukan
pip install Flask pandas matplotlib werkzeug
▶️ Cara Menjalankan Aplikasi
Pastikan Anda berada di direktori proyek csvtochart-tokenization.

Jalankan server Flask dengan perintah berikut:

Bash

python app.py
Setelah server berjalan, buka browser web Anda dan kunjungi alamat: http://127.0.0.1:5001.

Aplikasi siap digunakan. Unggah file CSV Anda dan berikan judul untuk melihat grafik yang dihasilkan!