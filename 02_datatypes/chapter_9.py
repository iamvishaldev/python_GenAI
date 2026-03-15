#Operator overloading and betearray in python

base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

# full_liquid_flavor = base_liquid.extend(extra_flavor)

full_liquid_mix = base_liquid + extra_flavor

# print(f"full{full_liquid_mix}")

strong_brew = ["black tea","water"] * 3

print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")

print(f"raw:,{raw_spice_data}")


#   Set and Frozenset in python

essentail_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black paper"}

all_spices = essentail_spices | optional_spices # union

print(all_spices)