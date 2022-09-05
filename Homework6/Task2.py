#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
N = input('Введите вещественное число N: ')
summa = 0
for c in N:
    if c.isdigit():
        summa += int(c)
print(summa)

#Можно доработать так
def task2(s):
    l=list(s)
    li = list(map(int, filter(lambda x: x.isdigit(),l)))
    return sum(li)

print(task2(N))