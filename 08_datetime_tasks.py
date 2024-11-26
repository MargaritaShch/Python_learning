import datetime
#1. Class date
print("Task 1 ======================================")
yesterday  = datetime.date(2017, 5, 2)
print(yesterday)
today = datetime.date.today()
print(today)
print("{}.{}.{}".format(today.day, today.month, today.year))

print(today.weekday())

#2. Class time
print("Task 2 ======================================")
current_time = datetime.time()
print(current_time)

current_time = datetime.time(16, 25)
print(current_time)

current_time = datetime.time(16, 25, 45)
print(current_time)

#3. Class datetime
print("Task 3 ======================================")
deadline = datetime.datetime(2017, 5, 10)
print(deadline)

deadline = datetime.datetime(2017, 5, 10, 4, 30)
print(deadline)
# print("{}.{}.{} {}:{}".format(now.day, now.month, now.day, now.hour, now.minute))

#4. Class timedelta
print("Task 4 ======================================")
print(datetime.timedelta(hours=3, minutes=30))
print(datetime.timedelta(2))
#сложение и вычитиание
print('Дата и время через 2 дняб 3 часа и 30 минут: ')
date = datetime.datetime.now() + datetime.timedelta(days=2, hours=3, minutes=30)
print(date)
print('Дата и время через 10 дней, 5 часов назад от предыдудщей даты: ')
print(date - datetime.timedelta(days=10, hours=5))

now = datetime.datetime.now()
new_year = datetime.datetime(now.year+1,1,1)
period = new_year - now

print('До нового года осталось: {} дней {} секунд {} микросекунда'.format(period.days, period.seconds, period.microseconds))
print('Всего: {} секунд'.format(period.total_seconds))

#5. Преобразование из строки в дату и наоборот
print("Task 5 ======================================")
deadline = datetime.datetime.strptime('22/05/2017', '%d/%m/%Y')
print(deadline)

#6. Module time
print("Task 6 ======================================")
import time
print(time.gmtime(0))

#time.ctime
print(time.ctime())
print(time.ctime(1384112639))

#time.sleep
for x in range(5):
    time.sleep(2)
    print("Slept for 2 second")

#time.strftime
a = time.strftime('%Y-%m-%d %H.%M.%S', time.localtime())
print(a)

#time.time
x = time.time()
print(x)

#7. Task 7
print("Task 7 ======================================")
from datetime import datetime, timedelta
# С клавиатуры вводится дата в формате DD-MM-YYYY. Нужно вывести дату начала недели, к которой относится введенная дата (дата понедельника недели), в таком же формате. z
# Формат ввода
# 22-09-2022

# Формат вывода
# 19-09-2022
# Примечания
# Если введен понедельник - нужно вывести его же.
input_date = input()
date = datetime.strptime(input_date, '%d-%m-%Y')
monday = date - timedelta(days = date.weekday())
print(monday.strftime('%d-%m-%Y'))

#8. Task 8
print("Task 8 ======================================")
# Даты. Разница между датами
# Напишите программу, которая принимает на вход две строки:
# Первая дата в формате "ГГГГ-ММ-ДД".
# Вторая дата в формате "ГГГГ-ММ-ДД".
# Программа должна рассчитать количество полных лет между датами, и корректно отобразить результат, учитывая склонения (год, года, лет). Обе даты лежат в диапазоне с 1900 по 2024 год включительно. Вторая дата больше первой минимум на один год.
# Формат ввода
# 1990-01-01
# 1993-09-15
# Формат вывода
# 3 года
def get_year_word(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
        return "года"
    else:
        return "лет"
    
input_date1 = input()
input_date2 = input()

date1 = datetime.strptime(input_date1, "%Y-%m-%d")
date2 = datetime.strptime(input_date2, "%Y-%m-%d")

if date2 <= date1:
    print("Вторая дата должна быть больше первой минимум на год")
else:
    years_difference = date2.year - date1.year
    if (date2.month, date2.day) < (date1.month, date1.day):
        years_difference -= 1

    word = get_year_word(years_difference)
    print(f"{years_difference} {word}")

#8. Task 9
print("Task 9 ======================================")
days_ru = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

input_date = input()  
input_language = input() 

try:
    date = datetime.strptime(input_date, "%d-%m-%Y")
except ValueError:
    print("Некорректный формат даты")
    exit()

day_of_week = date.weekday()  


if input_language == "ru":
    print(f"День недели - {days_ru[day_of_week]}")
elif input_language == "en":
    print(f"Day of the week - {days_en[day_of_week]}")
else:
    print("Непонятный язык")
