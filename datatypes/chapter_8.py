ingredients = ["water","milk","black tea"]

ingredients.append("sugar")

ingredients.remove("water")

print(f"ingredients are:",ingredients)

spice_options = ["ginger", "cardamom"]

chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)

chai_ingredients.insert(2,"black tea")

last_added = chai_ingredients.pop()

print("--->",last_added)

chai_ingredients.sort()

print(f"chai,{chai_ingredients}")

sugar_level = [1,2,3,4,5]

print(f"Max sugar level:{max(sugar_level)}")