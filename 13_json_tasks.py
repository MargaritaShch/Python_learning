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