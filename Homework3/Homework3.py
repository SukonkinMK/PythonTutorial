#программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции
def task1(li):
    result = 0
    for i in range(0,len(li)):
        if(i % 2 != 0):
            result +=li [i]
    return result

#программf, которая находит произведение пар чисел списка первого с последним и т.д.
def task2(li):
    resultList = []
    for i in range(0,(len(li) + 1) // 2):
        resultList.append(li[i]*li[-i-1])
    return resultList

#программа, которая найдёт разницу между максимальным и минимальным значением дробной части элементов списка
def task3(li):
    ans = 0
    min_fraction = 0
    max_fraction = 0
    for item in li:
        tmp = abs(item) - abs(int(item))
        if(tmp != 0):
            if(min_fraction > tmp or min_fraction == 0):
                min_fraction = tmp
            if(max_fraction < tmp or max_fraction == 0):
                max_fraction = tmp
    return round(max_fraction - min_fraction,6)

#программа, которая будет преобразовывать десятичное число в двоичное.
def task4(n):
    result = 0;
    step = 0
    while(n != 0):
        tmp = n % 2
        result = result + tmp * (10 ** step)
        n //= 2
        step +=1
    return result
#программа, которая будет возвращать список чисел Фибоначчи от [-n,n].
def task5(n):
    li = []
    for i in range(-n, n + 1):
        li.append(fibonacci(i))
    return li

def fibonacci(n):
    if n == -2:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n < 0:
            return fibonacci(n + 2) - fibonacci(n + 1)
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

#тесты задачи 1
print(task1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(task1([2, 3, 5, 9, 3]))
print()

#тесты задачи 2
print(task2([2, 3, 4, 5, 6]))
print(task2([2, 3, 5, 6]))
print()

#тесты задачи 3
print(task3([1.1, 1.2, 3.1, 5, 10.01]))
print()


#тесты задачи 4
print(task4(45))
print(task4(3))
print(task4(2))
print(task4(11))
print()

#тесты задачи 5
print(task5(8))