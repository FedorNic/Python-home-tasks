# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
num = int(input('Введите число' + '\n'))
list = range(num)
print('{', end=' ')
for i in list:
    i += 1
    n = 3*i+1
    print(f'{i}:{n}', end=' ')
print('}')