'''
Buat sebuah fungsi bernama bilangan prima(n) yang:
1. Menggunakan range()
2. Mengembalikan list bilangan prima dari 1 sampai n
Kemudian:
1. Panggil fungsi untuk n = 50
2. Tampilkan hasilnya
'''

def bilangan_prima(n):
    listprima = []
    for x in range (2, n+1):
        prima = True
        for y in range (2, x):
            if x % y == 0:
                prima = False
                break
        if prima:
            listprima.append(x)
    return listprima

print(bilangan_prima(50))