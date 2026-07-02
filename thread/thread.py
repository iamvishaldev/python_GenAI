# normal function :  direactly function call ho raha hai
# def greet(name):
#     print(f"Hello {name}")

# greet("Vishal")

# Thread ke saath

# import threading

# def greet(name):
#     print(f"Hello {name}")

# t =  threading.Thread(
#     target=greet,
#     args=("Vishal",)
# )

# t.start()

# multiple arguments

# import threading

# def add(a,b):
#     print(a + b)

# t = threading.Thread(target=add,args=(10,20))

# t.start()

# import threading

# def greet(name):
#     print(type(name))

# t = threading.Thread(target=greet,args=("Vishal",))

# t.start()

# name = ("Vishal","Rahul")

# print(type(name))

# names = ("Vishal",)

# print(type(names))

# import threading
# import time

# def greet(name,age):
#     print(f"Name",name)
#     print(f"age",age)

# t = threading.Thread(
#     target=greet,
#     args=("Vishal",29,)
# )

# t.start()
# t.join()

# import threading
# import time

# def task():
#     time.sleep(3)
#     print("Task finished")

# t = threading.Thread(target=task)

# t.start()
# t.join()

# print("Main thread finished")

# Multithreading- Multiple threads sharing the same memory space

# from threading import Thread
# import time

# def task(name):
#     print(f"Starting task {name}")
#     time.sleep(2)
#     print(f"Completed task {name}")

# start = time.time()

# t1 = Thread(target=task,args=("Task-1",))
# t2 = Thread(target=task,args=("Task-2",))

# # start both the thread
# t1.start()
# t2.start()
# # dono thread ak sath start ho gaye concurrently

# # wait for both to finish
# t1.join()
# t2.join()

# end = time.time()

# print(f"Total time: {end - start:.2f}")

# Download simulation using thread

# from threading import Thread
# import time

# def download_file(file_number):
#     print(f"Downloading File-{file_number}...")
#     time.sleep(1)
#     print(f"File-{file_number} download complete!")

# start = time.time()

# # Create multiple threads

# threads: list[Thread] = []
# for i in range(1,6):
#     thread = Thread(target=download_file,args=(i,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# end = time.time()

# print(f"All download finished in {end - start:.2f} seconds")