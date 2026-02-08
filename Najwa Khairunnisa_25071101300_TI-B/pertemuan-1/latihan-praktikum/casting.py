'''
Casting adalah proses mengubah tipe data satu ke tipe data lain
'''

string = '1'
string_to_numbers = int(string)

print (type (string))
print (type (string_to_numbers))

# Casting ke Integer
x = int (1)         # x = 1
y = int (2.3)       # y = 2 (angka dibelakang koma dihilangkan)
z = int ("3")       # z = 3
print (x, y, z)

# Casting ke Float
x = float (1)       # x = 1.0
y = float (2.3)     # y = 2.3
z = float ("3")     # z = 3.0
w = float ("4.5")   # w = 4.5
print (x, y, z, w)

# Casting ke String
x = str ('1')       # x = '1'
y = str (2)         # y = '2'
z = str (3.0)       # z = '3.0'
print (x, y, z)