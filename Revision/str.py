# () tuples
masala_spices = ["cardamom","cloves","cinnamon"]

(s1,s2,s3) = masala_spices
print(f"masala spices {s1} {s2} {s3}")

ginger_ratio, cardamom = 2,1
cardamom, ginger_ratio = 1,2
print(f"ginger {ginger_ratio} car {cardamom}")

# membership

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")