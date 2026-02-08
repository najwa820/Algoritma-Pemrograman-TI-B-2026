'''
Data types adalah jenis data yang digunakan untuk menentukan 
nilai apa yang disimpan di dalam variabel.
'''

tipe1 = "Hello World!"      # <class 'str'> 
tipe2 = '1'                 # <class 'str'>, walaupun isi variabelnya angka tapi karna menggunakan '' maka dianggap sebagai str
tipe3 = 1                   # <class 'int'>
tipe4 = 1.5                 # <class 'float'>
tipe5 = 3j                  # <class 'complex'>, Bilangan kompleks (j menandakan imajiner)
tipe6 = [1, 3, 4, 5]        # <class 'list'>, nilai didalamnya bisa diubah
tipe7 = ['najwa', 2, 3]     # <class 'list'>
tipe8 = (1, 2, 3.5)         # <class 'tuple'>, nilai didalamnya tidak bisa diubah
tipe9 = range(24)           # <class 'range'>
tipe10 = {                  # <class 'dict'>
    'nama' : 'najwa',       # ('key' : 'key value")
    'kelas' : 'TI B',
    'nim' : 25071101300,
    'mahasiswa aktif' : True
}
tipe11 = {                  # <class 'set'>
    "Jakarta", "Bandung", "Bogor"
}
tipe12 = True               # <class 'bool'>
tipe13 = b"Indonesia"       # <class 'bytes'>
tipe14 = bytearray(3)       # <class 'bytearray>
tipe15 = memoryview(bytes(3))   # <class 'memoryview'>
tipe16 = None               # <class 'NoneType'>

print (type (tipe1))
print (type (tipe2))
print (type (tipe3))
print (type (tipe4))
print (type (tipe5))
print (type (tipe6))
print (type (tipe7))
print (type (tipe8))
print (type (tipe9))
print (type (tipe10))
print (type (tipe11))
print (type (tipe12))
print (type (tipe13))
print (type (tipe14))
print (type (tipe15))
print (type (tipe16))
print ()

print (tipe6 [3])
print (tipe7 [0])
print (tipe8 [1])
print (tipe10 ['nim'])       #kalau mau ngambil indeks