device_status = input("Is device is (active/unactive) :").lower()
temperature = int(input("Enter the temperature :"))

if device_status == "active":
    if temperature > 50:
        print("🚨 EMERGENCY SHUTDOWN")
    elif temperature>45:
        print("So humadity")
    elif temperature>35:
        print("Too hot temp")
    elif temperature>25:
        print("OKOK Temp")
    elif temperature>10:
        print("Cool")
    else:
        print("Too Cool")
else:
    print("Device is not active")