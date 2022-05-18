# list1 = [4,2,3,4]
# list2 = [6,7,8,9]

# for i in list1:
#     print(i)

# for i in list2:
#     print(i)

# for i in list1:
#     list1[i] = list2[i]
#     list2[i] = 2

# print(list1)
# print(list2)

# print()

# for i in list1:
#     print(i)

# for i in list2:
#     print(i)

# list_1 = [1, 2, 3, 6, 38]
# for i in list_1:
#     if list_1[i]%2==0:
#         list_1.remove(i)
# print(list_1)

# print(range('a','g'))
# print(23//10)

# from turtle import up


# t = ['red', 'green', 'blue']
# red, green, blue = t
# print(f'{green} {green} {blue} {t[0]} {t[1]} {t[2]}')

# dictionary = {}
# dictionary = \
#     {
#         'up': t[0],
#         'down': t[2]
#     }
# print(dictionary['down'])

# a = list(range(2,101,2))
# print(a)

# print(list(range(2,101,2)))
data = '1 2 3 5 8 15 23 38'.split(' ')
# print(data[0])
# for i in data:
#     data[i] = int(data[i])
list = [int(x) for x in data]
for i in list:
    if list[i]%2==0:
        list.remove(list[i])
print(list)