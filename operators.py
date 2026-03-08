first_name = "Jhon"
age = 25
has_license = True

#AND - both must be true
can_drive = age>=16 and has_license


#OR - at least one must be true

day = "Sunday"

is_weekend = day == "Sunday" or day == "Saturday"

print(f"{first_name} can drive {can_drive} on  Sunday {is_weekend}")