#Operator overloading and betearray in python

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

# full_liquid_flavor = base_liquid.extend(extra_flavor)

full_liquid_mix = base_liquid + extra_flavor
strong_brew = ["black tea","water"] * 3
print(f"Strong brew: {strong_brew}")