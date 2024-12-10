from datetime import date
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

print((*fruits[1:], fruits[0]))

#** - развернуть словарь
date_info = {'year': '2020', 'month': '01', 'day': '01' }
track_info = {'artist' : "Beethoven", 'title': 'Symphony No 5'}
all_info = {**date_info, **track_info}
print(all_info)

#5. Anon functions
print("Task 5 ======================================")

func = lambda x, y: x+y
print(func(1,2))
print(func('a', 'b'))

print((lambda x, y: x+y)(2,3))

#6. Функции. Аргументы 1
# Допустим, ваша компания каждый месяц выделяет некоторую сумму денег на подарки сотрудникам ко дню рождения. Каждый месяц эта сумма разная. Также у вас есть список дней рождения сотрудников. Вам нужно написать удобный инструмент для того, чтобы сотрудники могли понять, сколько денег им ждать на день рождения, если известно, какой бюджет выделяется на месяц и для какого месяца производится подсчет. Для этого напишите функцию gift_count, которая будет принимать:

# бюджет, который выделяется компанией на месяц
# номер месяца, на который нужно произвести расчет
# словарь, где ключи - это имена сотрудников, а значения - datetime.date с датой рождения сотрудника.
# Функция должна вывести на экран фразу (цифры должны быть подставлены в соответствии со значениями аргументов):
# Именинники в месяце 5: Иванов Иван Иванович (01.05.1989), Петров Петр Петрович (06.05.1998). При бюджете 20000 они получат по 10000 рублей.
# Если в ответе получается не целое число, округлите его до меньшего целого. Именинники должны быть выведены в порядке дня рождения по возрастанию (не полной даты рождения, а именно дня). Если в выбранном месяце нет именинников, должна быть выведена строка "В этом месяце нет именинников."

# Формат ввода
# birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
# gift_count(20000, 5, birthdays)
# gift_count(budget=20000, month=5, birthdays=birthdays)

# Формат вывода
# Именинники в месяце 5: Иванов Иван Иванович (01.05.1989), Петров Петр Петрович (06.05.1998). При бюджете 20000 они получат по 10000 рублей.

# Примечания
# В примере формата ввода показаны несколько вариантов вызова функции gift_count: с порядковыми аргументами и с передачей их по имени. Соответственно, аргументы функции должны называться так же, как они используются в примере.
print("Task 6 ======================================")
# birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
def gift_count(budget, month, birthdays):
    month_birth = {
        name: birth_date
        for name, birth_date in birthdays.items()
        if birth_date.month == month
    }

    if not month_birth:
        print("В этом месяце нет именинников.")
        return
    
    sorted_birth = sorted(month_birth.items(), key = lambda item: item[1].day)

    birth_list = ', '.join(
        f"{name} ({birth_date.strftime('%d.%m.%Y')})"
        for name, birth_date in sorted_birth
    )

    gift_amount = budget // len(month_birth)

    print(
        f"Именинники в месяце {month}: {birth_list}. "
        f"При бюджете {budget} они получат по {gift_amount} рублей."
    )

birthdays = {
    "Иванов Иван Иванович": date(1989, 5, 1),
    "Петров Петр Петрович": date(1998, 5, 6),
    "Сидоров Сидр Сидорович": date(1995, 6, 15),
    
}

gift_count(20000, 5, birthdays)

#7.Функции. Аргументы 2
# Вам нужно написать функцию lists_sum, которая принимает произвольное количество списков чисел, и возвращает сумму всех этих чисел. Предусмотрите дополнительный аргумент unique, который по умолчанию равен False, но если в функцию подается unique=True, то функция должна вернуть сумму всех уникальных чисел из всех списков. Если поданы только пустые списки или списки чисел вообще не поданы в функцию, то считать сумму чисел нулём.
# Пример использования
# lists_sum([1, 1], [1], [1, 2, 3]) # должна вернуть 9
# lists_sum([1, 1, 1], [1, 1], unique=True) # должна вернуть 1
# lists_sum([1, 1, 1], unique=False) # должна вернуть 3
print("Task 7 ======================================")

def lists_sum(*lists, unique=False):
    all_num = [num for sublist in lists for num in sublist]
    if unique:
        all_num = set(all_num)

    return sum(all_num)

print(lists_sum([1, 1], [1], [1, 2, 3]))
print(lists_sum([1, 1, 1], unique=False))
print(lists_sum([1, 1, 1], [1, 1], unique=True))

#Вы с друзьями периодически собираетесь на лавке у подъезда выпить чаю с баранками. Каждый раз собирается разное количество человек, которое должно скинуть по n рублей на мероприятие. Также у вас в компании есть общак, в который можно докинуть денег, а можно взять. Все транзакции в общак логируются, т.е. у вас есть информация о каждом переводе денег в/из общака для каждого из друзей. Ваша задача - посчитать, сколько денег должен каждый из собравшихся на мероприятие друзей на момент начала мероприятия. Будем считать, что все деньги проходят через общак, поэтому у каждого друга к началу мероприятия уже есть некоторый "баланс" в общаке.

# Формат хранения данных
# Все операции с деньгами хранятся в базе данных и приходят к вам в виде списка словарей вида:

#     {"name": "Василий", "amount": 500},
#     {"name": "Петя", "amount": 100},
#     {"name": "Василий", "amount": -300},
# ]
# где name - имя друга (считаем, что всех зовут по-разному), amount - сумма, которая добавлена в общак. Если сумма отрицательная - это значит, что друг взял деньги из общака. Также считаем, что скидываются суммы в рублях без копеек.

# Вам нужно описать две функции.
# get_balance(name, transactions) -> int
# функция, которая возвращает текущий баланс друга с именем name, исходя из списка транзакций transactions. Если имя name ни разу не встречается в списке transactions, считаем, что баланс этого друга в общаке равен 0 рублей.
# count_debts(names, amount, transactions) -> dict
# функция, которая принимает список имен присутствующих на мероприятии друзей names, стоимость баранок и чая на человека amount, а также список транзакций в общак transactions. Вернуть эта функция должна словарь вида {"имя_друга": 100}, где 100 - это количество денег, которое он должен скинуть на мероприятие. Если на балансе друга больше денег, чем требуется на мероприятие, то он должен 0 рублей.
# Формат ввода
# transactions = [ {"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100}, {"name": "Василий", "amount": -300}, ]
# get_balance("Василий", transactions)
# count_debts(["Василий", "Петя", "Вова"], 150, transactions)

# Формат вывода
# get_balance("Василий", transactions) == 200
# count_debts(["Василий", "Петя", "Вова"], 150, transactions) == {"Василий": 0, "Петя": 50, "Вова": 150}
print("Task 7 ======================================")
def get_balance(name, transactions) -> int:
    balance = 0
    for transaction in transactions:
        if transaction["name"] == name: 
            balance += transaction["amount"]  
    return balance

def count_debts(names, amount, transactions) -> dict:
    balances = {name: 0 for name in names}
    
    for transaction in transactions:
        if transaction["name"] in balances:
            balances[transaction["name"]] += transaction["amount"]

    contributions = {}
    for name in names:
        current_balance = balances.get(name, 0)
        required_amount = max(0, amount - current_balance)
        contributions[name] = required_amount

    return contributions

