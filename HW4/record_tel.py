def record():
    entry=[]
    surname = input('Введите Фамилию: ')
    entry.append(surname.title())
    name = input('Введите Имя: ')
    entry.append(name.title())
    telephone = input('Введите телефон: ')
    entry.append(telephone)
    disription = input('Введите Описание: ')
    entry.append(disription)
    print('Вами введена запись: ', entry)
    return entry