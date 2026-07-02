# class Chai:
#     def make(self):
#         return print("Making chai")
# c = Chai()
# c.make()

# class ChaiUtils:
#     @staticmethod
#     def clean_ingredients(text):
#         print("text",text)
#         return [item.strip() for item in text.split(",")]
    
# raw = " water , milk , ginger , honey"

# obj = ChaiUtils()
# obj.clean_ingredients(raw)

class Demo:

    @staticmethod
    def add(a,b):
        return a+b

c = Demo() 
    
print(c.add(2,3)) # Demo.add(c,2,3)