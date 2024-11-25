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

#9. Task 9
print("Task 9 ======================================")
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