# import datetime
# from datetime import datetime, timedelta
# # print('=========ТИПЫ ДАННЫХ=========')
# # 1. Напишите программу, которая принимает число и определяет, является ли оно целым, вещественным или строкой.
# print("Task 1 ======================================")
# input_type = input()

# try:
#     num =int(input_type)
#     print("введенное значение является ЦЕЛЫМ ЧИСЛОМ")
# except ValueError:
#     try:
#         num_float = float(input_type)
#         print("введенное значение является ВЕЩЕСТВЕННЫМ ЧИСЛОМ")
#     except ValueError:    
#         print("введенное значение является СТРОКОЙ")

# #2.Напишите программу, которая принимает ввод с клавиатуры и проверяет, является ли введённое значение:
# # Положительным числом.
# # Отрицательным числом.
# # Нулём.
# # Текстом (если преобразование в число невозможно).
# print("Task 2 ======================================")
# input_value = input()
# try:
#     num =int(input_value)
#     if num == 0:
#         print("НОЛЬ")
#     elif num < 0:
#         print("ОТРИЦАТЕЛЬНОЕ ЧИСЛО")
#     else:
#         print("ПОЛОЖИТЛЬНОЕ ЧИСЛО")
# except ValueError:
#     print("введенное значение является СТРОКОЙ")

# #3. Создайте переменную с числом, преобразуйте её в строку, а затем обратно в число. Проверьте их типы.
# print("Task 3 ======================================")
# num = 123
# string = str(num)
# print(type(string))
# again_num = int(string)

# #4. Примите с клавиатуры два числа и выведите их сумму, разность и произведение.
# print("Task 4 ======================================")
# num_1 = int(input())
# num_2 = int(input())

# result_1 = num_1 + num_2
# result_2 = num_1 - num_2
# result_3 = num_1 * num_2
# print(result_1)
# print(result_2)
# print(result_3)

# #5. Преобразуйте строку "123.45" в вещественное число и проверьте, можно ли выполнить математические операции.
# print("Task 5 ======================================")
# string = "123.45"
# float_num = float(string)
# result = float_num + 2.4
# print(result)

# #6. Проверьте, является ли введённое значение булевым (True или False).
# print("Task 6 ======================================")
# input_val = input()
# if input_val == "True" or input_val == "False":
#     print('Булевое значение')
# else:
#     print('НЕ булевое значение')

# print('=========СТРОКИ=========')
# # #1. Напишите программу, которая проверяет, является ли введённая строка палиндромом.
# print("Task 1 ======================================")
# input_str = input()
# new_str = ''.join(reversed(input_str))
# if input_str == new_str:
#     print('строка палиндром')
# else:
#     print('строка НЕ палиндром')

# # Подсчитайте количество вхождений символа "а" в строке.
# print("Task 2 ======================================")
# string = 'My name is Jack and my last name is Nickolas'
# count_of_str = string.count('a')
# print(count_of_str)

# # Разделите строку "яблоко, груша, банан" на список слов.
# print("Task 3 ======================================")
# string = "яблоко, груша, банан"
# list_words = string.split(', ')
# print(list_words)

# # Примите строку, замените в ней все пробелы на символ "-".
# print("Task 4 ======================================")
# string = 'My name is Jack and my last name is Nickolas'
# repl = string.replace(' ', '-')
# print(repl)

# # Найдите самое длинное слово в строке.
# print("Task 5 ======================================")
# text = 'Дан произвольный текст Найдите номер первого самого длинного слова в нем'
# words = text.split()
# max_word = max(words, key=len)
# print(max_word)

# print('=========Коллекции=========')

# # Создайте множество из строки "aabbccddeeff", чтобы удалить дубликаты символов.
# print("Task 1======================================")
# string = "aabbccddeeff"
# sett = set(string)
# print(sett)

# print("Task 2======================================")
# # Найдите пересечение двух множеств: {1, 2, 3, 4} и {3, 4, 5, 6}.
# set1= {1, 2, 3, 4} 
# set2 = {3, 4, 5, 6}
# inser = set.intersection(set1 & set2)
# print(inser)

