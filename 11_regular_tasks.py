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

#Написать функцию, которая на вход принимает строку, а на выход выдает булево значение (True или False), которое истинно, если полученная строка соответствует российскому номеру телефона или адресу электронной почты.

# Сигнатура функции:

# check_string(string) -> bool

# Пример использования
# check_string("+7-916-000-00-00")  # должна вернуть True
 
# Приечания
# Допустимые форматы телефонов. Код страны - всегда либо 7, либо 8, либо +7, либо опущен; код оператора может быть любой:
# 89160000000
# +79160000000
# 9160000000
# 8(916)000-00-00
# +7(916)000-00-00
# (916)000-00-00
# 8 (916) 000-00-00
# +7 (916) 000-00-00
# (916) 000-00-00
# 8(916)0000000
# +7(916)0000000
# (916)0000000
# 8-916-000-00-00
# +7-916-000-00-00
# 916-000-00-00

# Валидным адресом электронной почты будем считать строки, содержащие @ и не меньше одной точки (после точки - не меньше двух символов), например:
# abc@abc.ab
# abc@abc.ab.ab
# a@ab.ab
# abc.abc@abc.abc

# Невалидные адреса:
# @abc.abc
# abc@abc
# abc@abc.a
# abc@abc.abc.a
# abc@abc.
# abc@abc@abc
print("Task 9 ======================================")
def check_string(string):
    pattern_mobile = r'^(8|\+7|7)?[-\s]?\(?\d{3}\)?[-\s]?\d{3}[- ]?\d{2}[- ]?\d{2}$'
    pattern_address = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern_mobile, string):
        return True
    elif re.match(pattern_address, string):
        return True
    else:
        return False

print(check_string("+7-916-000-00-00"))  
print(check_string("abc@abc.ab"))        
print(check_string("abc@abc"))           
print(check_string("79991234567"))       
print(check_string("+7 (916) 123-45-67"))
print(check_string("12345"))            