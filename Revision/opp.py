# class Chai:
#   pass

# class ChaiTime:
#   pass

# print(type(Chai))

# ginger_tea = Chai()

# print(type(ginger_tea))

# print(type(ginger_tea) is Chai)
# print(isinstance(ginger_tea,Chai))

# print(type(ginger_tea) is ChaiTime)


# class Animal:
#   pass

# class Dog(Animal):
#   pass

# tommy = Dog()

# print(type(tommy))
# print(isinstance(tommy, Dog))
# print(isinstance(tommy, Animal))

# print(Chai)

# _namespace.py

# class Chai:
#   origin = "India"

# Chai.is_hot = True

# # creating objects from class Chai
# masala = Chai()

# print(f"Masala 1 {masala.origin}")


# print(f"Masala 2 {masala.is_hot}")

# masala.is_hot = False

# print(f"Class {Chai.is_hot}")
# print(f"Masala {masala.is_hot}")


# class Chai:
#   temp = "hot"
#   strength = "strong"

# cutting = Chai()
# print(cutting.temp)

# cutting.temp = "Mild"
# cutting.cup = "small"
# print(f"After Changing the temp it get {cutting.temp}")
# print(f"cup size of chai {cutting.cup}")
# print(f"look into the class {Chai.temp}")

# del cutting.temp
# del cutting.cup

# print(f"After del Changing the temp it get {cutting.temp}")
# print(f"cup del size of chai {cutting.cup}")
# print(f"look into the class after del {Chai.temp}")

# Creating methods

# __self__args

class Chaicup:
  size = 150

  def desc(self):
    return f"A {self.size} ml chai cup"
  
cup = Chaicup()

print(cup.desc)