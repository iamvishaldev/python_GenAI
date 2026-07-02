# class Tea:
#     def __init__(self):
#         self._price = 10

#     def get_price(self):
#         return self._price
    
#     def set_price(self,value):
#         if value>0:
#             self._price = value
#         else:
#             print("Invalid Value")

# t = Tea()
# print(t.get_price)
# print(t.set_price(50))

class Tea:
    def __init__(self):
        self._price = 10
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Invalid price")

t = Tea()

print(t.price)   # getter
t.price = 50     # setter
print(t.price)

t.price = -10    # Invalid