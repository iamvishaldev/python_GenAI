flovours = ["hot water","out of stock","spiced","discontinued","mint"]

for flavour in flovours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} -->discontinued item found")

print(f"discontinued item found-->")