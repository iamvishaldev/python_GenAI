def local_coffe():
    yield "milk coffe"
    yield "coffe"

def imported_coffe():
    yield "Amricano coffe"
    yield "Latte coffe"

def full_menu():
    
    yield from local_coffe()
    yield from imported_coffe()

# overall_menu = full_menu()
# print(next(overall_menu))
# print(next(overall_menu))
# print(next(overall_menu))
# print(next(overall_menu))
# print(next(overall_menu))

for coffe in full_menu():
    print(coffe)

def chai_stall():
    try:
        while True:
            order=yield "Waiting for order"
    except:
        print("Stall closed")

stall = chai_stall()
print(next(stall))
stall.close() #memory cleanup