# if statement
age = 2

if age>=18:
    print("You can vote")
    print("You're an adult")

#if else

temperature = 26

if temperature>=25:
    print("to hot!")
else:
    print("good tempetature")

# if-elif-else

score = 20

if score>=90:
    print("A-Exc")
elif score >=80:
    print('B-Good job!')
elif score>=70:
    print('C-Keep it up')
else:
    print("F-Better luck next time")

#Multiple conditions

age = 25
has_license = True

is_weekend = "Sunday"
holiday = True

if age>=18 and has_license:
    print("You can drive")
else:
    print("You can't drive")

if is_weekend == "Sunday" or holiday:
    print("It's holiday")
else:
    print("It's working day")

# Nested if statements

has_ticket = True
age = 15

if has_ticket:
    if age>=18:
        print("You can watch the movie")
    else:
        print("Need adult age to watch the movie")
else:
    print("Buy the ticket first")
