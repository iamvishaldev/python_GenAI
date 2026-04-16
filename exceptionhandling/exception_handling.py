# Mini Project

# class InvalidChaiError(Exception): pass

# def bill(flavor, cups):
#     menu = {"masala": 20, "ginger":40}
#     try:
#         if flavor not in menu:
#             raise InvalidChaiError("that chai is not available")
#         if not isinstance(cups,int):
#             raise TypeError("Number of cups must be an integer")
#         total = menu[flavor] * cups
#     except Exception as e:
#         print("Error: ", e)
#     finally:
#         print("Thank you for visiting chaicode!")

# bill("mint",2)
# bill("masala","three")
# bill("ginger","three")

# 👉 Task:

# Create a function:
# - Takes flavor and cups
# - Has menu dict
# - Raise error if flavor not present
# - Raise error if cups not int
# - Print total bill

class InvalidChaiError(Exception): pass

def  bill(flavour,cups):
    menu = {"masala":20, "ginger":40, "elaichi":30}
    try:
        if cups < 0:
            raise TypeError("Cups must be positive")
        
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be integer")
        
        if flavour not in menu:
            raise InvalidChaiError("that chai is not avaible")

        if cups>=5:
            discount_rate = 10
            discount = discount_rate/100
        total = menu[flavour] * discount
        print("total bill",total)
    except Exception as e:
        print("Error :",e)
    finally:
        print("Thank you for visiting chaicode!")

bill("masala",10)