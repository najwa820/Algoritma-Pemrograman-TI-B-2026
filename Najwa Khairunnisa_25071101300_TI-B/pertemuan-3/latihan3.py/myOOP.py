'''
A. INHERITANCE (Pewarisan)
==================================================

1. Buatlah class induk bernama:
Produk
• Memiliki atribut:
nama_produk
harga
• Memiliki method:
info_produk() → Mengembalikan informasi produk

2. Buatlah class turunan:
a. ProdukElektronik
• Tambahan atribut:
garansi (dalam tahun)
• Method info_produk() menampilkan informasi
termasuk lama garansi.
b. ProdukMakanan
• Tambahan atribut:
tanggal_kadaluarsa
• Method info_produk() menampilkan informasi
termasuk tanggal kadaluarsa.

--------------------------------------------------
Contoh Output:
"TV seharga 3.000.000 dengan garansi 2 tahun"
"Roti seharga 15.000 kadaluarsa 12-12-2026"
--------------------------------------------------

==================================================
B. POLYMORPHISM
==================================================

3. Buatlah class:
Notifikasi
• Method:
kirim() → Mengembalikan pesan umum

4. Buat minimal 2 class turunan:
a. Email
• Method kirim() mengembalikan:
"Mengirim notifikasi melalui Email"
b. SMS
• Method kirim() mengembalikan:
"Mengirim notifikasi melalui SMS"

--------------------------------------------------
Catatan:
Method dengan nama yang sama dapat menghasilkan
keluaran yang berbeda tergantung objek yang digunakan.
--------------------------------------------------

==================================================
C. ENCAPSULATION
==================================================

5. Buatlah class:
Mahasiswa
• Atribut private:
__nilai
• Method:
set_nilai(nilai)
get_nilai()
Ketentuan:
• Nilai harus antara 0 - 100
• Jika di luar rentang tersebut,
kembalikan pesan:
"Nilai tidak valid"

--------------------------------------------------

CATATAN:

• Semua class harus berada di dalam file myOOP.py
• Gunakan atribut private dengan tanda (__)
• Method harus menggunakan return, bukan print()
• Buat file terpisah untuk menguji program
'''


#A. INHERITANCE (Pewarisan)
class Produk:
    def __init__ (self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        print("Barang tersedia")

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi
        
    def info_produk(self):
        print(f"{self.nama_produk} seharga {self.harga} dengan garansi {self.garansi} tahun")

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa
        
    def info_produk(self):
        print(f"{self.nama_produk} seharga {self.harga} kadaluarsa {self.tanggal_kadaluarsa}")

#B. POLYMORPHISM
class Notifikasi:
    def __init__ (self, pesan):
        self.pesan = pesan

    def kirim(self):
        print("Notifikasi baru")

class Email(Notifikasi):
    def __init__ (self, pesan):
        super().__init__(pesan)

    def kirim(self):
        print(f"Mengirim notifikasi melalui Email")

class SMS(Notifikasi):
    def __init__ (self, pesan):
        super().__init__(pesan)

    def kirim(self):
        print(f"Mengirim notifikasi melalui SMS")

#C. ENCAPSULATION
class Mahasiswa:
    def __init__(self, nilai):
        self.__nilai = nilai

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            return self.__nilai
        else:
            return "Nilai tidak valid"
        
    def get_nilai(self):
        return self.__nilai