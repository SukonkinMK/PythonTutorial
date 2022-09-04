#программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции
def task1(li):
    result = 0
    for i in range(0,len(li)):
        if(i % 2 != 0):
            result +=li [i]
    return result
#можно доработать так:
def task1_v2(li):
    l = [li[i] for i in range(1,len(li),2)]
    return sum(l)
def task1_v3(li):
    l = [el for i,el in enumerate(li) if i % 2 != 0]
    return sum(l)
print(task1([1,2,3,4,5,6,7]))
print(task1_v2([1,2,3,4,5,6,7]))
print(task1_v3([1,2,3,4,5,6,7]))