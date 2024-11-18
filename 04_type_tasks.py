# #1. Классическая задача с собеседования
# #дублирвоание занчений 3 раза
# a = [[]] * 3
# print(a)

# #меням последний элемент вывод [[3], [3], [3]] - так происходит потому что мы копируем ссылки на влоденные список
# a[2].append(3)
# print(a)

# #2. Преобразование числа к строке
# n = 1
# n_str = str(n)
# print(n_str)

#3. Экранирование строк
print("Hey, this code here \"Some code\"")
        #Новая строка
print('''Hey, this code here: \n- Some code''')
        #Backspace
print('Hey, this code here: \bSome code')
        #Backspace
print('\u00A9')
