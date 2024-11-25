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

