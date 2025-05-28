
# 📄 PDF Compressor GUI - Ridho Ismail N (2209466)
# EE-404 KOMUNIKASI DATA

Aplikasi desktop ringan berbasis Python untuk mengompres ukuran file PDF dengan antarmuka grafis yang user-friendly. Proyek ini menggunakan Tkinter dan Ghostscript sebagai backend.

---

## 📌 Deskripsi Singkat

- Proyek ini bertujuan untuk menyediakan solusi lokal dalam mengurangi ukuran file PDF.
- Cocok untuk pengguna yang ingin menghemat ruang penyimpanan tanpa harus menggunakan aplikasi online.
- Dibangun menggunakan Python dan berbagai pustaka pendukung.

---

## 🚀 Fitur Utama

- ✅ Kompresi file PDF secara lokal (tidak butuh internet)
- ✅ Antarmuka grafis sederhana dan intuitif (GUI)
- ✅ Pemilihan file melalui file explorer
- ✅ Menyimpan PDF hasil kompresi dengan nama custom
- ✅ Menampilkan logo Universitas dan informasi pengguna

---

## 🛠️ Teknologi dan Library yang Digunakan

- Python 3.x
- Tkinter (GUI)
- Ghostscript (kompresi PDF)
- Pillow (untuk menampilkan gambar)
- CairoSVG (menampilkan logo SVG)
- PyInstaller (untuk membuat file .exe)

---

## 📦 Langkah Instalasi

1. **Clone repository atau unduh source code**
   ```bash
   git clone https://github.com/nama-kamu/pdf-compressor-gui.git
   ```

2. **Install dependency Python**
   ```bash
   pip install pillow cairosvg
   ```

3. **Install Ghostscript**
   - Unduh Ghostscript: https://www.ghostscript.com/download/gsdnld.html
   - Install dan tambahkan folder `bin` ke Environment PATH, contoh:
     ```
     C:\Program Files\gs\gs10.02.1\bin
     ```

4. **Verifikasi instalasi Ghostscript**
   ```bash
   gswin64c --version
   ```

---

## ▶️ Menjalankan Program

```bash
python app.py
```

---

## 🪄 Konversi Menjadi File .EXE

1. **Install pyinstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Buat file .exe**
   ```bash
   pyinstaller --onefile --windowed app.py
   ```

File .exe akan berada di dalam folder `dist`.

---

## 👨‍🎓 Informasi Pengembang

- **Nama**: Ridho Ismail Nurpalah (2209466)
- **Jurusan**: Teknik Elektro - Universitas Pendidikan Indonesia

---

## 📄 Lisensi

MIT License – Bebas digunakan untuk keperluan pembelajaran dan pengembangan lebih lanjut dengan tetap mencantumkan kredit.

