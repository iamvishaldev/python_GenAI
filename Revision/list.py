ingredients = ["water","milk","black tea"]

ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")

ingredients.remove("water")

print(f"Ingredients are: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["chai_patti","masala","milk"]

chai_ingredients.extend(spice_options)

print("chai",chai_ingredients)

chai_ingredients.insert(2,"jaggery")

print("chai cup2",chai_ingredients)

last_added = chai_ingredients.pop()
print("last added",last_added)

print("chai cup3",chai_ingredients)


base_liquis = ["water","milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquis + extra_flavour

print("full",full_liquid_mix)