from tkinter import filedialog, Tk, Button, Entry, Label, Frame, messagebox, PhotoImage
import requests
from io import BytesIO
from PIL import Image, ImageTk
import cairosvg
import subprocess

def ambil_logo_svg_dan_konversi(url_svg):
    try:
        response = requests.get(url_svg)
        response.raise_for_status()
        
        svg_data = response.content
        png_data = cairosvg.svg2png(bytestring=svg_data)
        img = Image.open(BytesIO(png_data))
        img = img.resize((100, 100))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print("Gagal ambil atau konversi logo SVG:", e)
        return None

def cari_ghostscript():
    kemungkinan_path = [
        r"C:\Program Files\gs",
        r"C:\Program Files (x86)\gs"
    ]
    for base_path in kemungkinan_path:
        if os.path.exists(base_path):
            for folder in os.listdir(base_path):
                bin_path = os.path.join(base_path, folder, "bin", "gswin64c.exe")
                if os.path.isfile(bin_path):
                    return bin_path
    return None

def unggah_pdf():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_entry.delete(0, "end")
        pdf_entry.insert(0, file_path)

def kompres_pdf():
    gs_path = cari_ghostscript()
    if not gs_path:
        messagebox.showerror("Ghostscript Tidak Ditemukan", "Ghostscript tidak ditemukan di sistem Anda.\nSilakan instal dari: https://www.ghostscript.com/download/gsdnld.html")
        return

    input_path = file_path
    output_path = os.path.splitext(input_path)[0] + "_compressed.pdf"

    command = [
        gs_path,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]

    try:
        subprocess.run(command, check=True)
        status_label.config(text=f"✔ Berhasil dikompres:\n{os.path.basename(output_path)}", fg="#2e8b57")
    except subprocess.CalledProcessError:
        status_label.config(text="❌ Gagal mengompres PDF.", fg="red")

logo_url_svg = "https://upload.wikimedia.org/wikipedia/id/0/09/Logo_Almamater_UPI.svg"

root = Tk()
root.title("PDF Compressor")
root.geometry("620x350")
root.config(bg="#f0f0f5")

logo = ambil_logo_svg_dan_konversi(logo_url_svg)
if logo:
    logo_label = Label(root, image=logo, bg="#f0f0f5")
    logo_label.pack(pady=(10, 0))

# === Title ===
title_label = Label(root, text="PDF Size Compressor", font=("Helvetica", 18, "bold"), bg="#f0f0f5", fg="#333")
title_label.pack(pady=(10, 2))

# === Identitas ===
nama_label = Label(root, text="Ridho Ismail Nurpalah (2209466)", font=("Arial", 10), bg="#f0f0f5")
nama_label.pack()
jurusan_label = Label(root, text="Teknik Elektro – Universitas Pendidikan Indonesia", font=("Arial", 10), bg="#f0f0f5")
jurusan_label.pack(pady=(0, 10))

# === Frame for File Selection ===
frame = Frame(root, bg="#f0f0f5")
frame.pack(padx=20, pady=5)

pdf_entry = Entry(frame, width=50, font=("Arial", 12))
pdf_entry.grid(row=0, column=0, padx=(0, 10), pady=10)

unggah_button = Button(frame, text="📂 Pilih PDF", command=unggah_pdf, bg="#4da6ff", fg="white",
                       font=("Arial", 10, "bold"), relief="flat", padx=10, pady=5)
unggah_button.grid(row=0, column=1)

# === Compress Button ===
kompres_button = Button(root, text="📦 Kompres PDF", command=kompres_pdf, bg="#28a745", fg="white",
                        font=("Arial", 11, "bold"), relief="flat", padx=20, pady=8)
kompres_button.pack(pady=(10, 10))

# === Status Label ===
status_label = Label(root, text="", bg="#f0f0f5", font=("Arial", 10), wraplength=500, justify="center")
status_label.pack()

root.mainloop()
