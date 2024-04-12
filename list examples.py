#jan_6
# a=(4)
# print(type(a))
# l = [[1, 2], 3, [4, 5], [6, 7, 8]]
# result = []

# for item in l:
#     if isinstance(item, list):
#         result.extend(item)
#     else:
#         result.append(item)
#
# print(result)
##############
# l = [[1, 2], 3, [4, 5], [6, 7, 8]]
# result = []
# for i in l:
#     l.extend(i)
#     if i.isinstance("item"):
#         result.extend.(item)

##################
#for loop example:
# x=[10,20,30,40]
# for i in x:
#     print(i)
# o/p:10
# 20
# 30
# 40
#################
# for i in range(2,21,2):
#     print(i)
# o/p: it displays the even numbers
############
#print(range(1,10))
#o/p:error display vastundi(or)same print avutundi
##############
# no=input(input("enter any number:"))
# if (no==4):
#     print("this is 4")
#     print("program over")
##############
# no = int(input("Enter any number:"))
# if no == 4:
#     print("This is 4")
#     print("Program over")
# o/p:This is 4
# Program over
##################
# x=100
# y=200
# if (x>y):
#     print("x is largest")
# else:
#     print("y is largest")
#     print("program over")
# o/p:y is largest
# program over
################
#if elif_else:
# n=int(input("enter your age:"))
# if n<15:
#     print("you are kid")
# elif n<40:
#     print("you are young")
# elif n<60:
#     print("you are old")
# else:
#     print("you are aline ")
#     print("program over ")
# o/p:enter your age:14
# you are kid
#2.enter your age:80
# you are
# program over aline
##################
# while statement
# i=2
# while(i<=20):
#     print(i)
#     i=i+2
#o/p:it displays even numbers
#############
#############3 we use break statement
# for i in range(1,8):
#     if i==4:
#         break
#     print(i)
# print("program over")
# o/p:1
# 2
# 3
# program over
##################
##### we use continue statement
# for i in range(1,8):
#     if i==4:
#         continue
#     print(i)
# print("program over")
# o/p:1
# 2
# 3
# 5
# 6
# 7
# program over
# here value 4 is skip this situation
#################
# use pass statement
# for i in range(1,8):
#     if i==4:
#         pass
#         print("hai")
#     print(i)
# print("program over")
# o/p:1
# 2
# 3
# hai
# 4
# 5
# 6
# 7
# program over
###################
#functions:
# def add(a,b):
#     return a+b
# print(add(10,20))
# o/p:30
#############
###########lambda function
# add=lambda a,b:a+b
# print(add(10,20))
# o/p:30
###################
#map():by using functions
# def square(n):
#     return n*n
# l=[1,2,3,4,5]
# print(list(map(square,l)))
# o/p:[1, 4, 9, 16, 25]
############
# map() using lambda function
# l=[1,2,3,4,5]
# print(list(map(lambda n:n*n,l)))
# o/p:[1, 4, 9, 16, 25]
###############
#### filter function
#ex: using for loop
# for n in range(1,11):
#     if (n%2==0):
#         print(n)
# o/p:2
# 4
# 6
# 8
# 10
###############
#### using filter function
# l=[1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     if (n%2 == 0):
#         print(n)
# print(list(filter(even,l)))
# o/p:2
# 4
# 6
# 8
# 10
# []
###################
#using lambda function
# print(list(filter(lambda n:n%2==0,range(1,11))))
# o/p:[2, 4, 6, 8, 10]
#############
## reduce function
# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9,10]
# result=reduce(lambda x,y:x+y,l)
# print(result)
# o/p:55
##################


