def task1():
    x = int(input('Введите Х: '))
    y = int(input('Введите Y: '))
    if x > 0 and y > 0:
        print(f'Точка ({x},{y}) находится в 1 четверти')
    elif x < 0 and y > 0:
        print(f'Точка ({x},{y}) находится во 2 четверти')
    elif x < 0 and y < 0:
        print(f'Точка ({x},{y}) находится в 3 четверти')
    elif x > 0 and y < 0:
        print(f'Точка ({x},{y}) находится в 4 четверти')
    else:
        if x == 0 and y != 0:
            print(f'Точка ({x},{y}) находится на оси Y')
        elif y == 0 and x != 0:
            print(f'Точка ({x},{y}) находится на оси X')
        else:
            print(f'Точка ({x},{y}) находится в начале координат')
    return

def task2():
    a = int(input('Введите номер четверти: '))
    if a == 1:
        print('Допустимые значения: x > 0 и y > 0')
    elif a == 2:
        print('Допустимые значения: x < 0 и y > 0')
    elif a == 3:
        print('Допустимые значения: x < 0 и y < 0')
    elif a == 4:
        print('Допустимые значения: x > 0 и y < 0')
    return

def task3():
    x1 = int(input('Введите Х1: '))
    y1 = int(input('Введите Y1: '))
    z1 = int(input('Введите Z1: '))
    x2 = int(input('Введите Х2: '))
    y2 = int(input('Введите Y2: '))
    z2 = int(input('Введите Z2: '))
    dist = ((x1- x2) * (x1- x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2)) ** 0.5
    print(f'Расстояние между точками ({x1},{y1},{z1}) и ({x2},{y2},{z2}) равно {dist}')
    return 

while True:
    print('======================================')
    task = int(input('Введите номер задачи (от 1 до 3), для выхода введите 0: '))
    if task  == 0:
        break
    elif task == 1:
        task1()
    elif task == 2:
        task2()
    elif task == 3:
        task3()