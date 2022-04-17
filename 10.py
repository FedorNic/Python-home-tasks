# 10. Найти расстояние между двумя точками пространства
from math import sqrt

def find(first, second):
    result = (second - first) * (second - first)
    return result

x1 = int(input('Введите координату X1' + '\n'))
y1 = int(input('Введите координату Y1' + '\n'))
x2 = int(input('Введите координату X2' + '\n'))
y2 = int(input('Введите координату Y2' + '\n'))
sum = sqrt(find(x1, x2) + find(y1, y2))

print(f'Расстояние между точками в 2D пространстве = {round(sum,3)}')