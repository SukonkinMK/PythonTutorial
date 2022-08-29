import math
from posixpath import split
import random
import re

#31 Составить список простых множителей натурального числа N
def multiplierList(n):
    l=[]
    for i in range(2,n+1):
        if not isSimple(i):
            continue
        while  n % i == 0:
            l.append(i)
            n = n / i
        if n == 1:
            break
    return l

def isSimple(n):
    if n == 2:
        return True
    if(n % 2 == 0):
        return False
    for i in range(3, n,2):
        if n%i == 0:
            return False
    return True
print(multiplierList(37))
print()
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности чисел
def task2(l):
    s = set()
    for item in l:
        s.add(item)
    return list(s)
print(task2([1,2,3,4,1,2,4,5,6,7,8,4,67,8,34]))
print(task2([1, 2, 3, 5, 1, 5, 3, 10]))

#33 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
def polynom(k):
    s= ''
    for i in range(0, k+1):
        tmp = random.randint(0, 100)
        if tmp == 0:
            continue
        if len(s) != 0:
            s += ' + '
        s += expressionCreator(tmp,k-i)
    s += ' = 0'
    f = open('file.txt','w')
    f.writelines(s)
    f.close()

def expressionCreator(a,b):
    if b == 0:
        return str(a)
    elif b == 1:
        return f'{a}*x'
    else:
        return f'{a}*x^{b}'

polynom(2)
f = open('file.txt', 'r')
s = f.read()
f.close()
print(s)
#34. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов
def polynoSum(f1,f2):
    s = ''
    f = open('file1.txt', 'r')
    s1 = f.read()
    f.close()
    f = open('file2.txt', 'r')
    s2 = f.read()
    f.close()
    
    pol1 = polynomParser(s1)
    pol2 = polynomParser(s2)
    l1 = list(pol1.keys())
    l2 = list(pol2.keys())
    maxpower = max(max(l1),max(l2))
    for i in range(0, maxpower+1):
        tmp = 0
        if maxpower-i in l1:
            tmp += pol1[maxpower-i]
        if maxpower-i in l2:
            tmp += pol2[maxpower-i]
        if tmp == 0:
            continue
        if len(s) != 0:
            s += ' + '
        s += expressionCreator(tmp,maxpower-i)
    s += ' = 0'
    f = open('file.txt','w')
    f.writelines(s)
    f.close()

def polynomParser(pol):
    result = dict()
    pol = pol.strip(' = 0')
    s = pol.split(' + ')
    for item in s:
        if('*' in item):
            tmp = item.split('*')
            koef = int(tmp[0])
            if('^' in item):
                power = int(tmp[1].split('^')[1])
                result[power] = koef
            else:
                result[1] = koef
        else:
            result[0] = int(item)
    return result

path1 = 'file1.txt'
path2 = 'file2.txt'
path3 = 'file.txt'
f = open(path1, 'r')
print(f'Полином 1: {f.read()}')
f.close()
f = open(path2, 'r')
print(f'Полином 2: {f.read()}')
f.close()
polynoSum('file1.txt','file2.txt')
f = open(path3, 'r')
print(f'Результат: {f.read()}')
f.close()