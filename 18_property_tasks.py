#PROPERTIES
print("Task 1 ======================================")
INITIAL_BOUNS = 100
INTERMEDIATE_BALNCE =500
ADVANCED_BALANCE = 15000

class Client(object):
    bank = "Sberbank"
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

    @property
    def pence(self):
        return self.balance *100
    
#setter
    @pence.setter
    def pence(self,value):
        self.balance = value /100

client = Client("Ivan", 100)
print(client.balance) 
client.balance = 300
print(client.pence)