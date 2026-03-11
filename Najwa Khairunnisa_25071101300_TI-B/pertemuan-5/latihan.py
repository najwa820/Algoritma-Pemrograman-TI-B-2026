'''
Diberikan dua matriks:
A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Buatlah program python (tanpa NumPy) yang:
a. Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah
b. Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
c. Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam
C_skalar
d. Menampilkan ketiga hasil dengan format rapi baris per baris
'''

#a.
print("a.")
A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def tambah_matriks(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

c_tambah = tambah_matriks(A, B)
for baris in c_tambah:
    print(baris)

print("\n")

#b.
print("b.")
def kurang_matriks(A, B):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)]
    return hasil

c_kurang = kurang_matriks(A, B)
for baris in c_kurang:
    print(baris)

print("\n")

#c. 
print("c.")
def skalar(A):
    baris, kolom = len(A), len(A[0])
    hasil = [[A[i][j] * 4 for j in range(kolom)] for i in range(baris)]
    return hasil

c_skalar = skalar(A)
for baris in c_skalar:
    print(baris)

#d. opsional aja, jadi ga perlu banget