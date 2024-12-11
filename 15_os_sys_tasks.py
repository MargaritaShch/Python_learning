import os
import sys
import pickle

print("Task 1 ======================================")
print(os.name)
#Текущая директория
print(os.getcwd)
#переменные пользовательской среды
print(os.environ)

print("Task 2 ======================================")
print(sys.path)
print(sys.platform)
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)

print("Task 3 ======================================")
data = {
    'a': [1,2.0, 3, 4+6],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data_new = pickle.load(f)
print(data_new)
