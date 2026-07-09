# def get_numbers():
#     numbers = []

#     for i in range(1, 1000001):
#         numbers.append(i)

#     return numbers

# nums = get_numbers()

# print(nums)


# Generator Function

# def chai():
#     print("Make the chai")
#     return "Masala chai"
# print(chai())

# yield

# def chai():
#     print("Making Masala Chai")
#     yield "Masala"
#     print("Making Ginger Chai")
#     yield "Ginger"
#     print("Done")
# g = chai()

# print(next(g))
# print(next(g))
# print(next(g))

def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g))
print(next(g))

for i in g:
    print(i)
