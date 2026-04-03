class Chaicup:
    size = 150  # class attribute

    def describe(self):
        return f"A {self.size} ml chai cup"


cup = Chaicup()
print(cup.describe())              # A 150 ml chai cup
print(Chaicup.describe(cup))       # same as above

cup_two = Chaicup()
cup_two.size = 100                 # instance attribute (shadowing)

print(Chaicup.describe(cup_two))   # A 100 ml chai cup