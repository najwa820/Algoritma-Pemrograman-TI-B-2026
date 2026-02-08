# karena array menyimpan lebih dari satu, maka alangkah baiknya kita +s
# contoh: names, cars, dll

cars = ["Ford", "Volvo", "BMW"]
print (cars)

cars = ["Ford", "Volvo", "BMW"]
print (cars[2])

# len adalah panjang
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print (x)

# Looping in Arrays
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

# append menambahkan dibagian akhir
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print (cars)

# pop menghilangkan, kalau gaada dibuat indeks nya yg dihilagkan di bagian paling belakang
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print (cars)

# perbedaan remove dan pop, kalau pop merujuk ke indeks, kalau remove menunjuk langsung ke value
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print (x)
# better pakai remove karna kalau punya banyak data bisa langsung aja ke value nya
