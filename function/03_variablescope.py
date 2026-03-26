
# Local

# def calculate_price():
#     price=100
#     tax = price *0.1
#     print(f"Total: {price  + tax}")

# calculate_price()


# print(price)

# Global

discount_rate = 0.15

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

result = apply_discount(100)

print(result)

counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2