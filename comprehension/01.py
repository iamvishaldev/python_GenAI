# Normal Loop

# num = [1,2,3,4]

# result = []

# for n in num:
#     result.append(n)
# print(result)

# Convert to Comprehension

num = [1,2,3,4]

result = [n*n for n in num]
# print(f"result : {result}")

# add
 
num_add = [2,4,5,6]

add_result = [n+1 for n in num_add]
# print(f"result : {add_result}")

# mul

num_mul = [2,6,4,5]

add_mul = [n*n for n in num_mul]

# print(f"result : {add_mul}")

# Normal Loop

num =[1,2,3,4,5,6]

# even = []
# odd = []

# for n in num:
#     if n%2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# print(even)
# print(odd)

even = [n for n in num if n%2 == 0]
print(even)