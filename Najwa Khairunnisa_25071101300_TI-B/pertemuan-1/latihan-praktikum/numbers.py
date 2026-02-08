'''
Numbers adalah angka yang bisa digunakan dan dioperasikan
'''

# Int
'''
Int atau Integer adalah bilangan bulat positif dan negatif, dan tidak menggunakan koma/desimal
'''
x = 25
print (type (x))

# Float
'''
Float adalah angka positif atau negatif yang menggunakan koma/desimal
'''
y = 3.0
i = 25E3                # Bilangan float dengan notasi ilmiah 25E3 = 25 x 10**3
print (type (y))
print (type (i))

# Complex
'''
Complex adalah tipe data bilangan kompleks yang terdiri dari bilangan real dan imajiner.
Di python, bagian imajiner ditandai dengan huruf j.
'''
p = 200 + 7j            # 200 adalah bilangan real dan 7j adalah imajiner
print (type (p))

# Type conversion
'''
Type conversation digunakan untuk mengubah type dari int ke float, float ke int, atau int ke complex
'''
x = 5
y = 3.6
z = 2j

a = float (x)            # int ke float
b = int (y)              # float ke int
c = complex (x)          # int ke complex
d = complex (y)          # float ke complex

# Bilangan complex tidak bisa langsung di ubah ke int/float sehingga harus diambil bagian real nya terlebih dahulu
e = int (z.real)         # Ambil bagian real (0)
f = float (z.real)       # Ambil bagian reak (0.0)

# Random number
'''
Python tidak memiliki fungsi random() bawaan untuk membuat random number, tetapi memiliki modul random untuk membuat bilangan acak
'''
import random
print (random.randrange (1, 50))    # Hasilnya berubah-ubah dari 1 sampai 49