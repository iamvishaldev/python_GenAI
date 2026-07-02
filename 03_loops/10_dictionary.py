# # Using Dictionaries Instead of Repeated Cases

# users = [
#     {"id":1,"total":100,"coupon": "p20"},
#     {"id":2,"total":101,"coupon": "p21"},
#     {"id":3,"total":102,"coupon": "p22"},
#     {"id":4,"total":103,"coupon": "p23"}
# ]

# discount ={
#     "P20": (0.2,0),
#     "F10": (0.5,0),
#     "P50": (0,10)
# }

# for user in users:

# student = {
#         "name":"Rahul",
#         "age":21
# }
# print(f"dictionary : {student['age']}")

discount = {
    "P20": (0.2, 0),
    "F10": (0, 10)
}

print(f"discount : {discount["P20"]}")

marks = {
    "math": 90,
    "english": 80
}

print(f"marks  of math: {marks['math']} and of english : {marks['english']}")
