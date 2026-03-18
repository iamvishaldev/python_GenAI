flovours = ["hot water","lemon","cinamon","out of stock","Discontinued","Spiced","Mint"]

for flovour in flovours:
    if flovour == "out of stock":
        continue #skip
    if flovour == "Discontinued":
        break # not run after this
    print(f"Discountoinued item found : {flovour}")

    print(f"out side of loop")