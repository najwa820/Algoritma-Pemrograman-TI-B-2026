'''
Boolean adalah tipe data  yang hanya memiliki dua nilai yaitu True dan False
'''

print (10 > 9)
print (10 == 9)
print (10 < 9)

a = 1234
b = 50
if a > b:
    print ("a lebih besar dari b")
else:
    print ("a tidak lebih besar dari b")

# Most Values are True
print (bool ("Hello"))      # Hasilnya True karna gaada pembandingnya
print (bool (123))
print (bool (["Mangga", "Jeruk", "Apel"]))\

# Some values are False
print (bool (False))
print (bool (None))
print (bool (0))
print (bool (""))
print (bool (()))
print (bool ([]))
print (bool ({}))

# Custom object
class myclass():
  def __len__(self):
    return 0                # panjang = 0 -> dianggap False

myobj = myclass()
print (bool (myobj))        # False

class myclass():
  def __len__(self):
    return 5                # panjang > 0 -> dianggap True

myobj = myclass()
print (bool (myobj))        # True

# Function can Return a Boolean
'''
Di Python sebuah fungsi bisa mengembalikan nilai True atau False
'''
#1 Fungsi selalu Trui
def myFunction():
   return True              # Fungsi ini selalu mengembalikan nilai True
print (myFunction())        # True

#2 Fungsi digunakan dalam if-else
def myFunction():
   return True
if myFunction():            # Mengecek apakah fungsi mengembalikan nilai True
   print("Ya!")
else:
   print("No!")

#3 Fungsi mengembalikan False
def myFunction():
   return False
if myFunction():            # Mengecek apakah fungsi mengembalikan nilai False
   print("Ya!")
else:
   print("No!")

#4 Fungsi built-in yang mengembalikan nilai boolean
x = 250
print (isinstance (x, int)) # True, karena x adalah integer
print (isinstance (x, str)) # False, karena x bukan string