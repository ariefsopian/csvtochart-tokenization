Proyek CSV to Chart Tokenization
Deskripsi Program
Proyek ini adalah aplikasi web sederhana yang dibangun dengan framework Python Flask. Aplikasi ini memungkinkan pengguna untuk mengunggah file CSV yang berisi data "Tokenize" dan "Detokenize". Setelah file diunggah, program akan memproses data tersebut dan membuat grafik garis menggunakan library Matplotlib. Grafik yang dihasilkan kemudian akan ditampilkan di halaman web.

File-file utama dalam proyek ini adalah:

app.py: Kode utama aplikasi web Flask yang menangani unggahan file dan rendering halaman.

plot_chart.py: Skrip Python yang bertanggung jawab untuk membaca file CSV dan membuat grafik.

templates/: Folder yang berisi file-file HTML untuk tampilan antarmuka pengguna.

static/: Folder untuk menyimpan file-file statis seperti gambar grafik yang dihasilkan.

uploads/: Folder untuk menyimpan sementara file CSV yang diunggah oleh pengguna.

Prasyarat
Sebelum menjalankan program, pastikan Anda telah menginstal Python dan Git di sistem Anda.
Program ini membutuhkan beberapa library Python. Anda dapat menginstalnya menggunakan pip:

Flask

Pandas

Matplotlib

Werkzeug

Langkah-langkah Menjalankan Program
Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di komputer lokal Anda:

1. Kloning Repositori
Jika Anda belum mengkloning repositori ini, gunakan Git untuk mengambil semua file dari GitHub:

Bash

git clone https://github.com/ariefsopian/csvtochart-tokenization.git
cd csvtochart-tokenization
2. Instalasi Dependensi
Pastikan Anda berada di direktori proyek, lalu instal semua library yang diperlukan:

Bash

pip install Flask pandas matplotlib werkzeug
(Catatan: Anda mungkin ingin menggunakan lingkungan virtual (venv) untuk mengelola dependensi ini.)

3. Menjalankan Aplikasi
Jalankan file app.py dari terminal Anda:

Bash

python app.py
Anda akan melihat output seperti ini, yang menunjukkan bahwa server sudah berjalan:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
Server akan berjalan secara default di port 5001.

4. Menggunakan Aplikasi
Buka browser web Anda dan navigasi ke alamat berikut: http://127.0.0.1:5001.

Anda akan melihat halaman "Unggah File CSV".

Klik "Choose File" untuk memilih file CSV dari komputer Anda.

Masukkan judul yang Anda inginkan untuk grafik di kolom "Judul Grafik".

Klik tombol "Unggah" untuk mengirim file dan melihat grafik yang dihasilkan.
