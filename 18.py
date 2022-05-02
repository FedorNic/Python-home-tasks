# 18. Реализовать алгоритм перемешивания списка.
import random

N = int(input('Введите число элементов списка' + '\n'))
list = []
for i in range(N):
    list.append(random.randint(-N, N))
print(list)
random.shuffle(list)
print(list)