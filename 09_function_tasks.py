#1. functions
print("Task 1 ======================================")
def add(x,y):
    return x+y

print(add(5,10))
print(add('abc','def'))
print(max(add(55,105), add(7,201),))
a = add(88,45)
print(a)

#2. functions return None
print("Task 2 ======================================")
def func():
    pass
print(func())

#3. args
print("Task 3 ======================================")
#аргумент по умолчанию
def award(salary, prifit, position = 2.5):
    return salary* prifit*position

print(award(10000, 2.4))
#позиционные аргументы
award(500000, prifit=1.4, position=4)
#именованные аругменты
def foo(a, b=3,*, c, d=10):
    return(a,b,c,d)

print(foo(1,2, c=3,d=4))
print(foo(1, c=3,d=4))

#произвольное кол-во аргументов
def func2(*args):
    return(args)

print(func2(1,2,3, 'abc'))
print(func2())
print(func2(1))
#складывание в словарь
def func3(**kwards):
    print(kwards)

print(func3(a=1, b=2, c=3))
print(func3())
print(func3(a='python'))

#4. распаковка 
print("Task 4 ======================================")
fruits = ['lemon', 'pear', 'waterlemon', 'one more', 'tomato']

first, second, *remaining = fruits
print(remaining)

first, *remaining = fruits
print(remaining)
