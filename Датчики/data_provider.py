from random import randint

def get_temperature(sensor):    # Получение данных от датчика
    if sensor:
        return randint(-20, 0)
    else:
        return randint(0, 20)

def get_preassure(sensor):      # Получение данных от датчика
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)


def get_wind_speed(sensor):      # Получение данных от датчика
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))