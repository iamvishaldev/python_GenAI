# def print_order(name,chai_type):
#     print(f"{name} orderded {chai_type} chai!")

# print_order("max","masala")
# print_order("max1","tulsi")
# print_order("max2","ginger")
# print_order("max3","tulsi")

# def fetch_sales():
#     print(f"fetch the sales")

# def filter_valid_orders():
#     print(f"fetch the filter valid orders")

# def summarize_data():
#     print(f"fetch the summarize the data")

# def generate_report():
#     fetch_sales()
#     filter_valid_orders()
#     summarize_data()
#     print(f"All fetch done")

# generate_report()

def get_user_input():
    user_Id = input("Enter your user id: ")
    return user_Id

def validate_user(user_Id):
    if user_Id == "":
        print("Enter a valid user id")
        return False
    print("Valid user id")
    return True

def save_to_db(user_id):
    print(f"Successfully {user_id} saved in data base")

def register_user():
    user_id = get_user_input()

    if validate_user(user_id):
        save_to_db(user_id)
        print("User registration completed")
    else:
        print("Registration failed")
        
register_user()