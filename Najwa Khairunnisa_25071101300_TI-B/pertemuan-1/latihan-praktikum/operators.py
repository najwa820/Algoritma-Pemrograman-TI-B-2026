'''
Docstring for Pertemuan 1.operators
'''

a = 25
b = 5
print (a + b)
print (a - b)
print (a * b)

x = 15 + 20
y = x + 35
print (x + y)

# Arithmetic Operators
'''
Arithmetic Operators adalah operasi matematika untuk menentukan sebuah nilai

| Operator |            Nama             | Contoh |
|    +     | Penjumlahan                 | x + y  |
|    -     | Pengurangan                 | x - y  |
|    *     | Perkalian                   | x * y  |
|    /     | Pembagian                   | x / y  | 
|    %     | Modulo                      | x % y  |
|    **    | Pangkat (Exponation)        | x ** y |
|    //    | Floor (pembulatan ke bawah) | x // y | 
'''
print (20 + 5)
print (20 - 5)
print (20 * 5)
print (20 / 5)
print (20 % 5)
print (20 ** 5)
print (20 // 6)     # Hasilnya 3.3333 tapi karena menggunakan floor (pembulatan ke bawa) maka hasilnya 3

# Assignment Operators
'''
Digunakan untuk memasukkan nilai ke variabel

| Operator |      Contoh    |          Pengertian         | Sama dengan |
|    =     | x = 5          | Assign (Memberi nilai)      | x = 5       |
|    +=    | x += 3         | Menambahkan nilai variabel  | x = x + 3   |
|    -=    | x -= 3         | Mengurangi nilai variabel   | x = x - 3   |
|    *=    | x *= 3         | Mengalikan nilai variabel   | x = x * 3   |   
|    /=    | x /= 3         | Membagi nilai variabel      | x = x / 3   |
|    %=    | x %= 3         | Modulus (Sisa bagi)         | x = x % 3   |
|    //=   | x //= 3        | Floor (Pembukatan ke bawah) | x = x // 3  |
|    **=   | x **= 3        | Pangkat                     | x = x ** 3  |
|    &=    | x &= 3         | Bitwise AND                 | x = x & 3   |
|    |=    | x |= 3         | Bitwise OR                  | x = x | 3   |
|    ^=    | x ^= 3         | Bitwise XOR                 | x = x ^ 3   |
|    >>=   | x >>= 3        | Bitwise right shift         | x = x >> 3  |
|    <<=   | x <<= 3        | Bitwise left shift          | x = x << 3  |
|    :=    | print(x := 3)  | Walrus operator             | x = 3       |
'''
#1 = -> Memberi nilai
x = 5
print (x)               # Outputnya 5

#2 += -> Menambah Nilai
x = 5
x += 3
print (x)               # Outputnya 8

#3 -= -> Mengurangi nilai
x = 5
x -= 3
print (x)               # Outputnya 2

#4 *= -> Mengalikan nilai
x = 5
x *= 2
print (x)               # Outputnya 10

#5 /= -> Membagi nilai
x = 6
x /= 2
print (x)               # Outputnya 3

#6 %= -> Modulus
x = 7
x %= 3
print (x)               # Outputnya 1

#7 //= -> Floor
x = 7
x //= 3
print (x)               # Outputnya 2

#8 **= -> Pangkat
x = 2
x **= 3
print (x)               # Outputnya 8

#9 &= -> AND Bitwise
x = 5                   # Biner 5 : 0101
x &= 3                  # Biner 3 : 0011 -> 0101 & 0011 = 0001 (kalau keduanya 1 maka hasilnya 1, sisanya 0)
print (x)               # Outputnya 1 karena biner 1 : 0001

#10 |= -> OR Bitwise
x = 5                   # Biner 5 : 0101
x |= 3                  # Biner 3 : 0011 -> 0101 | 0011 = 0111 (kalau salah satunya 1, maka hasilnya 1)
print (x)               # Outputnya 7 karena biner 7 : 0111

#11 ^= -> XOR Bitwise
x = 5                   # Biner 5 : 0101
x ^= 3                  # Biner 3 : 0011 -> 0101 ^ 0011 = 0110 (kalau bit nya berbeda = 1, kalau sama = 0)
print (x)               # Outputnya 6 karena biner 6 : 0110

#12 >>= -> Right shift
x = 8                   # Biner 8 : 1000
x >>= 2                 # Geser 2 bit ke kanan = 0010
print (x)               # Outputnya 2

#13 <<= -> Left shift
x = 2                   # Biner 2 : 0010
x <<= 2                 # Geser 2 bit ke kiri = 1000
print (x)               # Outputnya 8

#14 := -> Walrus operator
'''
Berfungsi untuk menetapkan nilai ke variabel sekaligus melakukan operasi
'''
print (y := 5)          # Outputnya 5
print (y)               # Outputnya 5 

numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print (f'List has {count} elements')

# Comparison Operators
'''
| Operator |        Nama            | Contoh |
|    ==    | Sama dengan            | x == y |
|    !=    | Tidak sama dengan      | x != y |
|    >     | Besar dari             | x > y  |
|    <     | Kecil dari             | x < y  |
|    >=    | Besar sama dengan dari | x >= y |
|    <=    | Kecil sama dengan dari | x <= y |
'''
x = 10
y = 5
print (x == y)      # False
print (x != y)      # True
print (x > y)       # True
print (x < y)       # False
print (x >= y)      # True
print (x <= y)      # False

if 5 != 7:
    print ("True")

#Chaining Comparison Operators
angka1 = 3
angka2 = 5
print (1 < angka1 < 5)                  # True
print (angka1 > angka2 and angka1 > 10) # False

# Logical Operators
'''
| Operator |            Deskripsi            |
|   and    | True apabila keduanya True      |
|   or     | True apabila salah satunya Trus |
|   not    | Negasi                          |
'''
x = 30
print (x < 5 and x > 9)         # False (karena salah satunya (x < 5) False)
print (x > 50 or x > 7)         # True (karena salah satunya sudah True)
print (not (x > 3 and x > 5))   # False (karena lawan dari True adalah False)

# Identity Operators
'''
| Operator |                    Deskripsi                    |
|  is      | True apabila kedua variabel objeknya sama       |
|  is not  | True apabila kedua variabel objeknya tidak sama |
'''
x = ["Mangga", "Jeruk"]
y = ["Pisang", "Jeruk"]
z = x
print (x is z)      # True
print (x is y)      # False (is digunakan untuk mengecek apakah dua variabel menunjuk ke objek yang sama, walaupun isinya sama, tetapi lokasi nya berbeda)
print (x == y)      # False (== digunakan untuk membanadingkan nilai dua variabel. Walaupun vaariabelnya berbeda, nilainya sama, hasilnya true)
print (x is not z)  # False 
print (x is not y)  # True
print (x != y)      # False

# Membership Operators
'''
| Operator |                    Deskripsi                     |         
|  in      | True apabila katanya ada di dalam variabel       |
|  not in  | True apabila katanya tidak ada di dalam variabel |
'''
x = ["Berenang", "Jogging", "Bersepeda"]
print ("Bersepeda" in x)        # True (karena bersepeda ada di dalam variabel)
print ("Mendaki" not in x)      # True (karena Mendaki tidak ada di dalam variabel)

# Operator Precedence
'''
|               Operator            |                       Deskripsi               |
| ()                                | Parenthes (tanda kurung (paling didahulukan)) |
| **                                | Pangkat                                       |
| +x -x ~x                          | Unary Operator                                |
| * / // %                          | Operasi matematika                            |
| + -                               | Tambah kurang                                 |
| << >>                             | Geser bit                                     |
| &                                 | Bitwise AND                                   |
| ^                                 | Bitwise XOR                                   |
| |                                 | Bitwise OR                                    |
| == != > >= < <= is isnot in notin | Comparison, Identity, Membership              |
| not                               | Logika NOT                                    |
| and                               | Logika AND                                    |
| or                                | Logika OR                                     |
'''
x = 5       # Biner : 0101
print (~x)  # Outputnya -6 (~x membalik semua bit (0 jadi 1, 1 jadi 0))

print ((6 - 3) * (3 + 5))
print (100 + 5 * 3)
print (3 + 9 - 8 + 2 - 1)