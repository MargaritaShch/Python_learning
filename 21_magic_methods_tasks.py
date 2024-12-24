#len
print("Task 1======================================")
a = [1,2,3,4,5,6]
print(len(a))
print(dir(a))

def our_len(some_object):
    return some_object.__len__()

print(our_len(a))

print("Task 2======================================")
class Track:
    def __init__(self, values_list, sample_rate = 22050):
        self.values_list = values_list
        self.sample_rate = sample_rate

    def __len__(self):
        return round(self.values_list.__len__() / self.sample_rate) 
    
track = Track([25] * 100_00)
print(len(track), our_len(track))

#string
print("Task 3======================================")
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
    
    def __str__(self):
        return f"Student {self.name} from the group {self.group}"
    
s = Student("Fill", "21")
print(s)

#math operation
print("Task 4======================================")
class Meal:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return ": ".join([self.title, str(self.price)])
    
    def __repr__(self):
        return str(self)
    
    def __add__(self,other):
        if isinstance(other, Meal):
            new_title = ": ".join([self.title, other.title])
            new_price = self.price + other.price
        else:
            new_title = self.title + " и что-то еще"
            new_price = self.price + float(other)
        return Meal(new_title, new_price)
    
print(Meal("Big Mac", 200))
print(Meal("Big Mac", 200) + Meal("French Fries", 50))


print("Task 5======================================")
def our_call_methods(self):
    self.title = "Ты все съел!"
    self.price = -self.price

Meal.__call__ = our_call_methods
m = Meal("Борщ",150)
print(m())
print(m)