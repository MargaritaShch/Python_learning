#1. type
print("Task 1 ======================================")
#list
a = [1,2,3]
print(type(a))
#tuple
a = (1,2,3)
print(type(a))
#set
a = {1,2,3}
print(type(a))
#frozenest
b = frozenset([1,2,3])
print(type(b))
#dict
c = {1: 'a', 2: 'b', 3:'c'}
print(type(c))

#2. change type 
print("Task 2 ======================================")
my_tuple = ('a', 'b', 'a')

my_list = list(my_tuple)
my_set = set(my_tuple)
my_frozenest = frozenset(my_tuple)

print(my_list, my_frozenest,my_set)

#3. find index in list 
print("Task 3 ======================================")
my_list = ['a','b','c','d','e','f']
print(my_list[0])
print(my_list[3])
print(my_list[-1])
#list in list
my_list_2lv = [[1,2,3],['a','b','c','d','e','f']]
print(my_list_2lv[0])
print(my_list_2lv[0][2])
#change element in list
my_list = ['a','b','c','d','e','f', [2,5]]
my_list[0] =10
my_list[-1][0] = "str"
print(my_list)

#4. add and delete elem in list 
print("Task 4 ======================================")
my_list = ['a','b','c','d','e','f']
my_list.append(41)
print(my_list)
my_list.remove('a')
print(my_list)
my_list.pop(4)
print(my_list)
#add elem in list from another list
my_list = [1, 2, 3]
another_list = ['a','b','c']
my_list.extend(another_list)
print(my_list)
#join two lists without change list
#analog extend
a = [1, 2, 3]
b = [4,5]
c=  a+b
print(a,b,c)
#analog append
a = [1, 2, 3]
b = [4,5]
c=  a+ [b]
print(a,b,c)
#work with version > 3.5
a,b = [1, 2, 3],[4,5]
c = [*a,*b]
print(c)

#5. tuple and string
print("Task 5 ======================================")
my_tuple = (1,2,3,4,5,6)
my_string = 'kjkguyfu'

print(my_tuple[2])
print(my_string[-1])

print(sorted(my_tuple))
print(sorted(my_string))
#join string
my_string1 = 'kkhjkj'
my_string2='Hi'

print(my_string1+my_string2)
#join tuple
my_tuple1= (1,2,3)
my_tuple2 = (4,5,6)

print(my_tuple1+my_tuple2)

#6. set and dictionary
print("Task 6 ======================================")
my_set = set()
my_set = {1,2,3,4}
#with dictionary
my_hetero_set = {'abc', 3.14, (10,20)}

my_dict = {}
print(my_dict)
my_dict1 = {'one':1, 'two':2}
print(my_dict1)

#cycles
#keys
my_dict2 = {'one':1, 'two':2,'three':3}
for elem in my_dict2:
    print(elem)
#values
for elem in my_dict2.values():
    print(elem)
#keys and values
for ekey, value in my_dict2.items():
    print(ekey, value)
#join dictionaries
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 't':5, 'f':6}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
#доступ к занчениям словаря
print(dict1.get('a'))
print(dict1.get('fd', 'sfs'))

#6. Срезы
print("Task 7 ======================================")
my_list = ['a','b','c','d','e','f']
my_list[1:2] = [2]
print(my_list)

#замена двух элементов на один
my_list[1:3] = [0]
print(my_list)
#замена двух элементов на три
my_list[:2] = [100,200,300]
print(my_list)

#8. slice
print("Task 8 ======================================")
my_list = ['a','b','c','d','e','f']
my_slice = slice(2,4)
print(my_slice.start)
print(my_slice.stop)
print(my_slice.step)
print(my_list[my_slice])

# #9. Task 9
# print("Task 9 ======================================")
# С клавиатуры подается 5 чисел, разделенных концом строки. Нужно вывести их на экран от большего к меньшему, также разделяя их концом строки.
# Формат ввода
# 12
# 1
# 45
# 9
# 10

# Формат вывода
# 45
# 12
# 10
# 9
# 1
nums = []  
for _ in range(5):  
    nums.append(int(input()))  

nums_sort = sorted(nums, reverse=True)

for num in nums_sort:
    print(num)

#10. Task 10
print("Task 10 ======================================")
# Коллекции. Множества
# С клавиатуры вводится строка, содержащая произвольное количество слов через запятую и пробел. Слова могут повторяться. Нужно вывести на экран все слова в алфавитном порядке по одному разу, также через пробел и запятую.
# Формат ввода
# джек, воробей, капитан, джек, воробей
# Формат вывода
# воробей, джек, капитан
# Примечания
# Обратите внимание, что в примере у первого слова "воробей" стоит запятая, а у второго - нет. В решении такие случае следует учесть. Кроме того, слова могут быть написаны в разном регистре. Вывести их нужно в нижнем регистре. Одинаковые слова, написанные в разных регистрах, считаем одинаковыми.
input_words = input().lower().split(', ')
unic = set(input_words)
sorted_word = sorted(unic)
print(', '.join(sorted_word))

