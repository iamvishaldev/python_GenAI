# Loops
# Loops let you repeat code without writing it multiple times. Instead of copying and pasting, you tell Python to repeat the code for you.


for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(0,10,2):
    print(i)

for _ in range(5):
    print(_,"AI")

# Loop through text

name = "Python"

for letter in name:
    print(letter)

colors = ["red", "blue", "green"]

for color in colors:
    print(color)

count = 0
while count < 5:
    print(f"Count is {count}")
