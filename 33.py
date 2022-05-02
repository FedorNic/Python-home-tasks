# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 2
first = randint(0,101)
second = randint(0,101)
third = randint(0,101)
form = [f'{first}*x^{k} + {second}*x + {third} = 0']
with open('33.txt', 'w') as data:
    data.writelines(form)