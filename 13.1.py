# text_1 = input('Введите первую строку' + '\n')
# text_2 = input('Введите вторую строку' + '\n')
# common_letters = set(text_1) & set(text_2)
# print(len(common_letters))

# def text_find(a,b):
#     """
#     Function will find occurence of word in the text
#     """
#     count = 0
#     i = 0
#     while i <= len(a):
#         if b in a[i: i+len(b)]:
#             #print("Найдено повторение номер", count+1)
#             count += 1
#             i += len(b)
#         else:
#             i += 1
#     return count

# a = "a тесты тесты тессс тесты"
# b = "тесты"

# print(f"Count of first word in second phrase: {text_find(a,b)}")
# print(f"Count of first word in second phrase: {text_find('аааааааааа','аа')}")

# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

print('String: ' + str1)
print('Substrings: ' + str2)
print()

for i in substr_list:
    count = 0
    for j in str_list:
        count = str_list.count(i)
    print(f'{i} found {count} times.')
