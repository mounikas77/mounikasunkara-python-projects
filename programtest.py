#6/12/23(hclass for 100 programs)
# l=[]
# for num in range(2000,3201):
#     if (num %7==0) and (num %5!=0):
#         l.append(num)
# print(l)

#dec-6/12/2023(hclass)

# oops concepts

# class Flower:
#     def __init__(self,name,colour,stock):
#         self.name=name
#         self.colour=colour
#         self.stock=stock
# f1=Flower("rose","red",30)
# def get.flowername
# print(f1.__Flower__name)
# print(f1.name)
# print(f1.colour)
# print(f1.stock)#try chesanu but not correct

# class Flower:
#     def __init__(self, flower_name, price_per_kg, stock_available):
#         self.__flower_name = flower_name
#         self.__price_per_kg = price_per_kg
#         self.__stock_available = stock_available
#
#     def get_flower_name(self):
#         return self.__flower_name
#
#     def set_flower_name(self, flower_name):
#         self.__flower_name = flower_name
#
#     def get_price_per_kg(self):
#         return self.__price_per_kg
#
#     def set_price_per_kg(self, price_per_kg):
#          self.__price_per_kg = price_per_kg
#
#     def get_stock_available(self):
#         return self.__stock_available
#
#     def set_stock_available(self, stock_available):
#          self.stock_available = stock_available
#
#
# f1 = Flower("rose", "20", "30")
# f2 = Flower("sunflower", "30", "40")
# print(f1.get_flower_name())
# print(f1.get_price_per_kg())
# #print(f1.get_stock_available())
# f1.set_flower_name("rosess")
# print(f1.get_flower_name())
# f1.set_price_per_kg("500")
# print(f1.get_price_per_kg())
# #f1.set_stock_available("700")
# #print(f1.get_stock_available())
#
# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using symmetric_difference() method
symmetric_diff_method = set1.symmetric_difference(set2)
print("Symmetric Difference (Method):", symmetric_diff_method)

# Using ^ operator
symmetric_diff_operator = set1 ^ set2
print("Symmetric Difference (Operator):", symmetric_diff_operator)
