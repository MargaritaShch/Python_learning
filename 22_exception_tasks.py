from datetime import datetime, timedelta
from api import register_booking 
#Syntax Error
print("Task 1======================================")
# print(0/0))

#RecursionError
print("Task 2======================================")
# RecursionError: maximum recursion depth exceeded
# def recursion():
#     return recursion()
# recursion()

#IndentationError
print("Task 3======================================")
# IndentationError: expected an indented block after 'for' statement on line 14
# for i in range(10):
# print("Hello World")

#KeyBoardInterrupt
print("Task 4======================================")
# while True:
#     pass

#Exceptions
print("Task 5======================================")
#TypeValue
# a = 5
# b = "string"
# print(a+b) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#ValueError
# s = 5
# print(int(s))
# s = "qwerty"
# print(int(s)) #ValueError: invalid literal for int() with base 10: 'qwerty'

#ZeroDevisionError
# print(100/0) #ZeroDivisionError: division by zero

#AttributeError
# class A:
#     a=3
# a_instance = A()
# a.some_attr

#ImportError
# import spme_none_existing_module #ModuleNotFoundError: No module named 'spme_none_existing_module'

#LookupError
    #IndexError
# a = [1,10,15]
# print(a[20]) #IndexError: list index out of range

    #KeyError
# d = {1:"one", 2:"two"}
# print(d[15]) #KeyError: 15

#NameError
# print(truly) #NameError: name 'truly' is not defined

#Work with exceptions
print("Task 6======================================")
#operator raise
# raise ValueError("Сообщение об ошибке")

print("Task 7======================================")
def get_note_name(note):
    if not isinstance(note, (str,int)):
        raise TypeError("The note value should be string or int")
    
    letters = "CDEFGAHB"
    if note not in list(range(1,8)) + list(letters) + list(letters.lower()):
        raise ValueError(f"{note} is not a note")
    
    answers = ('до'," ре", "ми", "фа", "соль", "ля", "си")
    if isinstance(note, int):
        return answers[note-1]
    return answers[letters.index(note.upper())]

print(get_note_name('a'), get_note_name("A"),get_note_name(6))
# print(get_note_name(3.0)) #TypeError: The note value should be string or int
# print(get_note_name(45)) #ValueError: 45 is not a note

#try excet
print("Task 7======================================")
try:
    get_note_name('abcdef')
except:
    print("oops! something wrong...")

try:
    get_note_name('abcdef')
except ValueError:
    print("oops! something wrong...")

# try:
#     get_note_name(3555.0)
# except ValueError:
#     print("oops! something wrong...") #TypeError: The note value should be string or int

try:
    get_note_name(100500.0)
except (ValueError,TypeError):
    print("oops! something wrong...")


try:
    get_note_name(100500.0)
except ValueError:
    print("Неверное значение")
except TypeError:
    print("Type is not correct")

#as
try:
    get_note_name(100500)
except ValueError as exc:
    print(exc)

#args
try:
    raise Exception("description", "arg1", 45, 34.2)
except Exception as exc:
    print(exc.args)

#Block else
print("Task 8======================================")
def play_note(note):
    print("Играю ноту "  + note)

try:
    note = get_note_name(4)
except ValueError:
    print("Значение не верно")
except TypeError:
    print("Тип аргумента неверный")
else:
    play_note(note)

#Block finally
print("Task 9======================================")
try:
    note = get_note_name(4)
except ValueError:
    print("Значение не верно")
except TypeError:
    print("Тип аргумента неверный")
else:
    play_note(note)
finally:
    print("Cделал все, что смог")

#NotImplementesError
print("Task 9======================================")
class AbstractAnimal:
    speceis = NotImplementedError

    def make_a_sound(self):
        raise NotImplementedError("Этот класс - абстрактный, используйте конкретную реализацию")

class Cat(AbstractAnimal):
    speceis = "Cat"

    def make_a_sound(self):
        print("Meowww!")

class Dog(AbstractAnimal):
    speceis = "Dog"

    def make_a_sound(self):
        print("Woof!")

print(AbstractAnimal().speceis)
# print(AbstractAnimal().make_a_sound()) #NotImplementedError: Этот класс - абстрактный, используйте конкретную реализацию
print(Cat().make_a_sound())
print(Dog().make_a_sound())

#Costum Exceptions
print("Task 10======================================")
class MyIndexError(IndexError):
    def __init__(self, *args, **kwargs):
        IndexError.__init__(self, *args, **kwargs)

# try:
#     raise IndexError("Выбрасываем IndexError") #IndexError: Выбрасываем IndexError
# except MyIndexError:
#     print("Поймали!")

try:
    raise MyIndexError("Выбрасываем IndexError")
except IndexError:
    print("Поймали!")
    
#Write in log
print("Task 11======================================")
def MyLoggingError(Exception):
    def __init__(self, message, *args):
        super(MyLoggingError, self).__init__("Вызываем конструктор базового класса исключения, но без входных аргументов")
        with open("21_exception_log.txt", "a++") as log:
            log.write(message + ":" + str(args))

for i in range(10):
    try:
        raise MyLoggingError("Сообщение об ошибке. Аргументы", i, "arg%d" % i)
    except MyLoggingError:
        print(a.args)

with open("21_exception_log.txt", "r") as f:
    print(f.read())

print("Task 12======================================")
class Booking:
    def __init__(self, room_name, start, end):
        if end<=start:
            raise ValueError("End tome must be after start time")
        
        self.room_name = room_name
        self._start = start
        self.end = end

    @property
    def duration(self):
        return int((self.end - self.start).total_seconds() // 60)
    
    @property
    def start_date(self):
        return self.start.strftime("%Y-%m-%d")
    
    @property
    def end_date(self):
        return self.end.strftime("%Y-%m-%d")

    @property
    def start_time(self):
        return self.start.strftime("%H:%M")
    
    @property
    def end_time(self):
        return self.end.strftime("%H:%M")
    
    @property
    def create_booking(room_name, start, end):
        print("Начинаем создание бронирования")
        try:
            booking = Booking(room_name, start, end)
            result = register_booking(booking)

            if result is True:
                msg = "Бронирование создано"
                created = True
            elif result is False:
                msg = "Комната занята"
                created = False
            else:
                raise ValueError("Unexpected result from registr_booking")
        except KeyError:
            msg = "Комната найдена"
            created = False
        except ValueError as ve:
            msg = str(ve)
            created = False
        finally:
            print("Заканчиваем создание бронирования")
        
        booking_data = {
            "room_name": room_name,
            "start_date": start.strftime("%Y-%m-%d"),
            "start_time": start.strftime("%H:%M"),
            "end_date": end.strftime("%Y-%m-%d"),
            "end_time": end.strftime("%H:%M"),
            "duration": int((end - start).total_seconds() // 60),
        }

        return json.dumps({
            "created": created,
            "msg": msg,
            "booking": booking_data,
        }, ensure_ascii=False, indent=2)



        
