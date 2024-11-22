#1. type
print("Task 1 ======================================")
#list
a = [1,2,3]
print(type(a))
#tuple
a = (1,2,3)
print(type(a))
#set
a = {1,2,3}
print(type(a))
#frozenest
b = frozenset([1,2,3])
print(type(b))
#dict
c = {1: 'a', 2: 'b', 3:'c'}
print(type(c))

#2. change type 
print("Task 2 ======================================")
my_tuple = ('a', 'b', 'a')

my_list = list(my_tuple)
my_set = set(my_tuple)
my_frozenest = frozenset(my_tuple)

print(my_list, my_frozenest,my_set)
