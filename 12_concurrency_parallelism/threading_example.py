# without threading

# import time

# def task():
#     for i in range(1,3):
#         print(f"Working...{i}")
#         time.sleep(1)

# task()
# print("Done!")

# With Threading

import threading
import time

def task1():
    for i in range(3):
        print(f"Working...#{i}")
        time.sleep(1)

def task2():
    for i in range(3):
        print(f"Task 2 running...#{i}")
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both Tasks Done!")