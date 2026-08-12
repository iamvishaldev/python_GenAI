class Animal:

  def eat(self):
    print("functionality eating")

class Dog(Animal):
  
  def bark(self):
    print("functionality bark")

dog = Dog()
dog.eat()
dog.bark()