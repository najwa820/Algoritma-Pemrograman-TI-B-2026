'''
Function adalah blokode yang dijalankan jika dilakukan pemanggilan. 
Di Python function di definisikan menggnakan def.
'''

def good_morning():
    print ("Good morninggg")
good_morning()          # Pemanggilan function

def hallo():
    print ("Haloo semua")
hallo()                 # Pemanggilan function

# Function Names
'''
Function Names adalah case-sensitive (penulisannya harus sama, jika berbeda walaupun hanya satu huruf maka dianggap fungsi berbeda)
'''

# Why Use Function
'''
Function memudahkan membuat program, sehingga tidak perlu menulis kode yang panjang.
Jika ingin di gunakan bisa tinggal dipanggil saja.
'''

# Tidak menggunakan function
alas1 = 5
tinggi1 = 2
luas_segitiga = 0.5 * alas1 * tinggi1
print (luas_segitiga)

alas2 = 10
tinggi2 = 7
luas_segitiga = 0.5 * alas2 * tinggi2
print (luas_segitiga)

alas3 = 90
tinggi3 = 45
luas_segitiga = 0.5 * alas3 * tinggi3
print (luas_segitiga)               # Lebih panjang

# Menggunakan function
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
print (luas_segitiga (5, 2))        # Tinggal melakukan pemanggilan function
print (luas_segitiga (10, 7))       # Lebih singkat
print (luas_segitiga (90, 45))

# Return Values
'''
Function bisa mengembalikan nilai menggunakan return.
'''

def sapaan():
    return "Good Morning"               # Isi function sapaan()
pesan = sapaan()                        # Isi pesan = isi sapaan()
print (pesan)                           # Meskipun pemanggilan nilai pesan, tetapi isinya sama dengan isi sapaan()

# The pass Statement
def sapaan():
    pass            # Melewatkan (karena belum ada yang mau diisi)

# Arguments
def sapaan(nama):
    print (nama + " rajin belajar")    # Digunakan ketika ingin membuat kalimat tetapi isinya tidak berubah
sapaan("Najwa")                        # Outputnya Najwa rajin belajar
sapaan("Uwa")                          # Outputnya Uwa rajin belajar

# Parameter VS Argument
'''
Parameter adalah nilai yang didefinisikan di function, nilainya bisa berubah-ubah
Argument adalah nilai yang mengembalikan ke sebuah function ketika dipanggil.
'''
def panggilan(nama):                # nama adalah parameter
    print ("Good Morning", nama)
panggilan("Najwa")                  # Najwa adalah argument

# Default Parameter Values
def wishlist(negara = "Swedia"):
    print ("Aku akan berkunjung ke", negara)
wishlist("Korea selatan")
wishlist("Jepang")
wishlist()                  # Jika argument nya kosong, maka dia akan mengisi nilai yang didefinisikan di parameter

# Keyword Arguments
def peliharaan (hewan, nama):
    print ("Aku punya seekor", hewan)
    print (hewan + " aku namanya " + nama)
peliharaan ("Kucing", "Muler")
peliharaan ("Kelinci", "Omen")

# Mixing Positional and Keyword Arguments
def peliharaan (hewan, nama, umur):
    print (f"Aku punya seekor, {hewan}")
    print (f"{hewan} aku namanya {nama}")
    print (f"Umurnya {umur} tahun, Dia seekor {hewan} tua.")
peliharaan ("Kucing", "Muler", 3)
peliharaan ("Kelinci", "Omen", 2)

# Passing Different Data Types
def data_pribadi(nama, umur):
    for a in range (len(nama)):
        print (f"Nama: {nama[a]}")
        print (f"Umur: {umur[a]} tahun")
nama = ["Najwa", "Rosidah", "Siti", "Ghina", "Chintya", "Marcel"]
umur = [18, 18, 17, 19, 20, 21]
data_pribadi(nama, umur)

# Positional-Only Arguments VS Keyword-Only Arguments
'''
| Simbol |             Deskripsi          |                                     Artinya                              |
|    /   | Sebelum ini -> positional-only | Argumen wajib diisi berdasarkan posisi, tidak boleh pakai nama parameter |
|    *   | Setelah ini -> keyword-only    | Argumen wajib pakai nama parameter, tidak boleh pakai posisi             |
'''
def sapa (nama, umur, /):
    print (f'Halo semuanya nama aku {nama} umur {umur} tahun.')
sapa ("Najwa Khairunnisa", 18)      # Harus berurut sesuai parameter

def sapa (*, nama, umur):
    print (f'Halo semuanya nama aku {nama} umur {umur} tahun.')
sapa (umur = 18, nama = "Najwa Khairunnisa")    # Boleh tidak berurut tetapi wajib menggunakan nama parameter

# Arbitry Arguments - *args
'''
*args digunakan ketika ingin menampung banyak argumen.
*args bentuknya tuple.
Untuk mengakses nya menggunakan indeks.
contoh: 1, 2, 3
'''
def rata_rata(*nilai):
    total = 0
    rata = 0
    for a in nilai:
        total += a
        rata += 1
        rata_rata = total / rata
    print ("Rata-rata:", rata_rata)
    if rata_rata > 90:
        print ("A")
    elif rata_rata > 80:
        print ("B")
    elif rata_rata > 70:
        print  ("C")
    elif rata_rata > 60:
        print ("D")
    else:
        print ("E")
rata_rata(90, 99, 95, 89, 99, 100, 97) 
rata_rata(98, 78, 85, 99, 69, 78, 89)
rata_rata(90, 25, 12, 33, 25, 30, 40)

# Arbitry keyword Arguments - **kwargs
'''
**kwargs digunakan ketika ingin menampung banyak keyword.
**kwargs bentuknya dictionary
Untuk mengakses nya menggunakan key
contoh: a = 1, b = 2, c = 3
'''
def data_diri(**orang):
    print ("Nama:", orang["nama"])
    print ("Umur:", orang["umur"])
    print ("Data diri:", orang)
data_diri(nama = "Najwa", umur = 18, prodi = "S1 TIB")

# Python Scope
'''
Variabel hanya bisa digunakan di tempat dia di buat.
'''

# Local Scope
def hitung():
    hasil = 10 + 5
    print ("Hasil:", hasil)
hitung()

# Enclosing Scope
def luar():
    angka = 50
    def dalam():
        print ("Angka:", angka)     # menggunakan angka karena fungsi nya masi di dalam fungsi
    dalam()
luar()

total = 0
def tambah():
    total = 10
    print ("Jadi totalnya:", total) # Membaca nilai total didalam fungsi
tambah()
print ("Total 1:", total)           # Membaca nilai total diluar fungsi