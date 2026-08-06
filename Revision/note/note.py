def note_manager():
  print("===== Notes Manager =====")
  print("1. Write Note")
  print("2. Read Notes")
  print("3. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
     write_notes()
  elif choice == 2:
     read_notes()
  elif choice == 3:
     exit_from_notes()
  else:
     print("Invalid choise enter a valid choice")

def write_notes():
    your_notes = input("Enter your notes : ")

    with open("note.txt",'a') as file:
       file.write(your_notes + '\n')
       print("✅ Note saved successfully.")

def read_notes():
  try:
    with open("note.txt",'r') as file:
       note_data = file.read()
       if note_data:
           print("\n===== YOUR NOTES =====")
           print(note_data)
       else:
          print("No notes found.")

  except FileNotFoundError:
    print("No notes available. Please write a note first.")

def exit_from_notes():
    print("Thanks for using ai notes")

note_manager()