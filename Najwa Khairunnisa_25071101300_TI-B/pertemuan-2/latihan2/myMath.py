# 1. Penambahan (a, b)
def tambah (a, b):
    return a + b
print (tambah)

# 2. Pengurangan (a, b)
def kurang (a,b):
    return a - b

# 3. Pekalian (a, b)
def kali (a, b):
    return a * b

# 4. Pembagian (a, b)
def bagi (a, b):
    return a / b

# 5. Modulus (a, b)
def modulus (a, b):
    return a % b

# 6. fibonacci (n)
def fibonacci (n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)