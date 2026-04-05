# Class & Object in python

# class Student: # blueprint
#     college_name = "Birla College" # class attribute comman

#     # custom constructors (parameterized)
#     def __init__(self, name, marks): # self is the refrence of the current instance of the class and is used to access varaible that belongs to the class
#         self.name = name # name is the varibale ban jayega class me # obj attr> class attr
#         self.marks = marks
#         print(f"Adding new student name {name} with marks {marks} in Database.... of college {self.college_name}")

#     def hello(self):
#         print(f"Hello student welcome, in {self.college_name}")
    
#     def getmarks(self):
#         return print(self.marks)

# # creating object(instance of class)
# s1 = Student("Vishal",97) # object
# # print(s1.name)

# s2 =  Student("Rahul",99)
# # print(s2.name)
# s1.hello()
# s1.getmarks()

# # Let's Practice

# # Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# # Then create a method to print the average.

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod #decorator static method worked has class level
#     def hello():
#         print("Hello")

#     def student_avg(self):
#         total = 0
#         for val in self.marks:
#             total += val

#         avg = total / len(self.marks)
#         print(f"Hi {self.name}, your avg score is: {avg}")


# sub1 = Student("Vishal", [85, 56, 95])
# sub1.student_avg()

# sub1.name = "Rahul"
# sub1.hello()

class Chai:
    origin = "India"
    brand = "Indi chai patti"

c1 = Chai()
c2 = Chai()

print(c1)
print(c2)

c1.brand = "Tazahole"

print(c1.origin)
print(c2.origin)

print(c1.brand)
print(c2.brand)