# 11. Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
num = int(input('Введите число' + '\n'))
list = range(num)
for i in list:
    if i % 2 == 0:
        x = 3
    else:
        x = -3
    print(x**i)
