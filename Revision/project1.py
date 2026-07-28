# kettle_boiled = True

# if kettle_boiled:
#     print(f"kettle is boiled {kettle_boiled} make the chai")
# else:
#     print("Wait till it boilied")

# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa,it confirms the order.
# Otherwise,it says it's not available

# snack = input("Enter your preferred snack:")

# if snack == "cookies" or snack == "samosa":

#     print(f"user said: {snack}")
# else:
#     print(f"Not avaible")

# cup_size = input("What cupsize you want..").lower()

# if cup_size == "small":
#     print("10 rupiess")
# elif cup_size == "medium":
#     print("15")
# elif cup_size == "large":
#     print("20")
# else:
#     print("Unkown cup size")

# device_status = "unactive"
# temp = int(input("What is the temp..."))

# if device_status == "active":
#     print("Device is active")

#     if temp>35:
#         print("High temperature alert!")
#     else:
#         print("Temperature is normal")
        
# else:
#     print("Device is inactive")


# account_status = "active"
# withdraw_amount = int(input("Enter withdraw amount..."))
# balance_amount = 1000

# if account_status == "active":
#     print("Account is active...")

#     if withdraw_amount > balance_amount:
#         print("Insufficient balance")
#     else:
#         print("withdrawal successful")

# else:
#     print("Account is inactive")


# order_amount = int(input("Order Amount: "))
# delivery_fee = 0 if order_amount > 300 else 30
# print(f"billing details with delivery fee {delivery_fee}")

seat_type = input("what is your seat type...").lower()

match seat_type:
    case "sleeper":
        print("your seat type is sleeper")
    case "ac":
        print("your seat type is ac")
    case "general":
        print("your seat is general")
    case "luxury":
        print("your seat is luxury")
    case _:
        print("unknown")