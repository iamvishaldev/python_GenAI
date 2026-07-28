# ============================================================
# 1. Classes & instances basics (type, isinstance)
# ============================================================

# class Chai:
#   pass

# class ChaiTime:
#   pass

# print(type(Chai))

# ginger_tea = Chai()

# print(type(ginger_tea))

# print(type(ginger_tea) is Chai)
# print(isinstance(ginger_tea,Chai))

# print(type(ginger_tea) is ChaiTime)


# class Animal:
#   pass

# class Dog(Animal):
#   pass

# tommy = Dog()

# print(type(tommy))
# print(isinstance(tommy, Dog))
# print(isinstance(tommy, Animal))

# print(Chai)


# ============================================================
# 2. Class namespace & attribute lookup
# ============================================================

# _namespace.py

# class Chai:
#   origin = "India"

# Chai.is_hot = True

# # creating objects from class Chai
# masala = Chai()

# print(f"Masala 1 {masala.origin}")


# print(f"Masala 2 {masala.is_hot}")

# masala.is_hot = False

# print(f"Class {Chai.is_hot}")
# print(f"Masala {masala.is_hot}")


# ============================================================
# 3. Class attributes vs instance attributes (override & del)
# ============================================================

# class Chai:
#   temp = "hot"
#   strength = "strong"

# cutting = Chai()
# print(cutting.temp)

# cutting.temp = "Mild"
# cutting.cup = "small"
# print(f"After Changing the temp it get {cutting.temp}")
# print(f"cup size of chai {cutting.cup}")
# print(f"look into the class {Chai.temp}")

# del cutting.temp
# del cutting.cup

# print(f"After del Changing the temp it get {cutting.temp}")
# print(f"cup del size of chai {cutting.cup}")
# print(f"look into the class after del {Chai.temp}")


# ============================================================
# 4. Instance methods & self
# ============================================================

# __self__args

# class Chaicup:
#   size = 150

#   def desc(self):
#     return f"A {self.size} ml chai cup"

# cup = Chaicup()

# print(cup.desc)

# class ChaiCup:
#   size = 150 #ml

#   def describe(self):
#     return f"This is {self.size} ml of masala chai..."

# ChaiCup()


# ============================================================
# 5. Basic inheritance (no constructor)
# ============================================================

# class Animal:
#   def eat(self):
#     print("Eating")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.eat()


# ============================================================
# 6. Inheritance with __init__
# ============================================================

# class Animal:

#   def __init__(self,name):
#     self.name = name

#   def eat(self):
#     print(f"{self.name} is eating")


# class Dog(Animal):

#   def bark(self):
#     print("woof!")


# dog = Dog("Rocky")

# dog.eat()
# dog.bark()


# ============================================================
# 7. Constructors (with vs without __init__)
# ============================================================

# with constructor

# class Student:

#   def __init__(self):
#       print("Student Created")

# student = Student()

# without constructor

# class Student:
#   pass

# student = Student()
# division = Student()

# student.name = "vishal"
# student.age = 32

# division.name = "A"

# print("student",student.name,division.name)

# with constructor

# class Student:

#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     print(name,age)

# student = Student("Vishal",26)
# student2 = Student("dlkd",25)


# ============================================================
# 8. Composition example (ChaiShop / MasalaChai)
# ============================================================

# class BaseChai:

#   def __init__(self,type_):
#     self.type = type_

#   def prepare(self):
#     print(f"Preparing {self.type} chai....")

# class MasalaChai(BaseChai):

#   def add_spices(self):
#     print("Adding cardamom, ginger, cloves.")

# class ChaiShop:
#   chai_cls = BaseChai #  extracting the value from the BaseChai and putting into the chai_class this is the composer.

#   def __init__(self): # constructor
#     self.chai = self.chai_cls("Regular")  # passing the Regular value into the baseclass

#   def serve(self):
#     print(f"serving {self.chai.type} chai in the shop")
#     self.chai.prepare()

# class FancyChaiShop(ChaiShop):
#   chai_cls = MasalaChai

# shop = ChaiShop()
# fancy = FancyChaiShop()

# shop.serve()
# fancy.serve()


# ============================================================
# 9. Each instance has independent state
# ============================================================

# class Student:
#   def __init__(self):
#     self.name = "vishal"

# s1 = Student()
# s2 = Student()
# s3 = Student()

# print(f"s1 {s1.name}")
# print(f"s2 {s2.name}")
# print(f"s3 {s3.name}")


# ============================================================
# 10. Object references, not copies (aliasing)
# ============================================================

# class Student:

#   def __init__(self):
#     self.name = "vishal"

# student1 = Student()
# student2 = student1 # Python doesn't copy the object. It copies the reference (the pointer).

# student2.name = "Rahul"

# print(f"s1---> {student1.name}")
# print(f"s2---> {student1.name}")


# ============================================================
# 11. Inheritance without method override
# ============================================================

# class Animal:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age

#   def eat(self):
#       print(f"{self.name} is eating.")

#   def sleep(self):
#       print(f"{self.name} is sleeping.")

# class Dog(Animal):
#     pass

# d = Dog("Rocky",22)
# print(d.name, d.age)


# ============================================================
# 12. super() and method overriding
# ============================================================

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("Animal is eating")


# class Dog(Animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def eat(self):
#         print("Dog is eating")

# dog = Dog("Rocky","indian")

# print(dog.name)
# print(dog.breed)


# ============================================================
# 13. Active: Composition example (Mobile inside Person)
# ============================================================

class Mobile:
  pass

class Person():

  def __init__(self):
    self.mobile = Mobile()
