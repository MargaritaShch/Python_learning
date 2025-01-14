from flask import Flask
from functools import partial, cached_property, wraps
import statistics
#Decorator
print("Task 1======================================")
class A:
    @staticmethod
    def p():
        print("Привет, я в декораторе")

print(A.p())

#Function  is object
print("Task 2======================================")
def p1(s = "привет"):
    return s.upper()

print(p1())

p2 = p1
print(p2)

# del p1
# print(p1())# но осатется p2

#function within a function
print("Task 3======================================")
def a():
    def b():
        print("Function b")
    print("Function a")
    b()

print(a())

#function can return functiob
print("Task 4======================================")
def a():
    def b():
        print("Finction b")
    return b

print(a())

c= a()
print(c)
print(a()()) #return Finction b

#Callbacks
print("Task 5======================================")
def a(callback):
    print("Сначала выполним код, написанный в функции а, а потом:")
    callback()

def b():
    print("Код в функуии b")

def c():
    print("Код в функции с")

print(a(b))
print(a(c))

#create own decorator
print("Task 6======================================")
def decorator(source_func):
    def wrapper():
        print("Код ДО исходной функции")
        source_func()
        print("Код ПОСЛЕ исходной функции")
    return wrapper

def func():
    print("Код ВНУТРИ исходной функции")

print(decorator(func))
print(decorator(func)())
func = decorator(func)
print(func())

#syntax sugar
print("Task 7======================================")
@decorator
def func():
    print("код ВНУТРИ исходной функции")

print(func())
func = decorator(func)
print(func)

#syntax sugar
print("Task 8======================================")
def decorator1(func):
    def wrapper():
        print("Деуоратов 1 - начало")
        func()
        print("Декоратор 1 - конец")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Деуоратов 2 - начало")
        func()
        print("Декоратор 2 - конец")
    return wrapper

@decorator1
@decorator2
def f():
    print("Function")

print(f())

@decorator2
@decorator1
def f():
    print("Function")

print(f())

#wrap arguments
print("Task 9 ======================================")
def func_with_2_args(name, last_name):
    print("Здесь начинает выполняться функция")
    print("Name: ", name)
    print("Last name: ", last_name)

print(func_with_2_args("Nicola", "Tesla"))

def decorator_with_2_args(func):
    def wrapper_with_2_args(arg1, arg2):
        print("Аргументы, которые получил декоратор:", ", ".join((arg1, arg2)))
        func(arg1, arg2)
    return wrapper_with_2_args

@decorator_with_2_args
def func_with_2_args(name, last_name):
    print("Здесь начинает выполняться функция")
    print("Name: ", name)
    print("Last name: ", last_name)

print(func_with_2_args("Will", "Smith"))

#decoration methods
print("Task 10 ======================================")
def method_decorator(method):
    def method_wrapper(self,x):
        return method(self, x*1.15)
    return method_wrapper

class Price:
    def __init__(self, price):
        self.price = price

    @method_decorator
    def get_price(self, exchange_rate):
        return self.price * exchange_rate
    
p = Price(100)
print(p.get_price(72))

#general views decorators with args
print("Task 11 ======================================")
def common_decorator(func):
    def common_wrapper(*args,**kwargs):
        print("Декторатор приянял args:", args)
        print("Декторатор приянял kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("Декоратор завершается\n")
        return result
    return common_wrapper

@common_decorator
def zero_args():
    print("Функция без аргументов")

@common_decorator
def one_arg(x):
    print("Функция возвращается с одним аргументом x=", x)

@common_decorator
def two_args(x,y):
    print("Функция возвращается с одним аргументом x, y=", x, y)

@common_decorator
def multiple_args(*args):
    print("Функуция, которая приняла args:", args)

@common_decorator
def any_args(*args, **kwards):
    print("Функуция, которая приняла args:", args, "и kwards:" ,kwards)

print(zero_args())
print(one_arg(25))
print(one_arg(x = 25))
print(two_args("ПРИВЕТ", "АРГУМЕНТ"))
print(multiple_args(1,2,3,4,5))
print(any_args(1,2,3,4, a="A", b="B", e = 2.71))

#Decoration's fabric
#with framework Flask
print("Task 11 ======================================")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

print(hello_world())

def decorator_maker():
    print("decorator_maker started")
    def decoratoe(func):
        print("decorator started")
        def wrapper():
            print("wrapper started")
            func()
            print("wrapper ended")
        print("decorator retirns wrapper")
        return wrapper
    print("decorator_maker retun decorator")
    return decorator

def usual_func():
    print("usual function")

new_decorator = decorator_maker()
print(new_decorator)
usual_func = new_decorator(usual_func)
print(usual_func())

@decorator_maker()
def usual_func():
    print("usual func")

print(usual_func())

#Decoration's fabric
#with framework Flask
#with args
print("Task 12 ======================================")
def decorator_maker(dec_arg_1, dec_arg_2):
    print("Inside decorator_maker. Decorator args:", dec_arg_1, dec_arg_2)
    def decorator(func):
        print("Inside decorator. Decorator args:", dec_arg_1, dec_arg_2)
        def wrapper(func_arg_1, func_arg_2):
            print("Inside wrapper. Decorator args:", dec_arg_1, dec_arg_2)
            print("Inside decorator. Functions args:", func_arg_1, func_arg_2)
        return wrapper
    return decorator

@decorator_maker("DEC_ARG_1", "DEC_ARG_2")
def func(s1, s2):
    print("Inside functions. Functions args:", s1, s2)

# print(func("FUNC_ARG_1, FUNC_ARG_2"))

#Decoration's fabric
#with framework Flask
#with args
#field __name__ and library functools
print("Task 13 ======================================")
def our_function():
    pass

print(our_function.__name__)

@decorator
def decorated_function():
    pass

print(decorated_function.__name__)

#library functools
print("Task 14 ======================================")
print(int('10010'))
print(int('10010', base =2), end = '\n\n')

basetwo = partial(int, base = 2)
basetwo.__doc__ = 'Convert base 2 string to an int'
print(basetwo('10010'))

#library functools = > cached_property
print("Task 14 ======================================")
class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)
    
    @cached_property
    def variance(self):
        return statistics.variance(self._data)
        
ds = DataSet([1,2,3,4,5])
print(ds.stdev)
print(ds.variance)

#library functools = > wraps
print("Task 15 ======================================")
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print("Calling deckrated function")
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print("Calling example function")

print(example())
print(example.__name__)

#library functools = alternative
print("Task 16 ======================================")
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def add(a,b):
    return a+b

@register
def multiply(a,b):
    return a*b

def opertion(func_name, a, b):
    func = PLUGINS[func_name]
    return func(a,b)

print(PLUGINS)
print(opertion('add', 2,3))
print(opertion('multiply', 2,3))

#library functools = alternative
#wrapper under classes
print("Task 17 ======================================")
@common_decorator
class Calculator:
    def __init__(self, num):
        self.num = num
        import time
        time.sleep(2)

    def __call__(self):
        print("call")

    def doubled_and_add(self):
        res = sum([i*2 for i in range(self.num)])
        print("Result : {}".format(res))

c = Calculator(100)
print(c.doubled_and_add())
print(c())
print(common_decorator(c)())

        
