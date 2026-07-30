# Mini Project 1: Student

# class Student:
#     def __init__(self,std_name,std_class,std_rollno,std_marks):
#         self.std_name = std_name
#         self.std_class = std_class
#         self.std_rollno = std_rollno
#         self.std_marks = std_marks

    
#     def display_details(self):
#         print(f"student name is {self.std_name}")
#         print(f"student is in class {self.std_class}")
#         print(f"student roll no is {self.std_rollno}")
#         print(f"Student marks is {self.std_marks}")

#     def update_marks(self,marks):
#         self.std_marks = marks
 
# s1 = Student("Vishal","A",7,98)
# s1.update_marks(99)

# s1.display_details()

# Mini Project 1: Bank Account System

# class Bank:
#     def __init__(self,user_name,user_mobno,user_bal):
#         self.user_name = user_name
#         self.user_mobno = user_mobno
#         self.user_bal = user_bal

#     def display_accountdetails(self):
#         print(f"user account name is {self.user_name}")
#         print(f"user account name is {self.user_mobno}")
#         print(f"user bal is {self.user_bal}")

#     def check_acc_bal(self):
#         print(f"user balance is {self.user_bal}")

#     def deposit_amount(self,amount):
#         self.user_bal  = self.user_bal + amount

#     def widthdrawl(self,amount):
#         self.user_bal = self.user_bal - amount
    
# user1 = Bank("Vinod","123",3000)

# user1.display_accountdetails()

# user1.deposit_amount(200)

# user1.widthdrawl(1000)

# user1.check_acc_bal()

class Product:
  def __init__(self,product_name,product_price,product_qty):
    self.product_name = product_name
    self.product_price = product_price
    self.product_qty = product_qty

  def display_product(self):
    print(f"Product name is {self.product_name}")
    print(f"Product price is {self.product_price}")
    print(f"Product qty is {self.product_qty}")

product1 = Product("Mac",100000,1)

product1.display_product()

class ShoppingCart:
  def __init__(self):
    self.products = []

  def add_product(self,product):
    self.products.append(product)

cart = ShoppingCart() # ShoppingCart.__init__(cart)

product2 = Product("Hp",45000,5)

cart.add_product(product2)