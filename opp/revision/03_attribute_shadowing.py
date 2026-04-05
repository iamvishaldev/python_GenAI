class Chai():
    temp = "Hot"
    strength = "Strong"

cut1 = Chai()
cut2 = Chai()

cut1.temp ="mild"


print(cut1.temp)

Chai.temp = "Very Hot"

print(cut2.temp)


cut1.cup = "small"

print(cut1.cup)
