# Numbers can do math
total = 10+5

print(f'total:{total}')

# Strings combine differently 

name  = "Hello" + "World"
print(f'name:{name}')

# Can't mix without converting
#age = "25" + 5
age = int(25)+5
print(f"{age}")

#Basic math operations
# Addition and subtraction

total = 10+5
print(f"{total}")

area = 6*4
half = 10/2
print(f"area{area}&half{half}")

# Powers

squared = 5 ** 2
print(f"squared",{squared})

#Integer vs float division

#Regular division 
result = 10/3
print(f"result",{result})

#String
first_name = "John"
last_name = "Doe"

full_name = first_name + " " +last_name

print(f"fullName is {full_name}")

string = "My name is Dave"

# Repetition
stars = "*" * 5
dash = "_" * 45
print(stars)
print(dash)

#String length

message = "Hello"
print(len(message))

empty = ""
print(len(empty))

#Converting to string

#Turn other types into strings with str():

age=25
message = "I am " + str(age) + " years old"
print(message)

# Direct assignment

is_ready = True

# From comparisons

age=18
can_vote = age>=18

score = 75
is_pass = score>35
print(f"{first_name} can vote: {can_vote} & also pass in Exam with {score}%")