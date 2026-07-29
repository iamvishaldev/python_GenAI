# class ChaiCup:
#     size = 150 #ml

#     def discribe(self):
#         return f"A {self.size} ml chai cup"
    
# cup1 = ChaiCup()
# cup2 = ChaiCup()

# print(cup1.discribe())
# print(cup2.discribe())

# ChaiCup.size = 120 #ml

# print(cup1.discribe())
# print(cup2.discribe())

# class ChaiOrder:
#     def __init__(self,type_,size):
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f"{self.size} ml of {self.type} chai"
    
# order_one = ChaiOrder("Masala",200)

# print(order_one.summary())

# order_two = ChaiOrder("Gonger",150)

# print(order_two.summary())

# without init  

# class ChaiOrder:

#     def __init__(self,type_,size):
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f"{self.size} ml of {self.type} chai "
    
# order = ChaiOrder("Masala Chai",20)
# print(order.summary())

# order_two = ChaiOrder("Ginger",220)
# print(order_two.summary())

# class Student: # it is class
#     pass

# s1 = Student() # object 1

# s1.name = "Rahul" # attributes 1
# s1.age = 16 # attributes 1

# s2 = Student() # object 2

# s2.name = "Priya" # attributes 2
# s2.age = 22 # attributes 2

# print(s1.name)
# print(s1.age)

# print(s2.name)
# print(s2.age)

# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("Vinod1",33)
# s2 = Student("Dinod1",32)

# print(s1.name)
# print(s2.name)

# class Animal:

#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     pass


# dog = Dog()

# dog.eat()