# Set Comprehension

# 🔥 Important Point

# ❗ Set me:

# order fix nahi hota
# duplicates allowed nahi

# nums = [1,2,2,3,4,4]

# unique = {i for i in nums}

# even = {i: i for i in range(10) if i%2 == 0}

# even_odd = {i:"Even" if i%2 == 0 else "Odd"  for i in range(1,10)}

# print(f"even {even}")

# set comprehension
num = {0, 1, 1, 4, 4, 9, 16}
even = {i for i in num}
# dictionary comprehension
# even = {i: i for i in range(10) if i%2 ==0}
print(f"even {even}")