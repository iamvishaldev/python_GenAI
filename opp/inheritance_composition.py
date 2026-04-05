# class BaseChai:
#     def __init__(self, type_):
#         self.type = type_
#         print(f"Parent init {self.type}")

# class MasalaChai(BaseChai):
#     def __init__(self,type_):
#         super().__init__(type_) # 👈 parent call
#         print(f"Child init {self.type}")

# chai = MasalaChai("Masala")
# print(chai.type)

# class Cup:
#     def __init__(self, size):
#         self.size = size


# class Chai:
#     def __init__(self, type_, cup):
#         self.type = type_
#         self.cup = cup   # composition

#     def serve(self):
#         return f"{self.type} chai in {self.cup.size} ml cup"


# class SpecialChai(Chai):  # inheritance
#     def __init__(self, type_, cup, spice_level):
#         super().__init__(type_, cup)
#         self.spice_level = spice_level

#     def serve(self):  # overriding
#         return f"✨ {self.type} chai with spice {self.spice_level} in {self.cup.size} ml cup"


# # Usage
# cup = Cup(200)
# chai = SpecialChai("Masala", cup, "High")

# print(chai.serve())

class Cup:
    def __init__(self,size):
        self.size = size

class Chai:
    def __init__(self,type_,cup):
        self.type = type_
        self.cup = cup # composition object reuse

    def serve(self):
        return f"{self.type} chai in {self.cup.size} ml cup"
    
cup = Cup(150)
chai = Chai("Masala",cup)

print(chai.serve())