# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
try:
    First_Index = list.index("qwe") # Поиск индекса первого совпадения
    Find = list.index("qwe", First_Index+1) # Поиск индекса первого совпадения со следующего индекса за первым совпадением
    print(Find)
except ValueError:
    print(-1)
