class Book:
  def __init__(self,book_id,title,price):
    self.book_id = book_id
    self.title = title
    self.price = price
    self.is_borrowed = False

  def display_book(self):
    print(f"Book ID {self.book_id}")
    print(f"Title: {self.title}")
    print(f"Price: ₹{self.price}")
    print(f"Borrowed: {self.is_borrowed}")

class Library:
  def __init__(self):
    self.books = []

  def borrow_book(self,book_id):
    for book in self.books:
      if book.book_id == book_id:

library = Library() # it's create on library object

book1= Book(1,"Deep work",299)
book2= Book(1,"Let's try",299)

library.books.append(book1)
library.books.append(book2)

for book in library.books:
    book.display_book()