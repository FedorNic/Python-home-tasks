#32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
subs = [1, 3, 5, 4, 9, 14, 5, 1]
alone = []
for i in range (0, len(subs)):
    duplicate = 0
    for j in range(0, len(subs)):
        if i != j:
            if subs[i] == subs[j]:
                duplicate = 1
    if duplicate == 0:
        alone.append(subs[i])
print(alone)