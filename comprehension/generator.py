# A generator is like a list, but it does NOT store all values in memory
# it gives values one by one (on demand)

# gen = (i for i in range (1,6))

# print(next(gen))  # 1
# print(next(gen))  # 4
# print(next(gen))  # 9

# gen = (i*i for i in range(1000000000))
# for i in gen:
#     print(f"iiiii : {i}")
    

squares = (i*i for i in range(10))
for val in squares:
    print(val)