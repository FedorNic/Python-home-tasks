# 0. Вывести квадрат числа
# a = int(input('Введите число \n'))
# print(f'Квадрат числа {a} равен {a**2}')

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
q=63000
x = [31, 42, 51, 61, 76]
y = [19240, 25000, 30500, 55555, 65000]
f = interpolate.interp1d(x, y, fill_value="extrapolate")
# x1 = np.arange(6, 12)
# y1 = f(x1)   # использовать функцию интерполяции, возвращаемую `interp1d`

plt.plot(x, y, 'o', x, y, '--')
plt.show()

