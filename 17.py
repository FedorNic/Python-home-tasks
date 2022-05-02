# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
from importlib.resources import path
from random import randint


N = int(input('Введите число' + '\n'))
list = []
for i in range(N):
    list.append(randint(-N, N))
print(list)
path = 'file.txt'
data = open(path,'r')
count = 1
for line in data:
    if int(line) > len(list)-1:
        count*=1
    else:    
        count *= list[int(line)]
print(count)
data.close()