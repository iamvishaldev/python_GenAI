# concurrency

# threading.Thread
# asyncio

# parallelism

# multiprocessing.Process
# concurrent.future.ProcessPoolExecutor

# import threading
# import time

# def take_orders():
#     for i in range(1,4):
#         print(f"Taking order for #{i}")
#         time.sleep(1)

# def brew_chai():
#     for i in range(1,4):
#         print(f"Brewing chai for #{i}")
#         time.sleep(2)

# # creating threads
# order_thread = threading.Thread(target=take_orders)
# brew_thread = threading.Thread(target=brew_chai)

# order_thread.start()
# brew_thread.start()

# # wait for both to finish
# order_thread.join()
# brew_thread.join()

# print(f"All orders taken and chai brewed")

# import time

# def take_order():
#     for i in range(1,4):
#         print(f"Taking order for #{i}")
#         time.sleep(1)

# def brew_chai():
#     for i in range(1,4):
#         print(f"Brewing chai for #{i}")
#         time.sleep(2)

# start = time.time()

# print("start",start)

# take_order()
# brew_chai()

# end = time.time()

# print("Total time:", round(end - start, 2))

# import threading
# import time

# def task1():
#     time.sleep(2)
#     print("Task 1 done")

# def task2():
#     time.sleep(2)
#     print("Task 2 done")

# print("Start")

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("End")

# import threading
# import time

# def task1():
#     time.sleep(5)
#     print(f"Task 1 done")

# def task2():
#     time.sleep(5)
#     print(f"Task 2 done")

# print("Start")

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("End")

# 👉 One by one execution

# import time

# def task1():
#     time.sleep(2)
#     print("Task 1 done")

# def task2():
#     time.sleep(2)
#     print("Task 2 done")

# task1()
# task2()

# 🟢 WITH Threading

# import threading # create threads and run tasks together
# import time

# def task1():
#     time.sleep(2)
#     print("Task 1 done")

# def task2():
#     time.sleep(2)
#     print("Task 2 done")

# t1 = threading.Thread(target=task1) # Create a new thread (worker) that will run task1

# t2 = threading.Thread(target=task2) # Create a new thread (worker) that will run task2

# # ⚠️ Important:
# # 👉 At this point → nothing has started yet

# t1.start() # Start the thread and run task1
# t2.start() # Start the second thread and run task2
# print("End")
# # t1.join() # Wait until t1 finishes
# # t2.join() # Wait until t2 finishes
# print("Done")

# 🎯 Simple understanding

# 👉 join() = “ruk ja, kaam complete hone de”
# 👉 Without join = “mujhe farak nahi, main aage badh raha hoon”

# import time

# def task1():
#     print("Task 1 start")
#     time.sleep(2)
#     print("Task 1 end")

# def task2():
#     print("Task 2 start")
#     time.sleep(2)
#     print("Task 2 end")

# print("Start")

# task1()
# task2()

# import time
# import threading

# def task1():
#     print("Task 1 start")
#     time.sleep(2)
#     print("Task 1 end")

# def task2():
#     print("Task 2 start")
#     time.sleep(2)
#     print("Task 2 end")

# print("start")

# t1 = threading.Thread(target=task1) # create a new thread (worker) that will run task1
# t2 = threading.Thread(target=task2) # create a new thread (worker) that will run task2

# t1.start() # start the thread and run task1 
# t2.start() # start the thread and run task2

# t1.join() # wait until the task finishes
# t2.join() # wait until the task finishes

# print("End")

import threading
import time

def download_file():
    print(threading.current_thread().name)
    time.sleep(2)
    print(threading.current_thread().name)

thread1 = threading.Thread(target=download_file) # create a new thread (worker) that will run task download_file
thread2 = threading.Thread(target=download_file) # create a new thread (worker) that will run task download_file
thread3 = threading.Thread(target=download_file) # create a new thread (worker) that will run task download_file

thread1.start() # start the thread and run download_file
thread2.start() # start the thread and run download_file
thread3.start() # start the thread and run download_file

thread1.join() # wait until the task finish
thread2.join() # wait until the task finish
thread3.join() # wait until the task finish