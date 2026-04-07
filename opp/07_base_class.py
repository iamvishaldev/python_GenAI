# class Chai:

#     def __init__(self,type_,strength):
#         self.type = type_,
#         self.strength = strength

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         super().__init__(type_,strength)
#         self.spice_level = spice_level

# chai = GingerChai("Masala","Strong","High")

# print(chai.type)
# print(chai.strength)
# print(chai.spice_level)

# class Chai:
#     def __init__(self,type_,strength):
#         self.type = type_
#         self.strength = strength

# class GingerChai(Chai):
#     def __init__(self,type_,strength,spice_level):
#         super().__init__(type_,strength) # parent ka constuctor chala do
#         self.spice_level = spice_level

# g = GingerChai("Ginger","Strong","Mild")

# print(g.type)

class Tea:
    def __init__(self):
        print("Tea created")

class SpecialTea(Tea):
    def __init__(self):
        super().__init__()
        print("Special Tea created")

t = SpecialTea()