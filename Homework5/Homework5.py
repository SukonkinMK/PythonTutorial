import random

#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def CleanWords(string, sample ='абв'):
    s = ''
    parse = string.split()
    mod_parse = list(filter(lambda x: sample not in x, parse))
    for item in mod_parse:
        s += f'{item} '
    return s[:-1]

print(CleanWords('sdasdl sdasac sads. абвыфв фышовадокьта ыфвц ывабв'))

#Игра в конфеты
def StartCandyGame(s = ''):
    N = 100
    p1 = input('Введите имя первого игрока:')
    if s == 'bot':
        p2 = 'Bot'
    else:
        p2 = input('Введите имя второго игрока:')
    currentPlayer = ''
    coin = random.randint(0,1)
    if coin:
        currentPlayer = p1
    else:
        currentPlayer = p2
    print(f'Ходит игрок {currentPlayer}')
    while(N > 0):
        print()
        if N >= 28:
            if currentPlayer != 'Bot':
                n = int(input(f'Текущее кол-во конфет - {N}. Введите, сколько вы берете конфет (от 1 до 28):'))
            else:
                n = random.randint(1,28)
                print(f'{currentPlayer} взял {n} конфет')
        else:
            if currentPlayer != 'Bot':
                n = int(input(f'Текущее кол-во конфет - {N}. Введите, сколько вы берете конфет (от 1 до {N}):'))
            else:
                n = random.randint(1,N)
                print(f'{currentPlayer} взял {n} конфет')
        N -= n
        currentPlayer = ChangePlayer(currentPlayer, p1, p2)
    currentPlayer = ChangePlayer(currentPlayer, p1, p2)
    print(f'Победил {currentPlayer}')

def ChangePlayer(currentPlayer,p1,p2):
    if currentPlayer == p1:
            return p2
    else:
        return p1

if 'YES' == input('Чтобы запустить игру в конфеты, введите YES: '):
    if input('Чтобы сыграть против другого игрока, введите 1, против бота - 0: ') == 1:
        StartCandyGame()
    else:
        StartCandyGame('bot')
print('Игра завершена')

#Крестики нолики
def TickTackToe():
    arr =[['.'] * 3 for i in range(3) ]
    p1 = input('Введите имя первого игрока:')
    p2 = input('Введите имя второго игрока:')
    currentPlayer = ''
    coin = random.randint(0,1)
    if coin:
        currentPlayer = p1
    else:
        currentPlayer = p2
        p1, p2 = p2, p1
    while True:
        print(f'Ходит игрок {currentPlayer}')
        PrintPole(arr)
        while True:
            s = input('Введите, координаты клетки через пробел в формате - строка столбец (строки и столбцы нумеруются с 0)').split()
            x, y = list(map(int,s))
            if arr[x][y] == '.':
                break
            else:
                print('Введите другие координаты')
        if currentPlayer == p1:
            arr[x][y] = 'X'
        else:
            arr[x][y] = 'O'
        if WinCheck(arr):
           break;
        flag = 1
        for i in range(3):
            if not flag:
                break
            for j in range(3):
                if arr[i][j] == '.':
                    flag = 0
                    break
        if flag:
            break;
        currentPlayer = ChangePlayer(currentPlayer, p1, p2)
    PrintPole(arr)
    if flag:
        print('Ничья')
    else:
        print(f'Победил {currentPlayer}')

def WinCheck(arr):
    arrT = [[arr[j][i] for j in range(3)] for i in range(3)]
    #Проход по строкам
    if CheckRows(arr) or CheckRows(arrT):
        return True
    diag1,diag2 = '', ''
    for i in range(3):
        diag1 += arr[i][i]
        diag2 += arr[i][2-i]
    if diag1 == 'XXX' or diag2 == 'XXX' or diag1 == 'OOO' or diag2 == 'OOO':
        return True
    return False

def CheckRows(arr):
    for row in arr:
        if row == ['X'] * 3 or row == ['O'] * 3:
            return True
    return False

def PrintPole(arr):
    for row in arr:
        print(*row)


if 'YES' == input('Чтобы запустить игру крестики-нолики, введите YES: '):
    TickTackToe()
print('Игра завершена')

# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
def Code_RLE(string):
    s = ''
    tmp = ''
    count = 1
    step = 1
    for c in string:
        if (tmp == ''):
            tmp = c
        elif(c == tmp):
            count += 1
            if step == len(string):
                s += f'{count}{tmp}'
        else:
            s += f'{count}{tmp}'
            tmp = c
            count = 1
        step += 1
    return s

def Decode_RLE(string):
    s = ''
    tmp = ''
    for c in string:
        if c.isdigit():
            tmp += c
        else:
            s += c * int(tmp)
            tmp=''
    return s

s1 = Code_RLE('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
print(s1)
print(Decode_RLE(s1))
s2 = Code_RLE('ABCABCABCDDDFFFFFF')
print(s2)
print(Decode_RLE(s2))
