def serve_chai():
    yield "Cup1 : Masala Chai"
    yield "Cup2 : Lemon Tea"
    yield "Cup3 : Ginger Chai"
stall = list(serve_chai())
# for cup in stall:
#     print(cup)

# genrator function
def get_chai_list():
    return ["Cup1","Cup2","Cup3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))
