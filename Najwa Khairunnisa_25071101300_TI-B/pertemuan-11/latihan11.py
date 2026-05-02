'''
Buatlah sebuah program yang mengimplementasikan Linear dan Binary Search.
Dengan catatan data nya adalah : data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9].
Tampilkan data dan minta pengguna untuk memasukkan nilai berapa yang dicari, jika ketemu maka tampilkan index nya, jika tidak maka return -1.
Buatlah dalam 1 file saja
'''

print("Linear Search")
def linearSearch(data, cari):
    for i in range(len(data)):
        if data[i] == cari:
            return i
    return -1

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print(data)
cari = int(input("Masukkan angka yang ingin dicari: "))

indeks = linearSearch(data, cari)

if indeks != -1:
    print(f"Ada di indeks ke-{indeks}")
else:
    print("Tidak ditemukan")

print("\n")

print("Binary Search")
def binarySearch(data, cari):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == cari:
            return mid
        
        if data[mid] < cari:
            left = mid + 1
        else:
            right = mid - 1

    return -1

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
print(data)
data.sort()
print(f"Data setelah terurut: {data}")
cari = int(input("Masukkan angka yang ingin dicari: "))

indeks = binarySearch(data, cari)

if indeks != -1:
    print(f"Ada di indeks ke-{indeks}")
else:
    print("Tidak ditemukan")