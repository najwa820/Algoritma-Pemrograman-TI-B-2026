'''
Buatlah sebuah program Python yang berjalan di terminal dengan ketentuan sebagai berikut:

Program meminta pengguna untuk memasukkan jumlah elemen yang akan dimasukkan ke dalam array.
Selanjutnya, pengguna memasukkan sejumlah bilangan bulat non-negatif sesuai jumlah yang telah ditentukan, satu per satu.
Setelah semua elemen dimasukkan, program akan mengurutkan array tersebut menggunakan dua algoritma pengurutan, yaitu Radix Sort dan Merge Sort , secara terpisah.
Program menampilkan hasil pengurutan dari masing-masing algoritma ke layar terminal.

Input yang diterima hanya bilangan bulat non-negatif (≥ 0). Program harus menangani input yang tidak valid.
Implementasikan fungsi terpisah untuk Radix Sort dan Merge Sort.
Tampilkan array sebelum dan sesudah diurutkan untuk setiap algoritma.
'''

print("Radix Sort")
jumlah = int(input("Jumlah elemen: "))
array = []

for i in range (jumlah):
    bilangan = int(input("Bilangan non negatif: "))
    if bilangan < 0:
        print("Masukkan bilangan > 0")
    else:
        array.append(bilangan)

print(f"Sebelum sorting: {array}")

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        radixList = [[],[],[],[],[],[],[],[],[],[]]

    for num in arr:
        radixIndex = (num // exp) % 10
        radixList[radixIndex].append(num)

    for bucket in radixList:
        bubbleSort(bucket)

    i = 0
    for bucket in radixList:
        for num in bucket:
            arr[i] = num
            i += 1

    exp *= 10

radixSortWithBubbleSort(array)
print(f"Setelah sorting: {array}")

print("\nMerge Sort")
jumlah = int(input("Jumlah elemen: "))
array = []

for i in range (jumlah):
    bilangan = int(input("Bilangan non negatif: "))
    if bilangan < 0:
        print("Masukkan bilangan > 0")
    else:
        array.append(bilangan)

print(f"Sebelum sorting: {array}")

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

merge = mergeSort(array)
print(f"Setelah sorting: {merge}")