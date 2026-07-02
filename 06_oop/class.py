class Chai:
    type = "Ginger"
    price = 10

chai1 = Chai() # Object
chai2 = Chai() # Object

chai1.type = "Masala" # Object can have its own data

print(chai1.type)
print(chai2.price)

# class Car:
#     brand = "BMW" # class variable hain

# car1 = Car()
# car2 = Car()

# car1.brand = "Audi"

# print(car1.brand)
# print(car2.brand)

class Car:
    brand = "BMW"

car1 = Car()
car2 = Car()

car1.brand = "TATA"

print(car1.brand)