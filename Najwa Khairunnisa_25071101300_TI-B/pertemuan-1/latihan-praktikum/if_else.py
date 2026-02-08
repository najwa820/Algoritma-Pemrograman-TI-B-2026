'''
If Else digunakan untuk pemilihan atau pengambilan keputusan.
Program akan menjalankan kode jika kondisi bernilai True.
'''

angka1 = 48
angka2 = 37
angka3 = 69
if angka1 > angka2:
    if angka2 > angka3:
        print (f'{angka2} > {angka3}')
    else:
        print (f'{angka2} < {angka3}')

hari_ini_hari_minggu = True
if hari_ini_hari_minggu:
    print ('aku pergi bermain')

a = 10
b = 20
besar = a if a > b else b
print ("lebih besar", besar)

a = 33
b = 33
print ("A") if a > b else print ("=") if a == b else print ("B") 

hari = "Senin"
if hari == "Minggu":
    print ("Libur")
else:
    print ("Kuliah")

buah = "apel"
if buah in ["apel", "jeruk", "mangga"]:
    print ("Buah tersedia")
else:
    print ("Buah kosong")

# Multiple Elif Statements
nilai = 85
if nilai >= 90:
    print ("Nilai A")
elif nilai >= 80:
    print ("Nilai B")
elif nilai >= 70:
    print ("Nilai C")
else:                       # Digunakan jika tidak ada kemungkinan yang lain
    print ("Tidak lulus")

# Logical Operators
#1 The and operator
a = 3
b = 1
c = 5
if a > b and c > a:
    print ("True")

#2 The  or operator
a = 3
b = 1
c = 5
if a > b or a > c:
    print ("True")

#3 The not operator
a = 3
b = 5
if not a > b:
    print ("a < b")

# Tabel Kebenaran
'''
| Condition 1 | Condition 2 |  and  |   or  |
|     True    |    True     | True  | True  |
|     True    |    False    | False | True  |
|     False   |    True     | False | True  |
|     False   |    False    | False | False |
'''

username = "Najwa"
password = "belajarPython"
aktif = True
role =  "GiaT"

# Versi 1
if username:
    if password:
        if len(password) >= 10:
            if aktif:
                if role == "GiaT":
                    print ("Login berhasil")
                else:
                    print ("Login gagal")
            else:
                print ("Tidak aktif")
        else:
            print ("Password salah")
    else:
        print ("Password wajib diisi")
else:
    print ("Username wajib diisi")

# Versi 2
if not username:
    print ("Username wajib diisi")
elif not password:
    print ("Password wajib diisi")
elif len(password) < 10:
    print ("Password salah")
elif not aktif:
    print ("Tidak aktif")
elif role not in ["GiaT"]:
    print ("Tidak aktif")
else:
    print ("Login berhasil")

# Pass Statements
'''
Pass adalah perintah "Tidak melakukan apa-apa". 
Digunakan supaya kode tidak error meskipun belum ada isi perintahnya.
'''
umur = 17
if umur < 18:
    pass                    # Jika umur < 18 maka aturan untuk anak di bawah umur belum dibuat
else:
    print ("Boleh masuk")   # > 18

nilai = 75
if nilai >= 90:
    print ("Excellent")
elif nilai >= 75:
    pass                    # nilai cukup, sehingga tidak ada pesan yang ditulis
else:
    print ("Must study")

'''
Ringkasan:
- if -> menjalankan program jika kondisi True
- else -> dijalankan jika kondisi False
- elif -> kondisi tambahan
- nested if -> if di dalam if
- ternary -> if satu baris
- pass -> placeholder, tidak melakukan apa-apa
'''