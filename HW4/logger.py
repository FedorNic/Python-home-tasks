from datetime import datetime
import output_style
import csv

def log_to_file(entry):      #Запись в файл
    with open('telephone.csv', 'a') as file:
        file.write(f'{datetime.today()},{entry[0]},{entry[1]},{entry[2]},{entry[3]}\n')
    
def reading_file():     #Чтение всего справочника
    b = output_style.style()
    if b == 1:
        with open('telephone.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(*row, sep='-', end='\n\n')
    if b == 2:
         with open('telephone.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(*row, sep='\n', end='\n\n')