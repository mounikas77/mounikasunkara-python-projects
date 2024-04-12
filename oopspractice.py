#oops practice
class Car:
    def __init__(self, color, price, engine, name, brand):
        # instance variables
        self.color = color
        self.price = price
        self.engine = engine
        self.name = name
        self.brand = brand

    def start(self):
        pass

    def stop(self):
        pass


innova = Car("white", "1500000", "3500HP", "Innova", "TOYOTA")
kia = Car("black", "1000000", "3500HP", "Kia", "Kia")

print("Innova information")
print(f"""
    Name : {innova.name}
    Brand : {innova.brand}
    Price : {innova.price}
    engine : {innova.engine}
""")

print(id(innova))
print(id(kia))
kia.name = "Suzuki"

print("Kia information")
print(f"""
    Name : {kia.name}
    Brand : {kia.brand}
    Price : {kia.price}
    engine : {kia.engine}
""")
print(innova.name)

print(isinstance(kia, Car))
o/p:Innova
True

