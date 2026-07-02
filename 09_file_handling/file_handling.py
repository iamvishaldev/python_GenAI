# file = open("order.txt","w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

with open("order.txt","r") as file:
    data = file.read()
    print(data)