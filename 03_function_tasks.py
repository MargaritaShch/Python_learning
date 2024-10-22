# 1. DEF (сумма)
def plus(a, b):
    c  = a + b
    return c

function_result = plus(6,4)
print(function_result)

# 2.Напиши функцию greet, которая принимает имя пользователя в качестве аргумента и выводит сообщение приветствия. Например, если имя пользователя "Анна", функция должна вывести "Привет, Анна!"
def greet(name):
    return print(f"Привет, {name}!")
greet("Анна")

# 3.Создай функцию factorial, которая принимает целое число n и возвращает его факториал. Факториал числа n (n!) равен произведению всех натуральных чисел от 1 до n.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
number = factorial(5)
print(f"Факториал: {number}")
    
# 4.Создай функцию find_max, которая принимает список чисел и возвращает самое большое число из этого списка.
def find_max(list):
    if not list:
        return "Empty"
    
    max_num = None
    for num in list:
        if isinstance(num, (int, float)):
            if max_num is None or num >max_num:
                max_num = num

    if max_num is not None:
        return max_num
    else:
        return "Нет числовых элементов"

number_list = [1, 0, 5, "str", None, False, 99, 90]
result = find_max(number_list)
print(f"Самое большое число в списке {result}")

#5.Напиши функцию reverse_string, которая принимает строку и возвращает её перевёрнутый вариант.
def reverse_string(string):
    return ''.join(reversed(string))

word = reverse_string("Привет")
print(f"Result: {word}")