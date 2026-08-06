menu = {
    "Tea": 20, 
    "Coffee": 40, 
    "Burger": 120, 
    "Pizza": 250, 
    "Sandwich": 80
}

def main_menu():
  print("==== Welcome to AI RESTAURANT ====")
  print("1. Show Menu")
  print("2. Place Order")
  print("3. Exit")
  
  choice = int(input("Enter your choice : "))

  if choice == 1:
     show_menu()
  elif choice == 2:
    place_order()
  elif choice == 3:
    exit_program()
  else:
     print("Invalid choise")

def show_menu():
  for item , price in menu.items():
    print(f"{item} ------ MENU ------ {price}")

def place_order():
    item = input("Enter the menu name : ")
    if item in menu:
       print(f"{item} order succesfully of")
       print(f"Total Bill {menu[item]}")
       print("Order Placed Thank for shopping")
    else:
       print("item is not present in the menu")

def exit_program():
   print("Thank you for visiting AI RESTAURANT!")

main_menu()