import record_tel
import user_interface
import logger

def run():
    temp = user_interface.choice()
    if temp == 1:
        print('Вами выбрана операция внесения в справочник нового контакта')
        entry = record_tel.record() #Запись в справочник
        logger.log_to_file(entry)

    if temp == 2:
        print('Вами выбрана операция вывода на печать всех контактов в справочнике')
        logger.reading_file() 