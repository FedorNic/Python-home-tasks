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

list_1 = [1, 2, 3, 6, 38]
for i in list_1:
    if list_1[i]%2==0:
        list_1.remove(i)
print(list_1)
