import json
#кодирование основных объектов пайтон
print("Task 1 ======================================")
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.dumps( {'c':0, 'b':0,"a":0 }, sort_keys=True))

#компактное кодирование
print("Task 2 ======================================")
print(json.dumps([1,2,3, {'c':0, 'b':0,"a":0 }], separators=(',', ':')))

#красивый вывод
print("Task 3 ======================================")
print(json.dumps({'c':0, 'b':0,"a":0 },sort_keys=True, indent=4))

#декодирование
print("Task 4 ======================================")
print(type(json.loads('["foo", {"bar": ["baz", null, 1.0, 2]}]')))

#Задачи, аналогичные этой, часто встречаются в реальной веб-разработке. Будем получать и отдавать JSONы. К вам поступают данные в виде json-строки, в которых содержится список людей. Для каждого человека описаны различные его параметры, но вам нужно посчитать просто средний возраст всех людей из списка. Напишите функцию mean_age(json_string), которая принимает json строку, считает средний возраст людей из входных данных и возвращает новую json-строку в том формате, который указан ниже.

# Формат входной json-строки:
#     [
#         {
#             "name": "Петр",
#             "surname": "Петров",
#             "patronymic": "Васильевич",
#             "age": 23,
#             "occupation": "ойтишнек"
#         },
#         {
#             "name": "Василий",
#             "surname": "Васильев",
#             "patronymic": "Петрович",
#             "age": 24,
#             "occupation": "дворник"
#         }
#     ]
print("Task 5 ======================================")
def mean_age(json_string):
    my_dict = json.loads(json_string)
    ages = [person["age"] for person in my_dict]
    mean_age = sum(ages) / len(ages)
    result = json.dumps({"mean_age": round(mean_age, 2)})
    return result