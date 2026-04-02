# class Person:
#     def greet(self):
#         print("Hello from person")

# class Student(Person):
#     def study(self):
#         print("Studying")

# s = Student()
# s.greet()
# s.study()

# class Animal():
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# d = Dog()
# d.sound()

# class Vehical:
#     def __init__(self,name):
#         self.name = name

#     def start(self):
#         print(f"Car driver name {self.name}")

# class Driving(Vehical):
#     def drive(self):
#         print(f"Car driving is good rating him {self.name}")

# d = Driving()
# d.start()
# d.drive()

# class Animal:
#     def sound(self):
#         print("ANIMAL")

# class Dog(Animal):
#     def sound(self):
#         print("Dog bark")

# s = Dog()
# s.sound()

# class Animal:
#     def __init__(self,name):
#         self.name = name
#         print("Animal constructor")

# class Dog(Animal):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll = roll
#         print("Dog constructor")
# d = Dog("ste",111)

# class Animal:
#     def sound(self):
#         print("Animal")
        
# class Dog(Animal):
#     def bark(self):
#         pass

# s = Dog()
# s.sound()
# s.bark()

class Person:
    def __init__(self, name,roll):
        self.roll = roll

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # 👈 parent call
        self.roll = roll

s = Student("Vishal",101)
print(s.name)


##### continue