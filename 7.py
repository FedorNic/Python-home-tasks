# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def logic(x, y, z, f):
    if (not (x or y or z) == (not x and not y and not z)):
        f = True
    print(f)

f1, f2, f3, f4, f5, f6, f7, f8 = False, False, False, False, False, False, False, False
logic(True, True, True, f1)
logic(True, True, False, f2)
logic(True, False, True, f3)
logic(False, True, True, f4)
logic(True, False, False, f5)
logic(False, False, True, f6)
logic(False, True, True, f7)
logic(False, False, False, f8)

if (all([f1, f2, f3, f4, f5, f6, f7, f8])) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')