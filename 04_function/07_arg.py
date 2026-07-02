"""
🚀 Python Day 9 Notes
Topic: Functions, Arguments, Lambda, Pure vs Impure, Built-in Functions
"""

# =========================================
# 🧠 1. Handling Arguments in Functions
# =========================================

# 🔹 Normal Arguments
def add(a, b):
    return a + b

# Example:
# print(add(2, 5))


# 🔹 Default Arguments
def greet(name="Vishal"):
    return f"Hello {name}"

# Example:
# print(greet())
# print(greet("Ram"))


# 🔹 *args (Multiple Positional Arguments)
def total(*numbers):
    return sum(numbers)

# Example:
# print(total(10, 20, 30, 40))


# 🔹 Print tuple from args
def show_numbers(*args):
    print(args)

# Example:
# show_numbers(1, 2, 3)


# 🔹 Multiply using *args
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Example:
# print(multiply(1, 2, 3))


# 🔹 Sum using *args
def sum_numbers(*args):
    return sum(args)

# Example:
# print(sum_numbers(1, 2, 3))


# 🔹 **kwargs (Keyword Arguments)
def user(**data):
    print(data)

# Example:
# user(name="Vishal", age=25)


# 🔹 Access specific value
def show_user_name(**data):
    print(data["name"])

# Example:
# show_user_name(name="Vishal", age=25)


# 🔹 Loop through kwargs
def show_user_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Example:
# show_user_details(name="Vishal", age=25)


# 🔹 Combine *args and **kwargs
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Example:
# demo(1, 2, name="Vishal")


# 🔹 Return number of args
def user_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    return len(args)

# Example:
# result = user_info(10, 20, 30, name="Vishal", age=25)
# print("Number of args:", result)


# =========================================
# 🧠 2. Multiple Return
# =========================================

def calc(a, b):
    return a + b, a - b

# Example:
# print(calc(5, 2))


def stats(numbers):
    if len(numbers) == 0:
        return 0, 0, 0

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return total, count, average

# Example:
# print(stats([10, 20, 30]))


# =========================================
# 🧠 3. Lambda Functions
# =========================================

# 🔹 Basic lambda
add_lambda = lambda a, b: a + b

# Example:
# print(add_lambda(2, 3))


# 🔹 Square using map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))

# Example:
# print(squared)


# 🔹 Uppercase characters
name = "Vishal"
upper_chars = list(map(lambda x: x.upper(), name))

# Example:
# print(upper_chars)


# 🔹 Multiply two lists
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

multiplied = list(map(lambda a, b: a * b, list1, list2))

# Example:
# print(multiplied)


# =========================================
# 🧠 4. Pure vs Impure Functions
# =========================================

# ✅ Pure Function
def square(n):
    return n * n

# Example:
# print(square(2))


# ❌ Impure Function (uses global variable)
x = 10

def add_with_global(a):
    return a + x

# Example:
# print(add_with_global(5))


# =========================================
# 🧠 5. Built-in Functions
# =========================================

# Length
# print(len([1, 2, 3]))

# Sum
# print(sum([1, 2, 3]))

# Max
# print(max([1, 2, 3]))

# Min
# print(min([1, 2, 3]))


# 🔹 Type Conversion
# print(int("10"))
# print(str(10))
# print(float(5))


# =========================================
# 🔥 Key Takeaways
# =========================================

"""
*args → multiple values (tuple)
**kwargs → key-value (dict)

return → gives value
print → only shows

lambda → one-line function

pure → no side effects
impure → depends on external

built-in → ready-made functions
"""