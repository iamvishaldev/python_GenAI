chai_menu = {"masala":30, "ginger":40}

try:
    chai_menu['elichi']
except KeyError:
    print("The key you are trying to access does not exist")

print("Hello Chai code")