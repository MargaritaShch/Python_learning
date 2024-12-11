from collections import Counter
# #Открыть файл
# print("Task 1 ======================================")
# f = open('text.txt', 'r')
# print(f)
# f.close()

# # with open('text.txt', 'r', encoding='utf-8') as f:
# #     print(f.read(2))
# #     f.seek(0) # Возвращаем указатель в начало файла
# #     print(f.read())
# #     f.close()

# #чтение построчно в цикле for
# print("Task 2 ======================================")
# f = open('text.txt', 'r')
# for line in f:
#     print(line, end="")
# f.close()

#запись файла
print("Task 3 ======================================")
f = open('text.txt', 'w')
f.write('This is brand new file')
f.write('New line of drand new life.\n')
f.close()

#with
print("Task 4 ======================================")
with open('text.txt') as f:
    for line in f:
        print(line)

# Напишите функцию get_popular_name_from_file(filename), которая считывает файл, в котором в каждой строке записаны имя и фамилия через пробел. filename - это имя файла, в котором записаны эти имена. Вам нужно вернуть строку - самое популярное имя в файле. Если таких имен несколько, они должны быть перечислены через запятую внутри строки в алфавитном порядке.
print("Task 5 ======================================")
def get_popular_name_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        names = [line.split(' ')[0] for line in lines]
        name_count = Counter(names)
        max_count = max(name_count.values())
        popular_name = [name for name, count in name_count.items() if count == max_count]
        return ', '.join(sorted(popular_name))
       

