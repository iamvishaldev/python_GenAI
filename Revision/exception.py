# with open("note.txt","w") as file:
#     file.write("I am learning the python")

# with open("note.txt","r") as file:
#     data = file.read()

# print("Data after write")
# print(data)

# with open("note.txt","a") as file:
#     file.write("\nLearn AI")
#     file.write("\nToday I learned File Handling.")

# with open("note.txt","r") as file:
#     data = file.readlines()

# print("Data after append")

# print(data)

# class OutOfIngredientsError(Exception):
#     pass

# def make_chai(milk,sugar):
#     if milk == 0 or sugar == 0:
#         raise OutOfIngredientsError("Missing milk or sugar")
#     print("chai is ready")

# make_chai(0,1)

class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter the withdrawal amount :"))
    
    if amount > balance:
        raise InsufficientBalanceError("Amount should not be greater then the balance")
    balance-=amount
    print(f"Your balance is {balance}")
    
except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Transaction Successful")
    print("Thank you for using our ATM.")