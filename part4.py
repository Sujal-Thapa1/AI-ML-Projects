# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name
    

# stu1 = Student("Sujal",21)

# print(stu1.get_name())


'''class laptop:
    storage_type = "SSD"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage

l1 = laptop("8GB","1TB")
'''


'''class Laptop:
    storage_type = "SSD"

    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type: {cls.storage_type}")

    def get_info(self):
        print(f"Laptop Info: RAM = {self.RAM}, Storage = {self.Storage}")

    @staticmethod
    def clac_discount(price,discount):
        return price - (price * discount / 100)

l1 = Laptop("16GB","200GB")
l1.get_info()
'''


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")


p1 = Product("Iphone",1_00_000)

p1.get_info()