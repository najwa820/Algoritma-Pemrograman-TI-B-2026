# memanggil tapi dia harus berurutan
# interprator akan ngecek dari baris awal dulu
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# fungsi loop
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)