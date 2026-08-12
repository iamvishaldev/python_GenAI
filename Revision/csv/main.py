import csv

# READ
with open("students.csv","r") as file:
   data = csv.reader(file) # reader/itrator object

   next(data) # → consumes first row

   for item in data:
      print("item--->",item)

# WRITE
with open("students_output.csv","w") as file:
   data = csv.writer(file)
   data.writerow(["Vishal",29,"Python"])