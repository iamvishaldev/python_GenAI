class Chai:
    temperature = "hot"
    strength = "Strong"


# Create object
cutting = Chai()

# Access class attributes
print(cutting.strength)      # Strong
print(cutting.temperature)   # hot

# Attribute shadowing (instance overrides class)
cutting.temperature = "Mild"
cutting.cup = "small"

print("After changing:", cutting.temperature)  # Mild

# Delete instance attributes
del cutting.temperature
del cutting.cup

# Falls back to class attribute
print("After deleting:", cutting.temperature)  # hot

# Safe access (avoids error)
print("Cup:", getattr(cutting, "cup", "Not Found"))

class A:
    val = []

obj1 = A()
obj2 = A()

obj1.val.append(1)

print(obj1.val, obj2.val)