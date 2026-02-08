'''
Buat sebuah fungsi rekursif bernama jumlah digit(n) yang:
1. Menghitung jumlah seluruh digit dari sebuah bilangan
2. Menggunakan konsep rekursi
Contoh:
Input: 1234
Output: 10
'''

def jumlah_digit(n):
    if (n < 10):
        return n
    else:
        return n % 10 + jumlah_digit(n // 10)

print(jumlah_digit(1234))