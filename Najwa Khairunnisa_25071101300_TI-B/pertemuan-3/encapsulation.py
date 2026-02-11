#private properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property dikunci menggunakan __

p1 = Person("Emil", 25)
print(p1.name)


#untuk mengambil private properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  

  def getAge(self): #untuk mengakses properties yang di private menggunakan get
    print("age :", self.__age)

p1 = Person("Emil", 25)
print(p1.name)
print(p1.getAge())


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())


#menggunakan enkapsulasi
#dengan menggunakan enkalpsulasi akan mendapatkan manfaat perlindungan data, validasi, fleksibilitas, kontrol
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5)  # This would cause an error


#Name Mainling
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!