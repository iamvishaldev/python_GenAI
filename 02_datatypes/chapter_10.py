chai_order = dict(type="Masala Chai", size="large", sugar=2)

print(f"chai you ordered: {chai_order}")

chai_recipe = {}

chai_recipe["base"] = "black tea"

chai_recipe["liquid"] = "milk"

del chai_recipe["base"]

print(f"what is the recipe of the chai: {chai_recipe}")

print(chai_order.get("milk"))

print("chai_order",chai_order.items())

last_item = chai_order.popitem()

print(f"Removed last item:{last_item}")