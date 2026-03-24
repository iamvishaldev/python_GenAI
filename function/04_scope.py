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

def discount(price):
    if price>100:
        return price * 0.9
    return price

def final_bill(qty,price):
    total = qty * price
    return discount(total)

print(f"Total price of sandwich is with disount : {final_bill(5,35)}")