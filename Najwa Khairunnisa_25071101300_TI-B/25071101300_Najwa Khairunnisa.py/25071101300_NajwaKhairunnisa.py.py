'''
Deskripsi Program: Higher or Lower?
Game tebak angka berbasis terminal. Program menyimpan sekumpulan angka dalam sebuah list yang sudah ditentukan. 
Pada setiap ronde, satu angka diambil sebagai angka rahasia. 
Pemain diminta menebak angka tersebut dan akan mendapat petunjuk:
• "Terlalu kecil" — jika tebakan lebih kecil dari angka rahasia
• "Terlalu besar" — jika tebakan lebih besar dari angka rahasia
• "Benar!" — jika tebakan tepat

Skor pemain dihitung berdasarkan sisa percobaan saat berhasil menebak. Seluruh riwayat
permainan disimpan dalam matrix 2D dan ditampilkan sebagai leaderboard di akhir sesi.
Aturan Game (Tanpa Level)
Rentang angka 1 - 100
Maksimal percobaan 7 kali
Skor jika berhasil sisa_percobaan x 10
Skor jika gagal 0 (jika percobaan habis)

Variabel yang Sudah Disediakan
Gunakan variabel berikut yang telah disediakan di dalam program:
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
Angka rahasia diambil berurutan sesuai nomor ronde. Apabila ronde melebihi 10, gunakan operasi modulo:
DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
'''

'''
Bagian A — Fungsi Inti Game (60 poin)
Buat tiga fungsi berikut:
1. tebak_angka(angka_rahasia, maks_percobaan)
Minta input tebakan dari pemain secara berulang menggunakan loop. 
Cetak petunjuk "Terlalu kecil", "Terlalu besar", atau "Benar!" sesuai hasil perbandingan.
Kembalikan True jika pemain berhasil menebak, atau False jika percobaan habis.

2. hitung_skor(berhasil, sisa_percobaan)
Jika pemain berhasil (berhasil = True), kembalikan nilai sisa_percobaan x 10
sebagai skor. Jika tidak berhasil, kembalikan 0.

3. main_satu_ronde(nama, nomor_ronde)
Ambil angka rahasia dari DAFTAR_ANGKA berdasarkan nomor_ronde.
Jalankan tebak_angka() untuk mendapatkan hasil, kemudian panggil
hitung_skor() untuk menghitung skor. Kembalikan list [nama, skor].
'''
# Bagian A
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

def tebak_angka(angka_rahasia, maks_percobaan): #meminta pemain untuk menebak angka
    angka_rahasia = DAFTAR_ANGKA
    list = []
    for i in range (maks_percobaan):
        tebakan = int(input("Tebakan (0-100): "))

        if tebakan < angka_rahasia:
            return "Terlalu Kecil"
        elif tebakan > angka_rahasia:
            return "Terlalu Besar"
        else:
            return "Benar"
    list.append()

def hitung_skor(berhasil, sisa_percobaan): #menghitung skor yang di peroleh oleh pemain
    skor = 0

    if berhasil == True:
        skor += sisa_percobaan * 10
        return skor
    else:
        return 0

def main_satu_ronde(nama, nomor_ronde): #kalau mau main dalam satu ronde
    skor = []
    nomor_ronde = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]

    for i in DAFTAR_ANGKA:
        nama = input("Nama: ")
        nilai = hitung_skor()
        skor.append(nilai)
        nomor_ronde += 1
        return list  

'''
Bagian B — Riwayat Skor dengan Matrix 2D (20 poin)
Buat fungsi berikut:
1. tampilkan_riwayat(riwayat)
Cetak seluruh isi list riwayat dalam format tabel yang memuat kolom nomor,
nama, dan skor. Jika list riwayat kosong, tampilkan pesan: "Belum ada riwayat."
'''
#Bagian B
def tampilkan_riwayat(riwayat): #untuk menampilkan history dari angka apa saja yg udah dipilih pemain
    no = 1
    nama = []
    skor = []
    for nama, skor in main_satu_ronde():
        nama.append()
        skor.append()
    print(f"{no}. {nama} --> {skor}")
    no += 1
    panjang = len(skor)
    data = 0

    for i in range(panjang):
        for j in range(panjang - 1):
            return data[i][j]

'''
Bagian C — Leaderboard dengan Selection Sort (20 poin)
Buat dua fungsi berikut:
1. selection_sort_riwayat(riwayat)
Buat salinan dari list riwayat, lalu urutkan salinan tersebut dari skor tertinggi ke
terendah menggunakan algoritma Selection Sort. Data asli (parameter riwayat)
tidak boleh berubah. Kembalikan salinan yang sudah terurut.
2. tampilkan_leaderboard(riwayat)
Panggil selection_sort_riwayat() untuk mendapatkan data yang terurut, kemudian
cetak hasilnya beserta nomor peringkat. Berikan tanda bintang (*) pada entri
dengan peringkat pertama.
'''

#Bagian C
def selection_sort_riwayat(riwayat): #untuk mengurutkan riwayat 
    data = riwayat.copy()
    panjang = len(data)
    min_indeks = 0

    for i in (panjang):
        max_indeks = i
        for j in (i + 1, panjang):
            if data[j] < data[max_indeks]:
                max_indeks = j
        if i != max_indeks:
            data[j], data[max_indeks] = data[max_indeks], data[j]
            return max_indeks
        
def tampilkan_leadorboard(riwayat): #untuk menampilkan di leadorboard urutan pemenangnya
    data_terurut = selection_sort_riwayat()
    panjang = len(data_terurut)
    max = 0

    for i in range (panjang):
        if max < data_terurut[i]:
            return max
        
    if max:
        return "*"
    
'''
Program Utama
Susun alur program utama sebagai berikut:
1. Minta nama pemain menggunakan input() di awal program.
2. Jalankan main_satu_ronde() untuk memulai satu ronde permainan, lalu simpan
hasilnya ke dalam list riwayat.
3. Setelah setiap ronde selesai, tanyakan kepada pemain apakah ingin bermain lagi.
Gunakan loop while untuk mengulang selama pemain memilih ya.
4. Saat sesi berakhir, panggil tampilkan_riwayat() untuk menampilkan semua ronde
yang telah dimainkan, kemudian panggil tampilkan_leaderboard() untuk
menampilkan peringkat akhir.
'''

print("\n========== PROGRAM UTAMA ==========")
nama = input("Nama: ")
y = True
while y:
    pilihan = input("Apakah Ingin Bermain Lagi (ya/no): ")

    if pilihan == "ya":
        tebak_angka()
    elif pilihan == "no":
        print(tampilkan_riwayat())
    else:
        print("Pilih ya/no")
