# import threading
# import time

# def brew_chai():
#     print(f"{threading.current_thread().name} started brewing....")
#     count =0
#     for _ in range(100_000_000):
#         count +=1
#     print(f"{threading.current_thread().name} finished brewing....")

# thread1 = threading.Thread(target=brew_chai,name="Barista-1")
# thread2 = threading.Thread(target=brew_chai,name="Barista-2")

# start = time.time()
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# end = time.time()

# print(f"total time taken: {end - start:.2f} seconds")


# What is Global Interpreter Lock (GIL)

# GIL = Python ka rule
# Ek time pe sirf 1 thread Python code run karega

# no threading

import threading

def task1():
    for _ in range(5):
        print("Task 1")

def task2():
    for _ in range(5):
        print("Task 2")

t1 = threading.Thread(target=task1)

t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()