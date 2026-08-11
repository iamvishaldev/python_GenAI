import json

def load_students():
    with open("students.json","r") as file:
        students = json.load(file)
        return students
    
def save_students(students):
    with open("students.json","w") as file:
        json.dump(students,file)

def add_students():
    try:
        print("Welcome to AI database")
        students = load_students()

        student_name = input("Enter Your Name: ")
        student_age = int(input("Enter Your Age: "))
        student_course = input("Enter Your Course: ")

        student = {
            "Name": student_name,
            "Age": student_age,
            "Course": student_course
        }

        students.append(student)
        save_students(students)

    except ValueError:
        print("Enter a Valid Number")

def view_students():
    students = load_students()

    if students:
     for student in students:
        print(student)
    else:
        print("Add students")

add_students()
view_students()