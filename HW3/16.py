# 16. Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму.

num = int(input('Введите число' + '\n'))
list = [1+(1/i)**i for i in range(1, num+1)]
print(list)
print(sum(list))