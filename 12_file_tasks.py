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