#Logging
import logging
print("Task 1 ======================================")
print(logging.basicConfig(level=logging.DEBUG))
print(logging.debug("Сообщение для отладки"))
print(logging.info("Сообщение обыкновенное информационнная"))
print(logging.warning("Предупреждение"))
print(logging.error("Ошибка"))
print(logging.critical("Полный крах"))

print("Task 2 ======================================")
print(logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# %(levelname) - 8s [%(asctime)s] %(message)s',
    level=logging.DEBUG
))
print(logging.debug("Сообщение для отладки"))
print(logging.info("Сообщение обыкновенное информационнная"))
print(logging.warning("Предупреждение"))
print(logging.error("Ошибка"))
print(logging.critical("Полный крах"))

#add to file
print("Task 3 ======================================")
print(logging.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# %(levelname) - 8s [%(asctime)s] %(message)s',
    level=logging.DEBUG,
    filename="log.txt",
    filemode="w"
))

print(logging.debug("Сообщение для отладки"))
print(logging.info("Сообщение обыкновенное информационнная"))
print(logging.warning("Предупреждение"))
print(logging.error("Ошибка"))
print(logging.critical("Полный крах"))

with open("log.txt") as f:
    print(f.read())

#few loggers
print("Task 4 ======================================")
logger = logging.getLogger("our_app_name")
print(logger.setLevel(logging.DEBUG))

handler = logging.FileHandler("our_app_log.txt", 'a', "utf-8")
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname) - 8s [%(asctime)s] %(message)s")

handler.setFormatter(formatter)
print(logger.addHandler(handler))

handler2 = logging.FileHandler("our_app_log2.txt", 'a', "utf-8")
handler2.setFormatter(formatter)

print(logger.addHandler(handler2))
print(logger.info("Наш новый логгер работает"))

with open("our_app_log.txt", encoding="utf-8") as f:
    print(f.read())

print(logger.handlers)
print(handler.close())
print(handler2.close())