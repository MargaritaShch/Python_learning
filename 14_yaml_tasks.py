import yaml
from pprint import pprint

print("Task 1 ======================================")
with open('example.yml', encoding='utf-8') as f:
    templates =yaml.safe_load(f)

pprint(templates)

print("Task 2 ======================================")
list_1 = [1, 2, 3, 4, 5, "hello", "world", True, False]
list_2 = [[10, 20, 30], ("a", "b", "c"), 42, 3.14, "example"]

to_yaml = {'list1': list_1, 'list2': list_2}

with open('example.yml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('example.yml') as f:
    print(f.read())