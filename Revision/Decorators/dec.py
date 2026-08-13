# A decorator in python is a function 
# that takes another function add extra functionality to it 
# and return the modified function without changinng the original function's code

# def my_decorator(func):

#   def wrapper():
#     print("Before function run")
#     func()
#     print("After function run")

#   return wrapper

# @my_decorator
# def greet():
#   print("hello")

# greet()

# print(greet.__name__)

from functools import wraps

def my_decorator(func):

  @wraps(func)
  def wrapper():
        print("Before")
        func()
        print("After")

  return wrapper