# import json

# student = {
#   "name":"xyz",
#   "age":25,
#   "course":"python"
# }

# # Read
# with open("students.json","r") as file:
#   students = json.load(file)

# # Add student
#   students.append(student)

# # Write
# with open("students.json","w") as file:
#   json.dump(students,file)

#   print("s",students)

import json

def load_students():
  with open("students.json","r") as  file:
   students = json.load(file)

  return students

def save_students(students):
  with open("students.json","w") as file:
   json.dump(students,file)

def add_student():

 try:

    print("Welcome to AI course")

    students = load_students()

    student_name = input("Enter Your Name : ")
    student_age = int(input("Enter Your Age : "))
    student_course = input("Enter Your Course : ")
  
    student = {
      "Name":student_name,
      "Age": student_age,
      "Course": student_course
    }

    students.append(student)

    save_students(students)

 except ValueError:
   print("Enter a Valid Number")

def view_student():
  student_info = load_students()
  print("studentinfo",student_info)

view_student()