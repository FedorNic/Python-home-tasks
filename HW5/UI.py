from read_push_data import read_data
from add_data import add_data


def operations():
    print('Что делаем: \n1 - получаем информацию об учениках \n2 - добавляем ученика\n3 - выходим из программы\n')
    a = input('Выберите действие: ')
    while True:
        if a == '1':
            print(*read_data())     # Для красоты вывода
            operations()        # Повторный запуск программы, чтобы она не закрывалась каждый раз
        if a == '2':
            add_data()
            operations()
        if a == '3':
            print('Спасибо за сеанс, работа закончена.')
            exit()      # Выход из цикла (завершение программы)