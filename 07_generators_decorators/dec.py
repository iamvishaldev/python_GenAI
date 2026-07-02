# def my_dec(fun):
#     def wrapper():
#         print("Before function runs")
#         fun()
#         print("After function runs")
#     return wrapper

# @my_dec
# def greet():
#     print("Hello dec")

# greet()

def greet():
    print("Hello Vishal")

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

greeting = my_decorator(greet)

greeting()

# Logging Decorator

from functools import wraps