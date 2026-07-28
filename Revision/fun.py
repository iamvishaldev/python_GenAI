# def serve_chai():
#     chai_type = "Masala"
#     print(f"Inside function {chai_type}")

# chai_type = "Lemon"
# serve_chai()
# print(f"Outside function {chai_type}")


# def update_order():
#     chai_type="Elaichi"
#     def kitchen():
#         nonlocal chai_type
#         chai_type = "kesar"
#     kitchen()
#     print(f"--> {chai_type}")
# update_order()

# chai_type = "Plain"

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type = "Irani"
#     kitchen()


# front_desk()
# print(f"Final global {chai_type}")

# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ",order)

# prepare_chai(chai)
# print(chai)
# mutable list dict set

# immutable int float str tuple

# chai_cup = 5

# def edit_chai(cup):
#     cup=44

# edit_chai(chai_cup)
# print(chai_cup)

# purve vs impure
# recursive functions
# lambda(Anonymous function)


# Pure function

def pure_chai(cups):
    return cups * 10

print(pure_chai(5))