'''
Docstring for Pertemuan 1.Latihan 1.for_loops
'''
# Python For Loops
buah = ["apel", "pisang", "jeruk"]
for x in buah:
    print (x)

# Looping Through a string
for x in "najwa":
    print (x)

# The break Statement
buah = ["apel", "pisang", "jeruk"]
for x in buah:
    print (x)           # Loop berhenti setelah cetak pisang
    if x == "pisang":   
        break

for x in buah:
    if x == "pisang":
        break           # Loop berhenti sebelum cetak pisang
    print (x)           # Outputnya apel

# The continue Statement
buah = ["apel", "pisang", "jeruk"]
for x in buah:
    if x == "pisang":
        continue
    print (x)

# The range() Function
for x in range (6):         # Outputnya dari 0-5
    print (x)

for x in range (2, 6):      # Outputnya dari 2-5
    print (x)

for x in range (2, 30, 3):  # Outputnya dari 2-29 dengan jarak tiap output 3
    print (x)

for x in range (10, 0, -2):
    print (x)

# Else in For Loop
for x in range (6):
    print (x)
else:
    print ("Loop berhenti")

for x in range (6):
    if x == 3: break        # Loop berhenti dan lainnya tidak dilanjutkan
    print (x)
else:
    print ("Loop berhenti")

angka = [1, 3, 5, 7]
for x in angka:
    if x % 2 == 0:
        print ("Genap")
        break
else:
    print ("Ganjil")

# Nested Loops
warna = ["merah", "kuning", "hijau"]
buah = ["apel", "pisang", "jeruk"]
for x in warna:
    for y in buah:
        print (x, y)

# The pass Statement
for x in [1, 2, 3]:
    pass

nilai = [60, 75, 90, 45, 88]
for n in nilai:
    if n >= 75:
        print (n, "Lulus")

nilai = [80, 85, 90]
total = 0
for n in nilai:
    total += n
print ("Total nilai:", total)