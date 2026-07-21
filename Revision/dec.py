# def my_decorator(func):

#   def wrapper():
#     print("Before function runs")
#     func()
#     print("After function runs")
#   return wrapper

# @my_decorator
# def greet():
#   print("Hello from decorators class from chaicode")

# greet()
# print(greet.__name__)

# logged_in = True

# def login_required(func):
  
#   def wrapper():

#         print("🔍 Checking authentication...")

#         if not logged_in:
#             print("❌ Unauthorized")
#             return
    
#         func()

#   return wrapper

# @login_required 
# def get_products():
#     print("📦 Fetching Products")

# # It secretly converts it to:

# # def get_products():
# #     print("📦 Fetching Products")

# # get_products = login_required(get_products)


# @login_required
# def get_orders():
#     print("🛒 Fetching Orders")


# @login_required
# def get_profile():
#     print("👤 Fetching Profile")


# get_products()
# print("----------------")
# get_orders()
# print("----------------")
# get_profile()

def login_required(func):

    def wrapper():
        print("🔍 Checking Authentication...")

        func()

    return wrapper


def get_products():
    print("📦 Fetching Products")


# Python internally does this
get_products = login_required(get_products)


# Call function
get_products()