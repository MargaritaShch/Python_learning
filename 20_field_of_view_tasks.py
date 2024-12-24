#field of view
print("Task 1======================================")
class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def _compute_diameter(self):
        return 2 * self.radius
    
    def get_square(self):
        return self._pi * (self.radius**2)
    
    def get_lenght(self):
        return self._pi * self._compute_diameter()
    
class CircleChild(Circle):
    def show_pi(self):
        return self._pi
    
circle = Circle(50)
print(circle.get_square())
print(circle.get_lenght())
print(circle._compute_diameter())
print(CircleChild(5).show_pi())
    
#private
print("Task 2======================================")
class Worker:
    __premium_coef = 1

    def __init__(self, salary):
        self.salary = salary

    def overall_salary(self):
        return self.salary * 12 + self.salary * self.__premium_coef
    
class SeniorWorker(Worker):
    __senior_bonus = 300_000

    def overall_salary(self):
        return self.salary * 12 + self.salary * self._Worker__premium_coef + self.__senior_bonus
    
w = Worker(100_000)
print(w.overall_salary())
# print(w.__premium_coef)
print(Worker.__dict__)
print(w._Worker__premium_coef)

sw = SeniorWorker(200_000)
print(sw.overall_salary())