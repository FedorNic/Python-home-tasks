# 34. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from importlib.resources import path

path = '34_1.txt'
data = open(path,'r')
for line in data:
    first = line
data.close
# print(first)

path = '34_2.txt'
data = open(path,'r')
for line in data:
    second = line
data.close
# print(second)

Sum = f'({first})+({second})'
# print(Sum)

with open('34_3.txt', 'w') as data:
    data.writelines(Sum)