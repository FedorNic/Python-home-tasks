# 14. Подсчитать сумму цифр в вещественном числе.

def find(a):    # Считаем сумму цифр в числе
    res = 0
    while (a != 0):
        res += a % 10
        a = a // 10
    return res

num = input('Введите число' + '\n')
a = num.split('.')     # убираем точку, переводим в список
sum = list(map(int, a))
print(find(sum[0])+find(sum[0]))