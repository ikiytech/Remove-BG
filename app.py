import os
from flask import Flask, request, render_template, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi folder tempat menyimpan file yang diproses sementara
# Pastikan folder ini ada atau buat jika belum
os.makedirs('processed_images', exist_ok=True)

@app.route('/')
def index():
    """Merender halaman utama aplikasi."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Menangani unggahan file, menghapus latar belakang menggunakan rembg,
    dan mengirimkan kembali gambar yang sudah diproses.
    """
    # Periksa apakah ada file di dalam request
    if 'file' not in request.files:
        return "Tidak ada bagian file", 400

    file = request.files['file']

    # Jika pengguna tidak memilih file
    if file.filename == '':
        return "Tidak ada file yang dipilih", 400

    # Jika file ada dan valid
    if file:
        try:
            # Baca gambar dari aliran byte yang diunggah
            input_image_bytes = file.read()
            input_image = Image.open(BytesIO(input_image_bytes))

            # Hapus latar belakang dari gambar
            # post_process_mask=True seringkali membantu membersihkan area mask
            output_image = remove(input_image, post_process_mask=True)

            # Siapkan gambar hasil untuk dikirim kembali
            # Simpan gambar ke objek BytesIO sebagai PNG untuk mempertahankan transparansi
            output_image_io = BytesIO()
            output_image.save(output_image_io, format='PNG')
            output_image_io.seek(0) # Kembali ke awal aliran untuk membaca

            # Kirim gambar yang sudah diproses sebagai respons
            return send_file(
                output_image_io,
                mimetype='image/png',
                as_attachment=True, # Ini akan membuat browser mengunduh file
                download_name='gambar_tanpa_latar_belakang.png'
            )
        except Exception as e:
            # Tangani kesalahan yang mungkin terjadi selama pemrosesan gambar
            return f"Terjadi kesalahan saat memproses gambar: {e}", 500
    
    return "Terjadi kesalahan yang tidak diketahui", 500

if __name__ == '__main__':
    # Jalankan aplikasi Flask
    # Pastikan untuk menginstal 'rembg', 'Flask', dan 'Pillow'
    # Gunakan `debug=True` hanya untuk pengembangan. Untuk produksi, gunakan WSGI server (misal Gunicorn).
    app.run(debug=True, port=5000)

