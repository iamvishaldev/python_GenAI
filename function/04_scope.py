# 🧠 Core Idea (Golden Rule)

# 👉 Python variables are just “labels” pointing to objects in memory

# NOT boxes. NOT containers.
# 🟢 1. Assigning a New Value
# x = 10
# x = 11

# print("x",id(x))
# print("x",id(x))

# 🟡 2. Assigning One Variable to Another
# 👉 No new object created

# x=12
# y=x

# print("y",y,"x",x)
# print(id(x), id(y)) # Same memory address

# 🔴 3. Mutable Objects (IMPORTANT ⚡)

# x = [1,2,3]
# y =x

# y.append(4)

# print(x)

# 👉 Why?
# Because both point to SAME object

# x ──┐
#     ├──> [1, 2, 3, 4]
# y ──┘

# 🔵 4. Immutable Objects

# x = 10
# y = x

# y = y + 5

# print(id(x))
# print(id(y))

# 🚀 Python Scope Rule → LEGB
# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# 1️⃣ Local Scope (Inside function)

# def test():
#     x = 10
#     print(x)

# test()

# 2️⃣ Enclosing Scope (Nested functions)

# def outer():
#     x = "chai"

#     def inner():
#         x = "coffee" #Assignment = new local variable
#         print(x)
#     inner()
# outer()



# def serve_chai():
#     chai_type = "Masala"
#     print(f"Inside function {chai_type}")

# chai_type = "Lemon"
# serve_chai()
# print(f"Outside function: {chai_type}") 

# # Local variables

# def calculate_price():
#     price = 100
#     tax = price * 0.1
#     print(f"Total: {price + tax}")

# calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined

# Global variables

# discount_rate = 0.15

# def apply_discount(price):
#     discount = price * discount_rate
#     return price - discount

# result = apply_discount(100)
# print(f"res :{result}")

# def chai_counter():
#     chai_order = "lemon"
#     def print_order():
#         chai_order = "Ginger"
#         print("Inner :", chai_order)
#     print_order()
#     print("Outer: ", chai_order)

# chai_counter()

# counter = 0

# def increment():
#     global counter
#     counter +=1

# increment()
# increment()
# print(counter)

# def chai_counter():
#     chai_order = "lemon"

#     def print_order():
#         chai_order = "Ginger"
#         print(f"Inner :{chai_order}")
#     print_order()
#     print(f"outer scope :{chai_order}")
# chai_counter()

# non local vs global local

# def colud_kitchen():
#     order_name = "pav bhaji"
#     def order_recipe():
#         nonlocal order_name
#         # order_name = "Pizza"
#     order_recipe()
#     print(f"Your dish is ready {order_name} !!")

# colud_kitchen()

# Basic

# def add(a,b):
#     return a+b
# result=add(5,10)
# print(f"total : {result}")

# def greet(): #non input, no return
#     print("Hello")
# greet()

# def bread(type): #input, no return
#     print(f"bread type : {type}")
# bread("no maida")

# def cal_bread_rate(a,b): # input , return
#     return print(f"total cost of bread with vagies : {a+b}")
# cal_bread_rate(10,5)

#Function calling another Function
# Build a snadwich total bill with discount

# def discount(price):
#     if price>100:
#         return price * 0.9
#     return price

# def final_bill(qty,price):
#     total = qty * price
#     return discount(total)

# print(f"Total price of sandwich is with disount : {final_bill(5,35)}")

# ⚔️ Challenge 2 (Important)

# Modify discount():

# Rules:

# 200 → 20% discount

# 100 → 10% discount

# else → no discount

# def discount(price):
#     if price>=200:
#         return price * 0.20
#     elif price>=100:
#         return price * 0.10
#     else:
#         return price
    
# def final_bill(qty,amt):
#         total = qty * amt
#         return discount(total)

# print(f"Your Final discount is : {final_bill(6,99)}")

# non local vs global scope

# def update_order():
#    chai_type = "Elaichi"
#    def kitchen():
#     #   nonlocal chai_type
#       chai_type = "Kesar"
#    print(f"1Chai type: {chai_type}")

#    kitchen()
#    print(f"Chai type: {chai_type}")
# update_order()

# x = [1, 2]

# def modify(lst):
#     lst = [9, 9] 

# modify(x)

# print(x)

# x = "chai"

# def test():
#     print(x)
#     x = "coffee"

# test()

# def update_order():
#    chai_type = "Elaichi" #LOCAL
#    def kitchen():
#       global chai_type
#       chai_type = "Kesar"
#    print(f"1Chai type: {chai_type}")

#    kitchen()
#    print(f"Chai type: {chai_type}")
# update_order()
# chai_type="Plain"

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type = "Irani"
#     kitchen()

# front_desk()
# print(f"Final global chai : {chai_type}")

x = [1]

def outer():
    x = [2]

    def inner():
        nonlocal x
        x.append(3)

        def deep():
            global x
            x = [4]

        deep()
        x.append(5)

    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)