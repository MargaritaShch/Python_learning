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