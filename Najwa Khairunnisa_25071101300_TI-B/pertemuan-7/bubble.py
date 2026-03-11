# Kalau ketemu, dia langsung nge swap

# Contoh 1
print("Contoh 1")
list = [5, 2, 1, 4, 3]

n = len(list)

for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)

#contoh 2
print("\nContoh 2")
list = [1, 2, 3, 4, 5]
n = len(list)
swapped = False

for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            swapped = True
        if not swapped:
            break

print(list)

#contoh 3
print("\nContoh 3")
list = [1, 2, 3, 4, 5, 5, 5]
n = len(list)
i_counter = 0
j_counter = 0
counter = 0
swapped = False

for i in range(n-1):
    i_counter += 1
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            counter += 1
            list[j], list[j+1] = list[j+1], list[j]
            swapped = True
        if not swapped:
            break
print(f'i loop : {i_counter}')
print(f'j loop : {j_counter}')
print(f' : {counter}')
print(list)