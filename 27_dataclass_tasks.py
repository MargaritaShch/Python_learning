#Dataclass
from dataclasses import dataclass, make_dataclass
print("Task 1 ======================================")
@dataclass
class SomeThing:
    value1: int
    value2: int

s = SomeThing(1, "abc")
print(s.value1, s.value2)


# value3 = 5
# @dataclass
# class SomeThing:
#     value1: int
#     value2: int
#     value3

# s = SomeThing(1, "abc")
# print(s.value1, s.value2, s.value3)

#make_dataclass
print("Task 2 ======================================")

SomeThing = make_dataclass("SomeThing", ["value1", "value2"])
s = SomeThing(1,"abc")
print(s.value1, s.value2)

#default values
print("Task 3 ======================================")
@dataclass
class SomeThing:
    value1: int =1
    value2: int = "abc"

a = SomeThing(45)
b = SomeThing(value2="abdce")

print(b.value1, a.value2)
print(b.value1, a.value2)
print(SomeThing.value1)

#Frozen Data Class
print("Task 4 ======================================")
@dataclass(frozen=True)
class SomeThing:
    value1: int 
    value2: str

s = SomeThing(value1=256, value2="abc")
# s.value2 = "abcde" #dataclasses.FrozenInstanceError:
print(b.value1, a.value2)

#Frozen Data Class: eq, hash, order
print("Task 5 ======================================")
@dataclass(eq=True, order=True, unsafe_hash=True)
class SomeThing:
    value1: int 
    value2: str
