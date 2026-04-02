# class Car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

#     def show(self):
#         print(f"{self.brand} costs {self.price}")

# car1 = Car("BMW",5000000)
# car2 = Car("Audi",600000)

# car1.show()
# car2.show()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def intro(self):
#         print(f"My name is {self.name} and I am {self.age}")

# student1 = Student("Ram",25)
# student2 = Student("Dev",26)

# student1.intro()
# student2.intro()

# class Car:
#     def show(self): # self = object ko receive karne ke liye hota hai
#         print("Hello")
# c = Car()
# c.show() # Car.show(c) 

# class Car:
#     def set_brand(self,brand):
#         self.brand = brand
#         print(f"car brand name {brand}")

# c1 =Car()
# c2 =Car()

# c1.set_brand("TATA")
# c2.set_brand("Range Rover")

class Car:
    def __init__(self,brand): #__init__ = object banate hi data set karna
        self.brand = brand

c1 = Car("TATA") # Car.__init__(c1,"TATA")
c2 = Car("Range Rover") # Car.__init__(c2,"Range Rover")

print(c1.brand) 
print(c2.brand) 

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Vishal",27)
s2 = Student("Rahul",26)

print(s1.name, s1.age)
print(s2.name, s2.age)
