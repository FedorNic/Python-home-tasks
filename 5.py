# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
n = 15
if (n % 5 == 0 and n % 10 == 0) or (n % 15 == 0 and n % 30 != 0):
    print(True)
else:
    print(False)