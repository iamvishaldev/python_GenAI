# # class method

# class ChaiOrder():

#     def __init__(self, tea_type, sweetness, size):
#         self.tea_type = tea_type
#         self.sweetness = sweetness
#         self.size = size

#     @classmethod
#     def form_dict(cls,order_data):
#         return cls(
#             order_data["tea_type"],
#             order_data["sweetness"],
#             order_data["size"],
#         )
    
#     @classmethod
#     def from_string(cls,order_string):
#         tea_type, sweetness, size = order_string.split("-")
#         return cls(tea_type, sweetness, size)
    
# # order1 = ChaiOrder()
# order1 =ChaiOrder.form_dict({"tea_type":"masala","sweetness":"medium","size":"larger"})
# print(order1)

class TeaOrder:

    def __init__(self, type_, sweetness, size):
        self.type = type_
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_string(cls, text):
        type_, sweetness, size = text.split(",")
        return cls(type_, sweetness, size)
    
order = TeaOrder.from_string("Masala,Medium,Large")

print(order.size)