x=0
y=0
z=0
f=0

if (not (x or y or z) == (not x and not y and not z)):
        f = True
print(f)

f1, f2, f3, f4, f5, f6, f7, f8 = False, False, False, False, False, False, False, False

f1 = (True, True, False)
f2 = (True, False, True)
f3 = (False, True, True)
f4 = (True, False, False)
f5 = (False, False, True)
f6 = (False, True, True)
f7 = (False, False, False)
f8 = (True, True, True)

if (all([f1, f2, f3, f4, f5, f6, f7, f8])) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')