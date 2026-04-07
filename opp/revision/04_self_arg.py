class Chaicup:
    size = 120 #ml

    def describe(self): #method
        return f"A {self.size} ..."
    
cup = Chaicup() # Chaicup.describe(cup)

print(cup.describe())
# print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(cup_two.describe())