#11. Task 11
print("Task 11 ======================================")
# Коллекции. Пересечение списков
# Напишите программу, которая принимает на вход две строки, каждая из которых представляет собой список целых чисел, разделенных пробелами. Программа должна вывести список общих элементов этих списков в порядке возрастания. Если общих элементов нет, программа должна вывести сообщение: "Общих элементов нет".
# Формат ввода
# 1 2 3 4 5
# 3 5 7 9 11
# Формат вывода
# Общие элементы: 3 5
str_1 = input()
str_2 = input()

set1 = set(map(int, str_1.split()))
set2 = set(map(int, str_2.split()))

insr = set1 & set2

if insr:
    print("Общие элементы:", ' '.join(map(str, sorted(insr))))
else:
    print("Общих элементов нет")

#12. Task 12
print("Task 12 ======================================")
# Коллекции. Словари
# С клавиатуры вводятся слова через запятую с пробелом. Выведите на экран три наиболее часто встречаемых слова, вместе с количеством этих слов. Количество должно быть отделено от слова двоеточием и пробелом. Каждая пара слово-количество должна быть выведена на отдельной строчке. Для простоты гарантируется, что в строке нет слов с одинаковой встречаемостью.

# Формат ввода
# три, три, и, ещё, три, будет, дырка, и, будет, и, дырка, и, дырка, и, дырка

# Формат вывода
# и: 5
# дырка: 4
# три: 3

# Примечания
# Рекомендация: чтобы быстрее решить задачу, нужно составить словарь, в котором ключами будут встреченные слова, а значениями - их количество в строке. Далее работайте с этим словарем по своему усмотрению. Далее один из вариантов - отсортировать кортежи, в которых на первом месте стоит количество слов, а на втором - сами слова.Учтите, что различных слов в строке может быть меньше трех. В этом случае нужно вывести все.
input_words = input().lower().split(', ')
count ={}
for word in input_words:
    if word in count:
        count[word] +=1
    else:
        count[word] = 1

sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word, freq in sorted_words[:3]:
    print(f"{word}: {freq}")

#13. Task 13
print("Task 13 ======================================")
# Коллекции. Корзина покупок
# Программа должна принимать с клавиатуры данные о товарах, которые добавляются в корзину, а затем выводить чек с суммой покупок. Каждый товар записывается в виде строки:

# [название товара]: [цена товара]

# Ввод заканчивается строкой "конец".

# Чек должен отображать список покупок в том же порядке, в котором они были введены. Если введен повторяющийся товар, он должен быть добавлен к уже имеющемуся в чеке, с суммированием цены и увеличением количества штук. Вид чека приведен в примере (количество и расположение выведенных "-" должно совпадать).

# Структура чека:

# Чек:
# ---------------------
# [название товара 1]: [цена 1] ([количество 1] шт.)
# [название товара 2]: [цена 2] ([количество 2] шт.)
# ...
# ---------------------
# Итого: [сумма покупок]
 
# Формат ввода
# Яблоко: 100
# Хлеб: 50
# Яблоко: 100
# Молоко: 80
# конец
 

# Формат вывода
# Чек:
# ---------------------
# Яблоко: 200 (2 шт.)
# Хлеб: 50 (1 шт.)
# Молоко: 80 (1 шт.)
# ---------------------
# Итого: 330
 

# Примечания
# Если вы знакомы с синтаксисом самых новых версий питона, то вам может захотеться использовать в коде моржовый оператор :=. В нашей проверяющей системе более древний питон, поэтому ничего у вас не выйдет, страдайте и используйте старый синтаксис.
cart = {}
while True:
    input_products = input()
    if input_products.lower() ==  "конец":
        break

    try:
        name, price = input_products.split(": ")
        price = int(price)

        if name in cart:
            cart[name]["total_price"] +=price
            cart[name]["quantity"] +=1
        else:
            cart[name] = {"total_price": price, "quantity": 1}

    except ValueError:
        print("Некорректный формат ввода. Используйте формат: Название: Цена.")

print("Чек:")
print("---------------------")

total_sum =0
for name, details in cart.items():
    print(f"{name}: {details['total_price']} ({details['quantity']} шт.)")
    total_sum += details["total_price"]
print("---------------------")
print(f'Итого: {total_sum}')

