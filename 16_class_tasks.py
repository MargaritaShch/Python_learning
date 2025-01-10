#определить простейший класс
print("Task 1 ======================================")
class Nothing:
    pass

nothing1 = Nothing()
nothing2 = Nothing()
print(type(nothing1), type(nothing2))

#методы классов
print("Task 2 ======================================")
class Meower:
    def meow(self):
        print('Meow!')
cat = Meower()
cat.meow()
Meower.meow(cat)

#конструктор
print("Task 3 ======================================")
class Flien:
    def __init__(self):
        print('Я родился!')

luntik = Flien()
INITIAL_BOUNS = 100
INTERMEDIATE_BALNCE =500
ADVANCED_BALANCE = 15000
class Client:
    def __init__(self,name, balance ):
        self.name = name
        self.balance = balance +INITIAL_BOUNS
    
        if self.balance < INTERMEDIATE_BALNCE:
            self.level = 'BASIC'
        elif self.balance < ADVANCED_BALANCE:
            self.level = "INTERMEDIATE"
        else:
            self.level = "ADVANCED"

John_Doe = Client('John Doe', 500)
John_Dofe = Client('John Dofe', 15000)
print(John_Dofe.level)
print(John_Doe.level)

John_Doe.email = 'gjg@email.com'
print(John_Doe.email)
delattr(John_Doe, 'email')
hasattr(John_Doe, 'email')

#task4
print("Task 4 ======================================")
class Calculator:
    last = None

    def __init__(self):
        self.history_list = []

    def sum(self, a, b):
        result = a + b
        operation = f"sum({a}, {b}) == {result}"
        self._log_operation(operation)
        return result
    
    def sub(self, a, b):
        result = a - b
        operation = f"sub({a}, {b}) == {result}"
        self._log_operation(operation)
        return result
    
    def mul(self, a, b):
        result = a * b
        operation = f"mul({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def div(self, a, b, mod=False):
        if mod:
            result = a % b
            operation = f"div({a}, {b}) == {result}"
        else:
            result = a / b
            operation = f"div({a}, {b}) == {result}"
        self._log_operation(operation)
        return result

    def history(self, n):
        if not self.history_list:  
            return None
        if 1 <= n <= len(self.history_list):
            return self.history_list[-n]
        else:
            return "Invalid history index."

    @classmethod
    def clear(cls):
        cls.last = None

    def _log_operation(self, operation):
        self.history_list.append(operation)
        Calculator.last = operation


    @classmethod
    def clear(cls):
        cls.last = None

    def _log_operation(self, operation):
        self.history_list.append(operation)
        Calculator.last = operation

calc1 = Calculator()
calc2 = Calculator()

calc1.sum(5, 10)  # Выполнена операция sum(5, 10)
calc1.div(10, 3, mod=True)  # Выполнена операция div(10, 3)

print(calc1.history(1))  # div(10, 3) == 1
print(calc1.history(2))  # sum(5, 10) == 15
print(Calculator.last)  # div(10, 3) == 1

Calculator.clear()
print(Calculator.last)

print("Task 5 ======================================")
class BaseWallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def __repr__(self):
        return f"{self.__class__.__name__} Wallet {self.name} {self.amount}"
    
    def __str__(self):
        return f"{self.__class__.__name__.replace('Wallet', '')} Wallet {self.name} {self.amount}"
    
    def to_base(self):
        return self.amount * self.exchange_rate
    
    def spend_all(self):
        if self.amount > 0:
            self.amount = 0

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount + other.to_base() / self.exchange_rate
        elif isinstance(other, (int, float)):
            new_amount = self.amount + other
        else:
            raise TypeError("Unsupported type for addition")
        return self.__class__(self.name, new_amount)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = self.amount - other.to_base() / self.exchange_rate
        elif isinstance(other, (int, float)):
            new_amount = self.amount - other
        else:
            raise TypeError("Unsupported type for subtraction")
        return self.__class__(self.name, new_amount)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            new_amount = other - self.amount
            return self.__class__(self.name, new_amount)
        raise TypeError("Unsupported type for subtraction")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            return self.__class__(self.name, new_amount)
        raise TypeError("Unsupported type for multiplication")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_amount = self.amount / other
            return self.__class__(self.name, new_amount)
        raise TypeError("Unsupported type for division")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.amount == other.amount
        return False


class RubleWallet(BaseWallet):
    exchange_rate = 1

class DollarWallet(BaseWallet):
    exchange_rate = 60

class EuroWallet(BaseWallet):
    exchange_rate = 70


