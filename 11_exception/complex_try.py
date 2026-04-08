# def serve_chai(flavor):
#     try:
#         print(f"Preparing {flavor} chai...")
#         if flavor == "unknown":
#             raise ValueError("We don't know that flavor")
#     except ValueError as e:
#         print("Error: ",e)
#     else:
#         print(f"{flavor} chai is served")
#     finally:
#         print("Next customer please")

# serve_chai("masala")

# def test():
#     try:
#         x = int("abc")
#         print("A")
#     except ValueError as e:
#          print("Error: ",e)
#          print("B")
#     else:
#         print("C")
#     finally:
#         print("D")

# test()

# Multiple exception

# def process_order(item,quantity):
#     try:
#         price = {"masala":20}[item]
#         cost = price * quantity
#         print(f"total cost is {cost}")
#     except KeyError:
#         print("Sorry that chai is not on menu")
#     except TypeError:
#         print("Quanity must be in number")

# # process_order("ginger",2)
# process_order("masala",10)

# custom exceptions

# def brew_chai(flavor):
#     if flavor not in ["masala", "ginger", "elaichi"]:
#         raise ValueError("Unsupported chai flavor...")
#     print(f"brewing {flavor} chai...")

# brew_chai("masala")

# class OutOfIngredientsError(Exception):
#     pass

# def make_chai(milk,sugar):
#     if milk ==0 or sugar == 0:
#         raise OutOfIngredientsError("Missing milk or sugar")
#     print("Chai is ready...")

# make_chai(0,1)

class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":10,"ginger":30,"lemon":15}
    try:
        if not isinstance(cups,int):
            raise TypeError("Number of cupes must be an integer")
        
        if cups <=0:
            raise InvalidChaiError("Cups should not be in negative numbers")
        
        if flavor not in menu:
            raise InvalidChaiError(f"This chai {flavor} is not present in the menu....")
        
        price = menu[flavor]
        total = price * cups
        print("total",total)

        #discount logic 
        discount_amount = 0
        if cups > 5:
            discount_amount = total * 0.05
            print("discount_amount",discount_amount)
            total -= discount_amount
        print(f"Total bill: {total}")
        print(f"Discount: {discount_amount}")

    except Exception as e:
        print(f"Error : {e}")
    finally:
        print("Thanks for ordering the chai...!")

c = bill("masala",10)