#13. Task 13
print("Task 13 ======================================")
# Коллекции. Группировка товаров
# На вход подаются строки, представляющие собой информацию о товарах. Необходимо сгруппировать товары по категориям и вывести их в требуемом формате, отсортировав сначала категории по алфавиту, а затем товары внутри каждой категории по цене в порядке возрастания. Строки вводятся до тех пор, пока не встретится слово "стоп".
 
# Условия:

# Каждая строка содержит информацию о товаре в формате: Название товара - Категория - Цена.
# Гарантируется, что названия товаров не повторяются.
# В случае, если у товаров внутри одной категории одинаковая цена, их нужно сортировать по алфавиту.
# Структура вывода:

# Категория:
#   - Товар1 (Цена1)
#   - Товар2 (Цена2)
#   ...
 

# Формат ввода
# Телефон - Электроника - 50000
# Ноутбук - Электроника - 100000
# Кофе - Продукты - 300
# Чай - Продукты - 120
# Кроссовки - Одежда - 9000
# стоп
 

# Формат вывода
# Одежда:
#   - Кроссовки (9000 руб.)
# Продукты:
#   - Чай (120 руб.)
#   - Кофе (300 руб.)
# Электроника:
#   - Телефон (50000 руб.)
#   - Ноутбук (100000 руб.)

cart = {}
while True:
    input_products = input()
    if input_products.lower() ==  "стоп":
        break

    try:
        name, category, price = input_products.split(" - ")
        price = int(price)

        if category not in cart:
            cart[category] = []
        cart[category].append((name,price))
    except ValueError:
        print("Некорректный формат ввода.")

sorted_category = sorted(cart.keys())

for  category in sorted_category:
    print(f'{category}:')
    sorted_items = sorted(cart[category], key = lambda item: (item[1], item[0]))
    for name, price in sorted_items:
        print(f"  - {name} ({price} руб.)")

#14. Task 14
print("Task 14 ======================================")
# Коллекции. Расширенная группировка товаров
# На вход подаются строки, представляющие собой информацию о товарах. Необходимо сгруппировать товары по категориям, подкатегориям и вывести их в требуемом формате, отсортировав товары внутри каждой подкатегории по цене в порядке возрастания, категории и подкатегории в каждой категории по алфавиту. Строки вводятся до тех пор, пока не встретится слово "стоп".
 

# Условия:

# Каждая строка содержит информацию о товаре в формате: Категория - Подкатегория - Название товара - Цена.
# Гарантируется, что названия товаров не повторяются и что будет введено хотя бы одно значение товара.
# Структура вывода:

# Категория:
#   Подкатегория1:
#     - Название товара1 (Цена1 руб.)
#     - Название товара2 (Цена2 руб.)
#     ...
#   Подкатегория2:
#     - Название товара1 (Цена1 руб.)
#     - Название товара2 (Цена2 руб.)
#     ...
 
# Формат ввода
# Электроника - Телефон - Samsung Galaxy S23 - 50000
# Электроника - Ноутбук - Lenovo IdeaPad 3 - 40000
# Электроника - Телефон - iPhone 14 Pro Max - 80000
# Продукты - Чай - Lipton зеленый - 120
# Продукты - Кофе - Lavazza Crema e Aroma - 300
# Одежда - Кроссовки - Adidas Ultraboost 23 - 12000
# стоп
 

# Формат вывода
# Одежда:
#   Кроссовки:
#     - Adidas Ultraboost 23 (12000 руб.)
# Продукты:
#   Кофе:
#     - Lavazza Crema e Aroma (300 руб.)
#   Чай:
#     - Lipton зеленый (120 руб.)
# Электроника:
#   Ноутбук:
#     - Lenovo IdeaPad 3 (40000 руб.)
#   Телефон:
#     - Samsung Galaxy S23 (50000 руб.)
#     - iPhone 14 Pro Max (80000 руб.)

cart = {}
while True:
    input_products = input()
    if input_products.lower() ==  "стоп":
        break
    try:
        category, subcategory, name, price = input_products.split(" - ")
        price = int(price)

        if category not in cart:
            cart[category] = {}
        if subcategory not in cart[category]:
            cart[category][subcategory] = []
        cart[category][subcategory].append((name, price))
    except ValueError:
        print("Некорректный формат ввода.")
    
sorted_categories = sorted(cart.keys()) 

for category in sorted_categories:
    print(f"{category}:")
    sorted_subcategories = sorted(cart[category].keys())  
    for subcategory in sorted_subcategories:
        print(f"  {subcategory}:")
        sorted_items = sorted(cart[category][subcategory], key=lambda item: (item[1], item[0]))
        for name, price in sorted_items:
            print(f"    - {name} ({price} руб.)")