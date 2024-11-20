# #1. index
# print("Task 1 ======================================")
# s = 'abc'[0]
# print(s)
# #last symbol
# s = 'abc'[-1]
# print(s)

# #2. len
# print("Task 2 ======================================")
# s = ' abc '
# print(len(s))
# s = ' abc '[-1]
# print(s)

# #3. срез строк
# print("Task 3 ======================================")
# s = 'abc'[0:-1]
# print(s)

# s = 'abc'[:2]
# print(s)

# s = 'abc'[-1:-2]
# print(s)

# #4. 
# print("Task 4 ======================================")
# s = 'hello world'[1:4]
# print(s)
# #5. 
# print("Task 5 ======================================")
# s = 'python'[-3:]
# print(s)
# #6. 
# print("Task 6 ======================================")
# s = 'abcdefg'[::2]
# print(s)
# #7. конкатенация
# print("Task 7 ======================================")
# print("Помни " + "о " + '''пробелах''')
# #8. умножение строк
# print("Task 8 ======================================")
# s ="asd"
# print(2*s)
# print(s*2)
# #9. форматирование строк 
# #оператор %
# print("Task 9 ======================================")
# name ="Peter"
# print('Hello, %s!' % name)
# #format()
# name ="Jhon"
# print('Hello, {}!'.format(name))
# #F-строки
# name = "Eric Idle"
# age = 74
# profession = "comedian"
# affiliation = "Monty Python"

# print(f"Hello, {name}. You are {age}.")
# print(f"{2*5}")
# print(f"{name.lower()} is funny")

# #10.split разбиение строки по разделителю
# print("Task 10 ======================================")
# str = "adcf adcd dcfd"
# print(str.split())

# #11.join превращение спика строк в одно строку
# print("Task 11 ======================================")
# arr = ['adcf', 'adcd', 'dcfd']
# print(" ".join(arr))

# #12.replace замена подстроки на заданную строку в строке
# print("Task 12 ======================================")
# str = 'adcfdcfd'
# print(str.replace('cf', 'Y'))
# print(str.replace('cf', 'Z', 6))

#13. С клавиатуры вводится две строки:Раздел сайта (например, "articles", "blog", "news")
# Заголовок статьи (например, "How to write a program in Python"). Заголовок статьи не содержит знаков препинания.
# Программа должна сгенерировать URL-адрес для сайта https://www.mycoolsyte.com/, который будет иметь следующий формат: https://www.mycoolsyte.com/<раздел>/<заголовок-статьи>;. Преобразуйте заголовок в соответствие с примером.
# Формат ввода
# articles
# How to write a program in Python
# Формат вывода
# Созданный URL: https://www.mycoolsyte.com/articles/how-to-write-a-program-in-python
# print("Task 13 ======================================")
# input_site = input()
# input_titile = input()
# input_title_change = input_titile.lower().replace(' ', '-')
# input_site_change = input_site.lower()

# site = 'https://www.mycoolsyte.com'
# url = f"{site}/{input_site_change}/{input_title_change}"
# print(f"Созданный URL: {url}")

#14.Напишите программу, которая принимает пароль в качестве входных данных с терминала и проверяет его сложность, проверяя на следующие условия:
# Длина: Пароль должен быть не менее 8 символов. Если длина пароля меньше 8 символов, он считается слабым.
# Критерии сложности: Пароль должен содержать хотя бы один символ из каждого из следующих типов:
# Прописные буквы (A-Z)
# Строчные буквы (a-z)
# Цифры (0-9)
# Специальные символы (!@#$%^&*(),.?":{}|<>)
# Вывод:

# Программа должна выводить одну из следующих оценок:

# "Сильный пароль": Пароль удовлетворяет 4 критериям сложности.
# "Средний пароль": Пароль удовлетворяет 3 из 4 критериев сложности.
# "Слабый пароль": Пароль удовлетворяет менее 3 критериев сложности.
print("Task 14 ======================================")
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
digits = [str(i) for i in range(0, 10)]  
special_characters = list("!@#$%^&*(),.?\":{}|<>")

input_password = input()

if len(input_password) < 8:
    print("Слабый пароль")
    exit()

has_uppercase_letters = False
has_lowercase_letters = False
has_digits = False
has_special_characters = False


for char in input_password:
    if char in uppercase_letters:
        has_uppercase_letters = True
    if char in lowercase_letters:
        has_lowercase_letters = True
    if char in digits:
        has_digits = True
    if char in special_characters:
        has_special_characters = True

result = sum([has_lowercase_letters, has_uppercase_letters, has_digits,has_special_characters])

if result == 4:
    print("Сильный пароль")
elif result == 3:
    print("Средний пароль")
else:
    print("Слабый пароль")




