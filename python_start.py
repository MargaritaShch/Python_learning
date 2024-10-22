# Множественный вывод
print("Result: ", 6, 2, "!")

# #удление проблелов
print("Result: ", 7, 3, "!", sep="")

# #соединение двух print(end=""), 
print("Result: ", 8, 4, "!", end="")
print("Second Line")

# #перенос строки после print(end="\n"), 
print("Result: ", 9, 5, "!", end="\n")
print("Third Line")

# #двойные кавычки в строке, 
print("Result: ", 9, 5, "!", end="\n")
print("Forth \" Line")
# #двойные кавычки в строке 2й вариант
print('Forth " Line')

# #табуляция
print('Five\t Line')

#слеш \  как часть строки
print('Six\t \\Line')

# # МАТЕМАТИЧЕКИЕ ВЫРАЖЕНИЯ
# # Сложение
print(5+5)

# #Умножение
print(5*5)

# #Строка+вычисленеи
print("Результат:", 4*5)

# #Возведение в квадрат
print(5**5)

# #Деление
print(5/5)

# #Округление
print(5//2)

# ММАТЕМАТИЧЕСКИЕ ФУНКЦИИ
# Минимальное значение
print("Result:", min(2, 7, 9 ,8, 1))

# #Минимальное значение
print("Result:", max(2, 7, 9 ,8, 1))

# #Абсолютное значение
print("Result:", abs(-6))

# #Возведение в степень
print("Result:", pow(5, 7))

# #Округление к ближашему целому
print("Result:", round(5/2))

# ПОЛУЧЕНИЕ ДАННЫХ ОТ ПОЛЬЗОВАТЕЛЯ
# Получить данные
input("Введие свой возраст:")

# # ПЕРЕМЕННЫЕ
number = 5
print("Result:", number)
#Удаление
del number
number = 7
print("Result:", number)

#Хранение разных значений
digit = 5.3456
word = "Result:"
#Приведение к строке
print(word + str(digit))

#Boolean
boolean = False

str_num = "23"
#Приведение к числу
print(number+ int(str_num))

print(word +str(number+ int(str_num)))

#РАБОТА С ПОЛЬЗОВАТЛЕМ
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num1 +=5

print("Result:" ,num1 + num2)
print("Result:" ,num1 - num2)
print("Result:" ,num1 / num2)
print("Result:" ,num1 * num2)
print("Result:" ,num1 ** num2)
print("Result:" ,num1 // num2)

word = "Hey"
print(word*3)

del word
word = 45
print(word*3)

# Условные коснтрукции
user_data = int(input("Add number: "))
if user_data !=5:
    print("Мы на месте")
    if user_data >6:
        print("Number is bigger than 5")

isHappy = True
# if isHappy:
#     print('User is happy')

if isHappy or user_data == 6:
    print('User is happy')
elif user_data == 5:
    print("Number is 5")
elif user_data == 7:
    print("Number is 7")
else: 
    print("User is unhappy")

# ТЕРНАРНЫЙ ОПЕРАТОР - сокращение if-else
data = input()
number = 5 if data == "Five" else 0

if data == "Five":
    number = 5
else:
    number = 0

print(number)

# ЦИКЛЫ for, while
#FOR
for i in range(6):
    print(i)
# Задать интервал от 1 до 6
for i in range(1,6):
    print(i)
#Третий параметр увеличивает переменную
for i in range(1,6, 2):
    print(i)
#Перебор строк 
word = "Hello, World"
for i in word:
    print(i *3)
# Посик определенного символа 
count = 0
word = "Hello, World"
for i in word:
    if i == "l":
        count += 1

print('Count:', count)

# WHILE
i = 5
while i<=15:
    print(i)
    i+=2

isHasCar = True
while isHasCar:
    if input("Enter data:") == "Stop":
        isHasCar = False

# Операторы в циклах
for  i in range(1,11):
    if i == 5:
        break
    if i%2 == 0:
        continue
    print(i)

#Нахлждение символа в строке
for i in "hello":
    if i == "p":
        found = True
        break
else:
    found = False

print(found)

# СПИСКИ ДАННЫХ LIST
# Поиск по индексам
nums = [5, 6, 7, 7, 8, 9, True, "Hello", 2.3]
nums[0] = 50
print(nums[4])
#Вложенные списки
nums2 = [5, 6, 7, [3.33, 5.12]]
nums2[0] = 50
print(nums2[3][0])
#Обращение к последнему элементу
print(nums2[-1])

# Функуии спсиков
# Добавить занчение
numbers = [5, 7, 8]
numbers.append(100)
# Устанвока занчения по index
numbers.insert(1, True)
numbers.extend(['H', 'e', 'y'])
# Сортировка элементов
numbers.sort()
#переворачивание элементов
numbers.reverse()
#удаление элементов
numbers.pop()
#удаление элементов по значению
numbers.remove(8)
#удаление элементов по индексу
numbers.pop(1)
#Удаление всех элементов
numbers.clear()
# COUNT
print(numbers.count(7))
# Lenght
print(len(numbers))

# ВЫВОД СПИСКА ЧЕРЕЗ ЦИКЛ
nums = [ 1, 2, 3, 'Hey', False]
for i in nums:
    i *= 2
    print(i)

# НАПОЛНЕНИЕ СПИСКА ПОЛЬЗОВАТЕЛЯ
n = int(input("Enter lenght:"))
user_list = []
i = 0
while i<n:
    string = "Enter element #" + str(i+1) + ": "
    user_list.append(input(string))
    i+=1
print(user_list)

def test_func():
    print("HEllo", end ="")
    print("!")

test_func()
test_func()
test_func()