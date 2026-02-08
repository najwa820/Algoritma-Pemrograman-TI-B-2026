'''
Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b
2. Mengembalikan hasil penjumlahan a + b
3. Mengembalikan hasil pengurangan a - b
Kemudian:
1. Panggil fungsi tersebut
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
Contoh keluaran:
Penjumlahan = 8
Pengurangan = 2
'''

def hitung (a,b):
    tambah = a + b
    kurang = a - b
    return tambah, kurang       # Mengembalikan nilai
tambah, kurang = hitung (5, 3)
print (f'Penjumlahan = {tambah}')
print (f'Pengurangan = {kurang}')