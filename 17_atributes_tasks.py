#Атрибуты класаа
print("Task 1 ======================================")
INITIAL_BOUNS = 100
INTERMEDIATE_BALNCE =500
ADVANCED_BALANCE = 15000

class Client:
    bank = "Sber"
    location = "Russia"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance + INITIAL_BOUNS

        if self.balance < INTERMEDIATE_BALNCE:
            self.level = "Basic"
        elif self.balance < ADVANCED_BALANCE:
            self.level = "Intermediate"
        else:
            self.balance = "Advanced"

    @classmethod
    def bank_location(cls):
        return str(cls.bank + " " + cls.location)
    
    @staticmethod
    def on_salary_date():
        print("Ура! Зарплатал пришла!")


client = Client("Ivan", 100)
client.bank_location()
Client.country = "Russia"

John_Doe = Client("John Doe", 500)
Jone_Dofoe = Client("Jone Dofoe", 150000)


client = Client("Ivan", 100)
print(client)  # Печатает данные о клиенте
print(vars(client))  # Показывает все атрибуты клиента
Client.country = "Russia"

John_Doe = Client("John Doe", 500)
Jone_Dofoe = Client("Jone Dofoe", 150000)

print(John_Doe)  # Печатает объект John_Doe в понятном виде
print(vars(John_Doe))  # Показывает все атрибуты клиента John_Doe

# Доступ к атрибутам
print(John_Doe.name)  # Имя клиента
print(John_Doe.balance)  # Баланс клиента
print(John_Doe.level)  # Уровень клиента

# Показать атрибуты класса
print(Client.bank)  # Sber
print(Client.location)  # Russia

# Посмотреть все атрибуты класса
print(vars(Client))

        