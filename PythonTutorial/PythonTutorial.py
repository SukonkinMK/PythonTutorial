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
