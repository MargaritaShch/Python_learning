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

#Реализуйте функцию create_config(bot_id, bot_token, *commands), которая создает YAML-конфигурацию для бота, используя модуль yaml. Конфигурация должна содержать следующие данные:

# bot_id: Идентификатор бота (строка).
# bot_token: Токен доступа к боту (строка).
# commands: Одна или несколько команд, каждая из которых представлена словарем с ключами:
# description: Описание команды (строка).
# function: Имя функции, которая будет вызываться при выполнении команды (строка).
# Функция должна вернуть YAML-конфигурацию бота.

# Пример использования
# bot_id = "457"
# bot_token = "1249774028390"
# # Пример команд
# commands = [
#     ("Приветствие", "greet_user"),
#     ("Получить прогноз погоды", "get_weather")
# ]
print("Task 3 ======================================")
def create_config(bot_id, bot_token, *commands):
    config = {
        "bot_id": bot_id,
        "bot_token": bot_token,
        "commands": [{"description": description, "function": function} for description, function in commands]
    }
    yaml_config = yaml.dump(config, allow_unicode=True)
    return yaml_config