# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         star
        
#         t = time.time()
        
#         func(*args, **kwargs)
        
#         end = time.time()
#         print(f"Time taken: {end - start:.5f} seconds")
    
#     return wrapper

# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Work done")

# slow_function()

# def outer():
#     def inner():
#         print("Hello inner")
#     return inner

# f = outer()

# f()

# Pass function as argument

# def greet():
#     print("Hello")

# def call_fun(fun):
#     fun()

# call_fun(greet)

# # Decorator

# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
    
#     return wrapper

# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")

#     return wrapper

# def chai():
#     print("Ginger tea")

# chai()


def add_masala(type):
    def decorator(func):
        def wrapper():
            print(f"Making {type} chai")
            func()
        return wrapper
    return decorator

@add_masala("strong")
def chai():
    print("Ginger Chai")

chai()