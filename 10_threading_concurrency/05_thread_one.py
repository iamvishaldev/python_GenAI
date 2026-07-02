# without threading
# import time

# def task1():
#     print("Task 1 start")
#     time.sleep(2)
#     print("Task 1 end")

# def task2():
#     print("Task 2 start")
#     time.sleep(2)
#     print("Task 2 end")

# task1()
# task2()

# Total = 4 sec
# One by one execution

# with threading

# import threading
# import time

# def task1():
#     print("Task 1 start")
#     time.sleep(2)
#     print("Task 1 end")

# def task2():
#     print("Task 2 start")
#     time.sleep(2)
#     print("Task 2 end")

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
