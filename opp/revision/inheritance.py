# class BaseChai:
#     def __init__(self,type_):
#         self.type = type_

#     def prepare(self):
#         print(f"preparing {self.type} chai....")

# class MasalaChai(BaseChai):
#     def add_spcies(self):
#         print(f"Adding cardamom, ginger, colves. {self.type}")

# class ChaiShop:
#     chai_cls = BaseChai #composition get the reference of BaseChai

#     def __init__(self):
#         self.chai = self.chai_cls("Regular chai")

#     def serve(self):
#         print(f"serving {self.chai.type} chai in the shop")
#         self.chai.prepare()

# class FancyChaiShop(ChaiShop):
#     chai_cls = MasalaChai

# shop = ChaiShop()
# fancy = FancyChaiShop()
# shop.serve()
# fancy.serve()


class BaseChai:
    def __init__(self,type_):
        self.type=type_

    def prepare(self):
        print(f"Preparing {self.type} type of chai...")

class MasalaChai(BaseChai):

    def add_spices(self):
        print("Adding cardamom, ginger, cloves")

class ChaiShop:
    chai_cls = BaseChai # accesing whole thing from basechai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop:
    fancy_shop = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai_cls.add_spices()