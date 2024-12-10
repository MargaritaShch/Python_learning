import re
#re.mathc(pattern, string)
print("Task 1 ======================================")
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result) #<re.Match object; span=(0, 2), match='AV'>
print(result.group())#group() выводит весь паттерн

result = re.match(r'AV(.{3})', 'AV Analytics Vidhya AV')
print(result.group())
print(result.group(1))

print(result.start())
print(result.end())

#re.search(pattern, string)
print("Task 2 ======================================")
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result)
print(result.group())

#re.search(pattern, string)
print("Task 3 ======================================")
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print(result)

#re.findall(pattern, string)
print("Task 4 ======================================")
result = re.findall(r'Analytics', 'AV Analytics Vidhya AV')
print(result)

#re.split(pattern, string, [maxsplit =0])
print("Task 5 ======================================")
result = re.split(r'y', 'Analytics')
print(result)

result = re.split(r'i', 'Analytics Vidhya')
print(result)

result = re.split(r'i', 'Analytics Vidhya', maxsplit =1)
print(result)

#re.sub(pattern, repl, string)
print("Task 6 ======================================")
result = re.sub(r'India', 'the World', 'AV is largest Analustics community of India')
print(result)

#re.complile(pattern, repl, string)
print("Task 6 ======================================")
pattern = re.compile("AV")
result = pattern.findall('AV Analystics Vidhaya AV')
print(result)
result2 = pattern.findall('AV is largest Analustics community of India')
print(result2)

#rПроверить телефонный номер(номер должен быть длинной 11 знаков и начинаться с 7 или 8)
print("Task 7 ======================================")
li = ['89999999999','79979799999', 'email@email@.com', '7999', '8999999-999', '799999x9999']
for val in li:
    if re.match(r'[78][0-9]{9}', val):
        print(val, 'yes', sep="\t")
    else:
       print(val, 'no', sep="\t") 

#пример с группирующим скобками
print("Task 8 ======================================")
pattern = r'\s*([А-Яя-яЁё]+)(\d+)\s*'
string = r'---   Опять45   ---'
match = re.search(pattern,string)

if match: 
    print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
else:
    print("Совпадение не найдено")

#использование групп при заменах
print("Task 8 ======================================")
def repl(m):
    return '>censored(' + str(len(m[0])) + ')<'
text = "Некоторые хорошие слова подозрительны: хор, хоровод, хороводоведы."
print(re.sub(r'\b[хХхХ]\w*', repl, text))