# print("Task 3======================================")
# # Объедините два множества: {1, 2} и {3, 4}.
# set1= {1, 2} 
# set2 = {3, 4}
# print(set1 | set2)

# # Проверьте, является ли одно множество подмножеством другого: {1, 2} ⊆ {1, 2, 3}.
# print("Task 4======================================")
# set1= {1, 2} 
# set2 = {1, 2, 3}
# print(set1.issubset(set2))

# # Удалите случайный элемент из множества и выведите оставшиеся элементы.
# print("Task 5======================================")
# set2 = {3, 4, 5, 6}
# set2.pop()
# print(set2)

# print('=========Списки, кортежи, словари=========')

# # Примите 5 чисел и сохраните их в список. Выведите их сумму и среднее значение.
# print("Task 1======================================")

# my_list = []
# for i in range(5):
#     num = int(input(f'{i+1}'))
#     my_list.append(num)

# total_sum = sum(my_list)
# averege = total_sum/len(my_list)

# print(total_sum)
# print(averege)

# # Создайте кортеж из 5 слов. Попробуйте заменить одно из слов (объясните, почему это невозможно).
# print("Task 2======================================")
# my_tuple = ("word1", "word2", "word3", "word4", "word5")

# # Составьте словарь с ключами от 1 до 5 и значениями их квадратов.
# print("Task 3======================================")
# my_dict = {}
# for key in range(1,6):
#     value = key**2
#     my_dict[key] = value
# print(my_dict)

# # Найдите максимальное значение в списке и его индекс.
# print("Task 4======================================")
# my_list = [1,22,34,56,109,1111,3,2,6]
# print(max(my_list))
# print(my_list.index(max(my_list)))

# # Сортируйте словарь по значениям.
# print("Task 5======================================")
# my_dict = {4: 16, 1: 1, 2: 4,5: 25, 3: 9}
# #сортировка должна происходить по второму элементу в каждом кортеже
# sorted_num = sorted(my_dict.items(), key = lambda item: item[1])
# print(sorted_num)

# print('=========Срезы=========')

# # Создайте список из чисел от 1 до 10 и выведите только чётные элементы.
# print("Task 1======================================")
# my_list = []
# for num in range(0,10):
#     my_list.append(num+1)
# print(my_list)
# srez = my_list[1::2]
# print(srez)

# # Выведите последние 3 элемента списка [1, 2, 3, 4, 5].
# print("Task 2======================================")
# my_list = [1, 2, 3, 4, 5]
# srez= my_list[-3:]
# print(srez)

# # Разверните строку "hello" с помощью среза.
# print("Task 3======================================")
# string = "hello"
# reverse_str = string[::-1]
# print(reverse_str)

# # Выведите каждый второй элемент списка [10, 20, 30, 40, 50].
# print("Task 4======================================")
# my_list = [10, 20, 30, 40, 50]
# print(my_list[1::2])

# # Скопируйте список через срез и добавьте к нему ещё несколько элементов.
# print("Task 5======================================")
# my_list = [10, 20, 30, 40, 50]
# copy_list = my_list[:]
# copy_list.extend([100, 150, 200])
# print(copy_list)

# print('=========Генераторы=========')

# # Создайте генератор для чисел от 1 до 10, возводя каждое в квадрат.
# print("Task 1======================================")
# a = [1,2,3,4,5]
# b=(i**2 for i in a)#генератор
# print(a)
# print(b)

# for val in b:
#     print(val)

# # Напишите генератор, который возвращает только чётные числа из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# print("Task 2======================================")
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# c = (i for i in a if i%2 == 0)
# for val in c:
#     print(val)
# # Сгенерируйте список строк "Number 1", "Number 2", ..., "Number 5".
# print("Task 3======================================")
# my_list = [f"Number {i}" for i in range(1,6)]
# print(my_list)

