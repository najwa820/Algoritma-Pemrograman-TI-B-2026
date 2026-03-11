# Mengulang terus, menandai dulu, baru mengganti supaya terurut

list = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(list)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if list[j] < list[min_index]:
            min_index = j
    min_value = list.pop(min_index)
    list.insert(i, min_value)

print(list)