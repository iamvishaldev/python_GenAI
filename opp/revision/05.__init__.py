class Chai_Order:

    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
            return f"{self.type} ml of the {self.size} chai"
        
chai = Chai_Order(150,"small")
print(chai.type)
print(chai.size)

print(chai.summary())