# # Создайте генератор, возвращающий бесконечную последовательность чисел (остановите после 10 чисел).
# print("Task 4======================================")
# def generete_list():
#     i=0 
#     while True:
#         yield i
#         i+=1

# gen = generete_list()
# for _  in range(11):
#     print(next(gen))

# print('=========Даты и время=========')

# # Получите текущую дату и время и выведите их.
# print("Task 1======================================")
# today = datetime.date.today()
# print(today)
# print("{}.{}.{}".format(today.day, today.month, today.year))

# # Напишите программу, которая принимает дату и определяет, какой это был день недели.
# print("Task 2======================================")
# input_date = input()
# date = datetime.strptime(input_date, "%d-%m-%Y")
# day_of_week = date.weekday()
# day_of_week_name = date.strftime("%A")
# print(day_of_week_name)

# # Выведите дату следующей недели относительно текущей даты.
# print("Task 3======================================")
# date = datetime.now() + timedelta(days=7)
# print(date)

# # Вычислите разницу в днях между двумя датами.
# print("Task 4======================================")
# date1 = "22-09-2022"
# date2 = "22-12-2022"

# date_format1 = datetime.strptime(date1, "%d-%m-%Y")
# date_format2 = datetime.strptime(date2, "%d-%m-%Y")

# period = date_format2 - date_format1
# print(period)

# # Считайте строку в формате "22-09-2022" и преобразуйте её в объект datetime.
# print("Task 5======================================")
# date_str = "22-09-2022"

# day_of_week = datetime.strptime(date_str, "%d-%m-%Y") 
# print(day_of_week)

print('=========Функции=========')

# Напишите функцию, которая принимает два числа и возвращает их сумму.
print("Task 1======================================")
def sum_nums(num1, num2):
    return num1+ num2
result = sum_nums(11238, 18762)
print(result)

# Создайте функцию, которая проверяет, является ли строка палиндромом.
print("Task 2======================================")
def paliandrom_word(string):
    if string == string[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")

print(paliandrom_word("казак"))
print(paliandrom_word("печаль"))

# Реализуйте функцию, которая принимает список и возвращает его максимальный элемент.
print("Task 3======================================")
def long_word(word_list):
       return max(word_list, key = len)
print(long_word(['asdsfa','dfdg','dfgsrgs','afwFgaergag', 'fwef']))

# Напишите функцию, которая принимает два списка и возвращает список их общих элементов.
print("Task 4======================================")
def common_list(list1, list2):
    join_lists = []
    for i in list1:
        if i in list2:
            join_lists.append(i)
    return join_lists
print(common_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [ 11,234,6, 7, 8, 9,1029]))


print('=========Аргументы=========')

# Напишите функцию, которая принимает произвольное количество чисел и возвращает их сумму.
print("Task 1======================================")
def aum_nums(*nums):
    sum=0
    for num in nums:
        sum +=num
    return sum
print(aum_nums(1,5,66,82,13))
print(aum_nums(66,82))

# Реализуйте функцию, которая принимает два обязательных и один необязательный аргумент.
print("Task 2======================================")
def func(a,b, c=10):
    return a,b,c
print(func(3,6, c=16))

# Напишите функцию, которая принимает словарь с ключами и значениями и выводит их в формате "ключ: значение".
print("Task 3======================================")
def print_key_value(dict1):
    for key, value in dict1.items():
         print(f"{key}: {value}") 
print(print_key_value({'a':1, 'b':2, 'c':3}))

# Создайте функцию, принимающую позиционные и именованные аргументы одновременно.
def greet(name,age):
    print(f"Hello {name}, I know you're {age} old ")
print(greet("Alice",age= 26))


print('=========Распаковка и анонимные функции=========')

# Создайте список и используйте распаковку, чтобы вывести его элементы через запятую.
# Напишите lambda-функцию, которая принимает число и возвращает его квадрат.
# Используйте map и анонимную функцию, чтобы преобразовать список чисел в их квадраты.
# Примените распаковку к словарю, чтобы передать его элементы в функцию.
# Напишите программу, которая принимает список строк и сортирует их по длине с использованием lambda.