from operations import (add , substract, multiply, divide)

def calculator():
  print("===== Calculator =====")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 5:
        print("Thanks for using calculator")
        return

  def get_input():
       num1 = int(input("Enter first number : "))
       num2 = int(input("Enter second number : "))
       return num1, num2
  
  num1, num2 = get_input()

  if choice == 1:
      print(add(num1,num2))
  elif choice == 2:
       print(substract(num1,num2))
  elif choice == 3:
        print(multiply(num1,num2))
  elif choice == 4:
        print(divide(num1,num2))
  else:
        print("Invalid choice")

calculator()