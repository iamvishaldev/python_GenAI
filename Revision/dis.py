# chai_order = dict(type="Masala Chai",size="Large", sugar=2)

# print(f"Chai order : {chai_order}")

# chai_recipe = {} # dictionary
# chai_recipe["base"] = "black tea"
# chai_recipe["liquid"] = "milk"

# print(f"Recipe base : {chai_recipe["base"]}")
# del chai_recipe["liquid"]

# print(f"extact chai_base {chai_recipe['base']}")

# # all the keys
# chai_order = {"type":"Ginger Chai","size":"Medium","sugar":1}

# print(f"Order details (keys) : {chai_order.keys()}")

# # get all values

# print(f"Order details (values) : {chai_order.values()}")

import arrow

time = arrow.utcnow()
time.to("India")