text = input('Введите вещественное число' + '\n')
list = text.replace(',','.') # Подстраховка на случай ввода ',' вместо '.'
str_lst= list.split('.') # Разделение полученного списка по точке на несколько индексов
int_lst = [int(x) for x in str_lst] # Функция конвертации строчного списка в целочисленный список на несколько индексов
first = 0
while (int_lst[0] != 0):
    first = first + int_lst[0] % 10
    int_lst[0] = int_lst[0] // 10
# Сумма чисел слева от исходной точки
second = 0
while (int_lst[1] != 0):
    second = second + int_lst[1] % 10
    int_lst[1] = int_lst[1] // 10
# Сумма чисел справа от исходной точки
print(first+second)