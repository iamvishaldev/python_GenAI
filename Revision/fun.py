# def get_input():
#     print("Getting user input")

# def validate_input():
#     print("Validating the user input info")

# def save_to_db():
#     print("saved to db")

# def register_user():
#     get_input()
#     validate_input()
#     save_to_db()
#     print("Registration done")


# register_user()


# def calculate_bill(cups, price_per_cup):
#     return cups * price_per_cup

# order1 = calculate_bill(2,55)
# order2 = calculate_bill(2,40)

# print("order",order1)
# print("order",order2)

# without lambda code
# chai_types = ["light","kadak","ginger","kadak"]

# def is_kadak(chai):
#     return chai == "kadak"

# strong_chai = list(filter(is_kadak,chai_types))

# with lamda

# strong_chai = list(filter(lambda chai: chai == "kadak",chai_types))

# print(f"strong chai {strong_chai}")

# strong_chai = list(filter(lambda chai: chai=="kadak",chai_types))

users = [
    {"name": "Vishal", "active": True},
    {"name": "Rahul", "active": False},
]


isActive_User = list(filter(lambda user: user["active"],users))

print(f"Get the Active user {isActive_User}")