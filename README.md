Aplikasi Penghapus Latar Belakang Gambar Sederhana
Aplikasi web sederhana untuk menghapus latar belakang gambar menggunakan Python (Flask) dan JavaScript.
Struktur Proyek
remove-bg-app/
├── app.py                   # Backend Flask untuk memproses gambar
├── requirements.txt         # Daftar pustaka Python yang dibutuhkan
├── templates/               # Folder untuk file HTML
│   └── index.html           # Halaman frontend utama
├── static/                  # Folder untuk aset statis (CSS, JS kustom)
│   └── style.css            # Styling untuk aplikasi
└── README.md                # File ini

Fitur
 * Mengunggah gambar (JPG, PNG, dll.).
 * Secara otomatis menghapus latar belakang gambar menggunakan pustaka rembg.
 * Menampilkan gambar hasil tanpa latar belakang.
 * Tautan untuk mengunduh gambar yang sudah diproses.
Persyaratan
 * Python 3.x
 * pip (Pengelola Paket Python)
Cara Menjalankan (Lokal)
 * Kloning repositori (atau buat folder dan file secara manual):
   Jika ini adalah repositori Git:
   git clone <URL_REPOSITORI_ANDA>
cd remove-bg-app

   Jika Anda membuat file secara manual, pastikan Anda berada di folder remove-bg-app.
 * Buat Virtual Environment (Sangat Direkomendasikan):
   python -m venv venv

   * Untuk macOS/Linux:
     source venv/bin/activate

   * Untuk Windows:
     venv\Scripts\activate

 * Instal Dependensi:
   Pastikan Anda telah mengaktifkan virtual environment, lalu instal pustaka yang dibutuhkan dari requirements.txt:
   pip install -r requirements.txt

 * Jalankan Aplikasi Flask:
   python app.py

 * Buka di Browser:
   Aplikasi akan berjalan di http://127.0.0.1:5000/. Buka URL ini di browser web Anda.
Catatan Penting untuk Deployment
 * GitHub Pages TIDAK bisa menjalankan kode Python (Flask). GitHub Pages hanya untuk hosting file statis (HTML, CSS, JavaScript).
 * Untuk membuat aplikasi ini berfungsi secara publik, Anda perlu deploy bagian backend Python (app.py) ke platform hosting yang mendukung Python, seperti Heroku, Render, PythonAnywhere, atau VPS.
 * Jika Anda deploy backend ke platform lain, Anda perlu mengubah URL di bagian fetch pada index.html dari /upload menjadi URL lengkap endpoint backend Anda (misalnya, https://nama-aplikasi-anda.herokuapp.com/upload).
Teknologi yang Digunakan
 * Backend: Flask (Python)
 * Penghapusan Latar Belakang: rembg (Python)
 * Manipulasi Gambar: Pillow (Python)
 * Frontend: HTML, CSS, JavaScript (Fetch API)
