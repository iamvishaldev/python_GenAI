class Book:

  def __init__(self,title,author):
    self.title = title
    self.author = author

  def display(self):
    print(f"The Book Title is {self.title} by author {self.author}")

book1 = Book("Atomic Habit","James Clear",False)

book1.display()