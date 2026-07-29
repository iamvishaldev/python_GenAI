# def chai_customer():
#     print("Welcome ! What chai would you like?")
#     order = yield
#     while True:
#         print(f"Preparing: {order}")
#         order = yield

# stall = chai_customer()
# next(stall) #start generator

# stall.send("Masala Chai")

def hot_tea():
    yield "Masala"
    yield "Ginger"

def all_tea():
    yield from hot_tea()
    yield "Iced Lemon Tea"

for tea in all_tea():
    print("tea",tea)