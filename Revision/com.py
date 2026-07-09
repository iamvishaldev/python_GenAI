# numbers = [1,2,3,4,5,6]

# square = [x*x for x in numbers]

# print("square",square)

# menu = [
#     "Masala Chai",
#     "Iced lemon tea",
#     "green tea",
#     "iced peach tea",
#     "ginger chai"
# ]

# iced = [tea for tea in menu if "iced" in tea.lower()]

# print(iced)

# users = [
#     {"name": "Vishal", "active": True},
#     {"name": "Rahul", "active": False},
#     {"name": "Aman", "active": True}
# ]

# active_user = [user for user in users if user['active']]
# print(active_user)

# """ Remove duplicates """

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique1 = {x*2 for x in numbers}
print("unique",unique1)

menus = [
    "Masala Chai",
     "Iced lemon tea",
     "green tea",
     "iced peach tea",
     "iced peach tea",
     "ginger chai"
]

unique2 = {
    user for user in menus
}

print("unique2",unique2)