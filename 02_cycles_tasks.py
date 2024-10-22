# 1. Цикл от 0 n-1
for i in range(6):
    print(i) # result = 0,1,2,3,4,5

# 2. Цикл по итерируемому объеку
string = "abcdef"
for character in string:
    print("Следующий цикл: ", character)

# 3. Испольщование индекса объекта в перебираемой коллекуии (enumerate)
string_1 = "abcdef"
for i, character in enumerate(string_1):
    print("Следующий цикл: ", i, ':', character)

# 4. Цикл while
n = 20
i = 2
s = 0
while i < n: 
    s+=i
    i+=2
print(s)

# 5. Напиши программу, которая принимает на вход целое число N и вычисляет сумму всех чисел от 1 до N
input = int(input("Введите число: "))
result = 0
#итерируемся по диапазону от 1
for i in range(1, input +1):
    result += i

print("Result: ", result)

# 6. Вывод четных чисел от 1 до N
input_6 = int(input("Введите число: "))
if input_6 < 1:
        print("Ввкдите число больше 0")
else:
    for i in range(1,input_6):
        if i % 2 == 0:
            print(i)

# 7. Напиши программу, которая запрашивает у пользователя целое число X и выводит таблицу умножения на это число от 1 до 10
input_7 = int(input("Введите число: "))
if input_7 < 1:
    print("Ввtдите число больше 0")
else:
    for i in range(11):
        print( input_7* i)
