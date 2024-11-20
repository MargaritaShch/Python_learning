#1. index
print("Task 1 ======================================")
s = 'abc'[0]
print(s)
#last symbol
s = 'abc'[-1]
print(s)

#2. len
print("Task 2 ======================================")
s = ' abc '
print(len(s))
s = ' abc '[-1]
print(s)

#3. срез строк
print("Task 3 ======================================")
s = 'abc'[0:-1]
print(s)

s = 'abc'[:2]
print(s)

s = 'abc'[-1:-2]
print(s)

#4. 
print("Task 4 ======================================")
s = 'hello world'[1:4]
print(s)
#5. 
print("Task 5 ======================================")
s = 'python'[-3:]
print(s)
#6. 
print("Task 6 ======================================")
s = 'abcdefg'[::2]
print(s)
#7. конкатенация
print("Task 7 ======================================")
print("Помни " + "о " + '''пробелах''')
#8. умножение строк
print("Task 8 ======================================")
s ="asd"
print(2*s)
print(s*2)
#9. форматирование строк 
#оператор %
print("Task 9 ======================================")
name ="Peter"
print('Hello, %s!' % name)
#format()
name ="Jhon"
print('Hello, {}!'.format(name))
#F-строки
name = "Eric Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"

print(f"Hello, {name}. You are {age}.")
print(f"{2*5}")
print(f"{name.lower()} is funny")

#10.split разбиение строки по разделителю
print("Task 10 ======================================")
str = "adcf adcd dcfd"
print(str.split())

#11.join превращение спика строк в одно строку
print("Task 11 ======================================")
arr = ['adcf', 'adcd', 'dcfd']
print(" ".join(arr))

#12.replace замена подстроки на заданную строку в строке
print("Task 12 ======================================")
str = 'adcfdcfd'
print(str.replace('cf', 'Y'))
print(str.replace('cf', 'Z', 6))