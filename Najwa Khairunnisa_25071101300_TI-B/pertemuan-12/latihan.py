struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

print("Tugas A - Hitung Total Ukuran")
def total_ukuran(folder: dict) -> int:
    total = 0
    for key in folder:
        value = folder[key]

        if type(value) == dict:
            total += total_ukuran(value)
        else:
            total += value
    return total

hasil = total_ukuran(struktur)
print(f"Total ukuran skripsi: {hasil} KB")

print("\nTugas B - Hitung Jumlah File")
def hitung_file(folder: dict) -> int:
    jumlah = 0

    for key in folder:
        if type(folder[key]) == dict:
            jumlah += hitung_file(folder[key])
        else:
            jumlah += 1
    return jumlah

print(f"Jumlah file: {hitung_file(struktur)} file")

print("\nTugas C - Cari File Terbesar")
def cari_terbesar(folder: dict) -> tuple:
    namaFile = ""
    ukuran_kb = -1

    for key, value in folder.items():
        if type(value) == dict:
            namafol, ukuranfol = cari_terbesar(value)

            if ukuranfol > ukuran_kb:
                ukuran_kb = ukuranfol
                namaFile = namafol
        else:
            if value > ukuran_kb:
                ukuran_kb = value
                namaFile = key
    return namaFile, ukuran_kb

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

print("\nTugas D - Cetak Struktur Folder")
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indentasi = "  " * level
    print(f"{indentasi}{nama}")

    for key, value in folder.items():
        if type(value) == dict:
            tampilkan_tree(value, key, level + 1)
        else:
            indentasiFile = "  " * (level + 1)
            print(f"{indentasiFile} {key} ({value} KB)")

tampilkan_tree(struktur)