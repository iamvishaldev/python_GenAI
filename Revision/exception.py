with open("note.txt","w") as file:
  file.write("I am learning python")

with open("note.txt","r") as file:
  data = file.read()
  print("Data after write")
  print(data)

with open("note.txt","a") as file:
  file.write("\nLearn AI")
  file.write("\nToday I learned File Handling")

with open("note.txt", "r") as file:
    data = file.read()

print("\nData after Append:")
print(data)