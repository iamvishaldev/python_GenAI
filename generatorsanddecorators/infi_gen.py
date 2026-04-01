# def chai_counter():
#     num = 1
#     while True:   # infinite loop
#         yield num
#         num += 1

# chai = chai_counter()

# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai))


# def gen():
#     while True:
#         print("chai")

# g = gen()
# print(next(g))

# 3. Even Number Generator

def even_number():
    n =0
    while True:
        yield n
        n +=2
g = even_number()

for _ in range(5):
    print(next(g))