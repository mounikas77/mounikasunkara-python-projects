# jan-9
# decorators
# closure technique
# def outer():
#     x=3
#     def inner():
#         y=3
#         return x+y
# #print(inner())
#     return inner
# a=outer()
# print(a())
# o/p:6
##########################
# def greet():
#     return "hi hello"
# print(greet())
# o/p:hi hello
##################
# def str_upper(greet)
#     def inner():
#         str=greet() inka vundi
#####################
# def sub(fun):
#     def inner(x,y):
#         return fun1()-x-y
#     return inner
# def add(a,b):
#     return a+b
# a=sub(lambda:add(2,3))(1,1)
# print(a)
# o/p:3
#################
#iter tools
# from itertools import count
#
# for i in count(1, 2):
#     print(i)
#     break
#####################
# from itertools import cycle
#
# for item in cycle(['a', 'b', 'c']):
#     print(item)
#     break
#######################
# from itertools import repeat
#
# for i in repeat('hello', 3):
#     print(i)
# o/p:hello
# hello
# hello
##########################
# from itertools import accumulate
#
# data = [1, 2, 3, 4, 5]
# for running_sum in accumulate(data):
#     print(running_sum)
#####################
# from itertools import chain
#
# iter1 = [1, 2, 3]
# iter2 = ['a', 'b', 'c']
#
# for item in chain(iter1, iter2):
#     print(item)
############################
# from itertools import zip_longest
#
# iter1 = [1, 2, 3,4]
# iter2 = ['a', 'b']
#
# for pair in zip_longest(iter1, iter2, fillvalue='N/A'):
#     print(pair)
# o/p:(1, 'a')
# (2, 'b')
# (3, 'N/A')
# (4, 'N/A')
################################
#chat gpt in decorators
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# # Equivalent to: say_hello = my_decorator(say_hello)
#
# say_hello()
###################3
# def f1(list1,list2):
#     list1.append[6,7,8]
#     print(f"inside fun list1 is")
##############
# a=[1,2,3]
# b=a
# b.append([5,6])
# print(a)
# print(b)
# o/p:[1, 2, 3, [5, 6]]
# [1, 2, 3, [5, 6]]
##################
# a=[1,2,3]#sshollow copy
# b=a
# b.append(5)
# print(a)
# print(b)
# o/p:[1, 2, 3, 5]
# [1, 2, 3, 5]
##################
# deep copy
# a=[1,2,3]
# b=a.copy()
# b.append(5)
# print(a)
# print(b)
##############

#oops concepts can use the MRO functions.
################################
# jan-10(wednesday)
# factorial of a given number
# def fact(x):
#     if x==0:
#         return 1
#     return x*fact(x-1)
# x=int(input("enter the value:"))
# print(fact(x))
# o/p:enter the value:5
# 120
#################
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# o/p:['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 35
#######################
# first_naame="harish"
# First_name="harish"
# print(first_name)
# print(First_name)
##################
# get
# post
# #put
# delete
# patch












