'''
Variabel adalah tempat untuk menyimpan data/nilai agar bisa digunakan kembali.
'''
#1) Menggunakan variabel
a = 25          # Dibuat string karena bukan untuk operasi matematika
b = "Maret"
c = 2007        # Dibuat string karena bukan untuk operasi matematika
print (a)
print (b)
print (c)
print (a, b, c)

print ("Saya lahir tanggal", a, b, c)                  
print (f'Saya lahir tanggal {a} {b} {c}')  

#2) Casting
'''
Casting digunakan untuk mengubah tipe data sesuai yang dibutuhkan.
'''
# String ke Integer
a = "25"
b = int (a)
print (b + 5)       # Hasilnya 30

# Integer ke Float
c = 4
d = float (c)
print (d)           # Hasilnya 4.0

# Number ke String
e = 2026
f = str (e)
print ("Sekarang tahun " + f)   

#3) Menentukan Type
angka = 45
objek = "komputer"
print (type (angka))        # <class 'int'>
print (type (objek))        # <class 'str'>
# Lebih lengkap ada di dataTypes.py

#4) Case-sensitive
'''
Python membedakan huruf besar dan kecil dalam penamaan variabel.
'''
umur = 18
Umur = 20
UMUR = 22
print (umur, Umur, UMUR)

#5) Cara penulisan nama variabel yang benar
namalengkap = "Najwa Khairunnisa"
nama_lengkap =  "Najwa Khairunnisa"
_nama_lengkap = "Najwa Khairunnisa"
namaLengkap = "Najwa Khairunnisa"
NamaLengkap = "Najwa Khairunnisa"
NAMALENGKAP = "Najwa Khairunnisa"
namalengkap1 = "Najwa Khairunnisa"

#6) Multiple Variables
x, y, z = "Siti", "Ghina", "Chintya"
print (y)
print (x, y, z)

h = i = j = "friends"
print (h, i, j)

friends = ["Rosidah ", "Marcel ", "Ratna "]
p, q, r = friends
print (p)
print (p, q)
print (p + q + r) 

#7) Global variables
x = "berlari"                   # Variabel global
def myfunc ():                 
    x = "berenang"              # Variabel lokal (hanya berlaku di dalam fungsi)
    print ("fahmi sedang " + x)
myfunc ()
print ("fahmi sedang " + x)     # Tetap memakai variabel global

#8) Global keyword
def myfunc ():
    global x                    # Mengubah variabel global dari dalam fungsi
    x = "memasak"
myfunc ()
print ("fahmi sedang " + x)

x = "belanja"                   # Variabel global
def myfunc ():
    global x                    # Global digunakan agar variabel x yang di dalam fungsi digunakan
    x = "menyapu"               # Mengubah nilai variabel global x
myfunc ()
print ("fahmi sedang " + x)     # Menampilkan nilai terbaru dari variabel x