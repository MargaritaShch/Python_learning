import logging
import time
import threading
import concurrent.futures as cf
import asyncio

# #однопоточная программа
# print("Task 1======================================")
# logger_format = '%(asctime)s:%(threadName)s:%(message)s'
# logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")

# def delay(delay, message):
#     logging.info(f"{message} received")
#     time.sleep(delay)
#     logging.info(f"Printing {message}")
#     return message

# def main():
#     logging.info("Main startded")
#     delay(2, "TWO SECONDS DELAY")
#     delay(3, "THREE SECONDS DELAY")
#     logging.info("Main ended")

# print(main())

# #thrading
# print("Task 2======================================")

# def main():
#     logging.info("Main startded")
#     threads = [
#         threading.Thread(target=delay, args=(3, "THREE SECONDS DELAY")),
#         threading.Thread(target=delay, args=(2, "TWO SECONDS DELAY")),
#     ]
#     for thread in threads:
#         thread.start()
#     logging.info("А тут мы видим, что главный поток тоже продолжает исполняться")
#     for thread in threads:
#         thread.join()
#     logging.info("Main ended")

# print(main())

# #футуры
# print("Task 3======================================")

# def main():
#     with cf.ThreadPoolExecutor(max_workers=2) as executor:
#         future_to_mapping = {
#             executor.submit(delay,3, "THREE SECONDS DELAY"): "3 secs",
#             executor.submit(delay,2, "TWO SECONDS DELAY"): "2 secs",
#             executor.submit(delay,4, "FOUR SECONDS DELAY"): "4 secs"
#         }
#         for future in cf.as_completed(future_to_mapping):
#             logging.info(f"{future.result()} Done")

# print(main())

#корутины
print("Task 4======================================")

def grep(pattern):
    print("Serching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("coroutine")
print("grep:", type(grep))
print("search:", type(search))
print()

next(search)
search.send("I love you")
search.send("Don't ypu love me?")
search.send("I love cotoutine instead")
search.close()

# #asyncio
# print("Task 5======================================")

async def delay_message(delay, message):
    logging.info(f"{message} received")
    await asyncio.sleep(delay)
    logging.info(f"Printing {message}")

# print(type(delay_message))
# print(type(delay_message(2, "TWO SECONDS AWAIT"))) 
# <class 'function'>
# C:\Users\user\Desktop\Projects\Python Start\28_async_tasks.py:89: RuntimeWarning: coroutine 'delay_message' was never awaited      
#   print(type(delay_message(2, "TWO SECONDS DELAY")))
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# <class 'coroutine'>

# print("Task 6======================================")

# async def main():
#     logging.info("Main startes")
#     logging.info(f"Текущие зарегистрированные залания: {len(asyncio.all_tasks())}")
#     logging.info("Создадим задания")
#     task_1 = asyncio.create_task(delay_message(2, "TWO SECONDS DELAY"))
#     task_2 = asyncio.create_task(delay_message(3, "THREE SECONDS DELAY"))
#     logging.info(f"Текущие зарегитрированные значения: {len(asyncio.all_tasks())}")
#     await task_1
#     await task_2
#     logging.info("Main Ended")

# # await main()
# print(asyncio.run(main()))
# print(main())

# # asyncio.gather
# print("Task 7======================================")
# async def main():
#     logging.info("Main startded")
#     logging.info("Создаем несколько заданий с помощью asyncio.gather")
#     await asyncio.gather(*[delay_message(i, f"WAITING {i} SECONDS") for i in range(6, 0, -1)])
#     logging.info("Main ended")

# print(asyncio.run(main()))
# print(main())

# # блокировка ресурсов
# print("Task 8======================================")

# async def delay_message(delay, message):
#     logging.info(f"{message} received")
#     if '6' not in message:
#         await asyncio.sleep(delay)
#     else:
#         time.sleep(delay)
#     logging.info(f"Printing {message}")

# async def main():
#     logging.info("Main startded")
#     logging.info("Создаем несколько заданий с помощью asyncio.gather")
#     await asyncio.gather(*[delay_message(i, f"WAITING {i} SECONDS") for i in range(10, 0, -1)])
#     logging.info("Main ended")

# # asyncio.run(main)

# # блокировка потоков
# print("Task 9======================================")
# LOCK = threading.Lock()
# class DbUpdate:
#     def __init__(self):
#         self.value = 0

#     def update(self):
#         logging.info("Update Started")
#         logging.info("Sleeping")
#         time.sleep(2)
#         with LOCK:
#             logging.info(f"Readinf Value From Db: {self.value}")
#             tmp = self.value +1
#             logging.info("Updating Value")
#             self.value = tmp
#             logging.info("Update Finished")

# db = DbUpdate()
# with cf.ThreadPoolExecutor(max_workers=5) as executor:
#     updates = [executor.submit(db.update) for _ in range(2)]
# print(logging.info(f"Final value is {db.value}"))


# print("Task 10======================================")
# class DbUpdate:
#     def __init__(self):
#         self.value = 0

#     async def update(self):
#         logging.info("Update Started")
#         logging.info("Sleeping")
#         await asyncio.sleep(2)
#         logging.info(f"Readinf Value From Db: {self.value}")
#         tmp = self.value +1
#         logging.info("Updating Value")
#         self.value = tmp
#         logging.info("Update Finished")

# async def main(): 
#     db = DbUpdate()
#     await asyncio.gather(*[db.update() for _ in range(2)])
                         
# await main()

#deadlock
print("Task 11======================================")
async def foo():
    await boo()

async def boo():
    await foo()

async def main():
    await asyncio.gather(*[foo(), boo()])

# print("Task 12======================================")
# async def main():
#     print(f"{time.ctime()} Hello!")
#     await asyncio.sleep(1.0)
#     print(f"{time.ctime()} Goodbye!")

# def get_or_create_loop():
#     loop = asyncio.get_event_loop()
#     if loop.is_closed():
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#     return loop

# loop = get_or_create_loop()
# print("Createa loop")
# loop.create_task(main())
# print("Created task main and now run loop")
# loop.run_forever()
# pending = asyncio.all_tasks(loop=loop)
# group = asyncio.gather(*pending, return_exceptions = True)
# print("Gatheres tasks")
# loop.run_until_complete(group)
# print(loop.close())

# asyncio.run(main())

# print("Task 13======================================")
# async def main():
#     print(f"{time.ctime()} Hello!")
#     await asyncio.sleep(5)
#     print(f"{time.ctime()} Goodbye!")

# def blocking():
#     print("blocking started")
#     time.sleep(3)
#     print(f"{time.ctime()} Hello from a thread")

# loop = asyncio.new_event_loop()
# # asyncio.set_event_loop()

# loop.create_task(main())
# loop.run_in_executor(None, blocking)
# loop.run_forever()

# pending = asyncio.all_tasks(loop=loop)
# group = asyncio.gather(*pending)
# loop.run_until_complete(group)
# loop.close()

#корутины
print("Task 14======================================")
def x():
    yield 1
print(x())

#корутины
print("Task 15======================================")
async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(5)
    print(f"{time.ctime()} Goodbye!")


#корутины
print("Task 16======================================")
async def f():
    return "abc"

coroutine = f()
try:
    coroutine.send(None)
except StopIteration as e:
    print(e.value)

