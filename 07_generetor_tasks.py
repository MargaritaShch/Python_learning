#1.Генераторы списков 
print("Task 1 ======================================")
a = [1,2,3,4,5]
b=[i+10 for i in a]#генератор
print(a)
print(b)
#Добавить условие/ randint - генерит случайное число из диапазона
from random import randint
nums = [randint(10,20) for i in range(10)]
print(nums)

#2.Генераторы словарей и множеств
print("Task 2 ======================================")
a = {i:i**2 for i in range(11,15)}
print(a)#result = {11: 121, 12: 144, 13: 169, 14: 196}
#3.представление элемента
print("Task 3 ======================================")
my_dict = {11: 121, 12: 144, 13: 169, 14: 196}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#4.Генераторы
print("Task 4 ======================================")
a = (i for i in range(2,8))
print(a)

for i in a:
    print(i)
#не полуситяс перебрать второй раз
for i in a:
    print(i)

def func(start, finish):
    while start < finish:
        yield start * 0.33
        start +=1

a = func(1,4)
print(a)

for i in a:
    print(i)
for i in a:
    print(i)
