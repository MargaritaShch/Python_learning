#inheritance
print("Task 1 ======================================")
class Base:
    class_field = 42

    def __init__(self):
        self.instance_field = "I'm instance field"

    def some_instance_method(self, x):
        return x**2
    
class Inherited(Base):
    Inherited_class_field = 24

    def inherited_class_method(self):
        return self.Inherited_class_field /2
    
base = Base()
print(base.class_field, base.instance_field, base.some_instance_method(10), sep = '\n')  

#super
print("Task 2 ======================================")
class Builder:
    def __init__(self, name):
        self.name = name
        self.helmet = None
        print(f"СТроитель {self.name} проснулся и готов к работе")

    def put_on_helmet(self, helmet_number):
        self.helmet = helmet_number
        print(f"СТроитель {self.name} надел каску с номером {helmet_number}")

class Driver(Builder):
    def __init__(self, name):
        super(Driver, self).__init__(name)
        print(f"СТроитель {self.name}  сеголня назначен водителем и везет всех на стройку")

b1 = Builder("Vasya")
print(b1.put_on_helmet(25))

b2 = Driver("Ivan")
print(b2.put_on_helmet(34))

#multiple inheritance
print("Task 3 ======================================")
class Person(object):
    def __init__(self, name):
        self.name = name
        print(f"Человек {self.name}  проснулся")

    def move(self):
        print(f"Человек {self.name} пытается встать с кровати")

class Pedestrian(Person):
    def move(self):
        print(f"Человек {self.name} пошел пешком")

    def wave(self):
        print("Прмахнулся рукой")

class Driver(Person):
    def move(self):
        print(f"Человек {self.name} поехал на машине")

    def beep(self):
        print("Побибикал")

class Ivan(Driver, Pedestrian):
    pass

print(Person("Vlad").move())
print(Driver("Olga").move())
print(Ivan("Ivan").move())
# print(Driver("Ivan").wave())
        
