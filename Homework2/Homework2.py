import random

# Task1
N = input('Введите вещественное число N: ')
summa = 0
for c in N:
    if c.isdigit():
        summa += int(c)

print(summa)
# Task2
N = int(input('Введите N: '))
arr = []
res = 1
for i in range (1, N + 1):
    res *= i
    arr.append(res)
print(arr)

# Task3
arr = []
arr = input('Введите элементы списка через пробел: ').split()
print(f'Введенный список {arr}')
for i in range(0,len(arr)):
    tmp = arr[i]
    j = random.randint(i, len(arr) - 1)
    arr[i] = arr[j]
    arr[j] = tmp
print(f'Перемешанный список {arr}')