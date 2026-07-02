# List Comprehension ko READ kaise kare

# odd = []
# even = []

# for i in range(10):
#     if i%2 == 0:
#         odd.append(i)
#     else:
#         even.append(i)
# print(f"odd number : {odd}")
# print(f"even number : {even}")

# evens = [i for i in range(20) if i%2 ==0]

# square_evens  = [i*i for i in range(10) if i%2 == 1]

# yes_no = ["Yes" if i %2 == 0 else "No" for i in range(5)]
# print(f"yes_no : {yes_no}")

num = [1,2,3,4,5,6]

# num = [i for i in num if i%2 ==0]

nums = ["Even" if i%2 ==0 else "Odd" for i in num]

print(f"nums : {nums}")

even_square = [i*i for i in range(1,21) if i%2 == 0]

print(f"square : {even_square}")

task2 = ["Even" if i%2 == 0 else "Odd" for i in range(10)]

print(f"task2 : {task2}")
