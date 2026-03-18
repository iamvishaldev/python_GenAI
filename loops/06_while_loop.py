temp = 81

while temp<100:
    print(f"🌡 Temperature: {temp}°C")
    if temp>=100:
        print("💨 Water is boiling!")
        if temp>80:
            print("Almost boiling")
    temp += 15
    
