# def functionname():
#      print("this is function")
# functionname()#function ni call chestene output display avutundi.
# o/p:this is function


# def functionname(name):
#     print("this is function",name)
# functionname("kiran")#single parameter
#o/p:this is function kiran


# def functionname(name,age):
#     print("this is function",name,age)
# functionname('kiran',1)#multiple parameters
#o/p:this is function kiran 1


# def functionname(a,b):
#     return a+b
# w=functionname(3,1)
# print(w)#addition of two values

# def functionname(a):
#     return a*3
# print(functionname(3))#multiplication of value
#o/p:9

# def functionname(a):
#     pass
#C:\Users\mounika\PycharmProjects\s3\venv\Scripts\python.exe C:\Users\mounika\PycharmProjects\s3\functionexample.py

#Process finished with exit code 0


# def functionname(a):
#     for i in a:
#         print(i)
# functionname([1,2,3,4,5])#by using list in function.
#o/p:1
# 2
# 3
# 4
# 5

# def functionname(a):
#     for i in a:
#         print(i)
# functionname((1,2,3,4,5,))#by using tuple in function
#o/p:1
# 2
# 3
# 4
# 5

# def functionname(a):
#     for i in a:
#         print(i)
# functionname({1,2,3,4,5})#by using dictionary in function
#o/p:1
# 2
# 3
# 4
# 5


# def functionname(a):
#     print(a)
# functionname(1,2,3,4,5,6,7)#here error will be displayed that means one variable can store one value.
#o/p:line 68, in <module>
#    functionname(1,2,3,4,5,6,7)
#TypeError: functionname() takes 1 positional argument but 7 were given



# * means arbitary argument
# def functionname(*a):
#     print(a)
# functionname(1,2,3,54,5,6,7)#here multiple values can store only single variable.
#o/p:(1, 2, 3, 54, 5, 6, 7)


# def functionname(**a):
#     print(a)
# functionname(name='kiran',age=21)#it displays dictionary type values.
#o/p:{'name': 'kiran', 'age': 21}


# nov_30(hclass)(but i do the work dec_4 mon)
# functions
# group of statements
# reusability


# types of functions
# 1.Builtin functions (or) predefined functions
# 2.user defined functions


# creating a parameterless function
# def function_name():
#      print("hi")
#      print("good morning")
#      print("how are you")
#      print("good bye")
# function_name()#it means calling a function
# o/p:hi
# good morning
# how are you
# good bye




# function with parameters
# def function_to_greet(name):
#      print(f"hi {name}!")
# function_to_greet("harish")
# o/p:hi harish!


#default arguments(or)default parameters
# def add(num1=1,num2=3):#default ga manam values ichamu
#      print(num2+num1)
# add()
# o/p:4


#default parameters
# def add(num1=1,num2=3):#default ga manam values ichamu
#      print(num2+num1)
# add(5,5)#function call chesina dagara values pass cheyakapote default values ni assign chestundi
# funtion call chesina dagara arguments pass cheste default values vunna manam ichina values ni assign chestudi

#positional arguements
# def add(a,b):
#      print(a+b)
# add(7,3)#here a value is 7,and b value is 3
# o/p:10

#keyword arguments
# def add(a,b):
#      print(a-b)
# add(a=30,b=20)
# o/p:10

#keyword arguments
# def add(a,b):
#      print(a-b)
# add(b=30,a=20)#with out order we can execute the functions
# o/p:-10


#variable-length & kwargs
# def display_sequence(a):
#      print(a)
# display_sequence(1,2,3,4,5)
# o/p:display_sequence(1,2,3,4,5)
# TypeError: display_sequence() takes 1 positional argument but 5 were given


# variable-length & kwargs(first type)
# def display_sequence(*a):
#       print(a)
# display_sequence(1,2,3,4,5)#number of values ichinapudu one argument iste error vachidi , appudu variable length argument * ni
# use cheste output tuple lo form chestundi
# o/p:(1, 2, 3, 4, 5)


#variable-length & kwargs(second type)
# def display_sequence(**a):
#       print(a)
# display_sequence(a='1',b='2',c='3',d='4',e='5')#double star ichinapudu keys , values both ivali appudu output dictionary format lo vastundi
# o/p:{'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}




# def display_sequence(*args):
#     print(args)
#     for i in args:
#          print(i)
# display_sequence(1, 2, 3, 0, 4, 89, 100)
# o/p:(1, 2, 3, 0, 4, 89, 100)
# 1
# 2
# 3
# 0
# 4
# 89
# 100



# def display_keypairs(**args):
#      print(args)
#      for k, v in args.items():
#          print(k, v)
# display_keypairs(user="harish", userid=123)
# display_keypairs(user="harish1", userid=1234,gender="male")
# o/p:{'user': 'harish', 'userid': 123}
# user harish
# userid 123
# {'user': 'harish1', 'userid': 1234, 'gender': 'male'}
# user harish1
# userid 1234
# gender male


#   lst = []
# for i in range(n + 1):
#          lst.append(i)
# #return ldef generate_natural_nums(n):
#   st
# #values = generate_natural_nums(10)
# #print(values)
# return lst
#
#
# a = 1,2,3,4
# print(a)
#
#
# def test():
#     return 1, 3, 5, 6
# print(test())



#recursion function
#function calling itself is known as recursive function
#this concept is called recursion

#adv:
#1.clean code
#2.reduce no of lines

#disadv
#1.not memory efficient
#2.hard to debug

# def factorial(n):
#      if n == 0:
#           return 1
#      return n*factorial(n-1)
# print(factorial(5))
# o/p:120


#by using import method
# import sys
# print(sys.setrecursionlimit(200))
# print(sys.getrecursionlimit())#here it gives the limit is hello 1 to hello 999
# def greet(num):
#      num = num + 1
#      print("hello", num)
#      greet(num)
# greet(0)
# o/p:hello 1 ----- hello 199

#6/12/23(hclass)

#lambda functions

# 1. Lambda functions are the ananonymous functions which do not have any name.
# 2. We can have any number of arguments and only one expression.
# 3. No return keyword
# 4. We can use lambda for short operations.
# 5. improves code readability and reduces the code.
# 6. mostly we use lambda functions with map, filter, reduce

#example programs

# is_even_list=[lambda arg=x: arg*10 for x in range(1,5)]
# print(is_even_list)#it displays lambda object
# o/p:[<function <lambda> at 0x0000026E71C1A2A0>, <function <lambda> at 0x0000026E73B1E160>, <function <lambda> at 0x0000026E73B1EB60>, <function <lambda> at 0x0000026E73B1EC00>]


# is_even_list=[lambda arg=x: arg*10 for x in range(1,5)]
# print(is_even_list[0]())
# for item in is_even_list:
#     print(item)
#o/p:10
# <function <lambda> at 0x000001AA1D68A2A0>
# <function <lambda> at 0x000001AA1F5CE160>
# <function <lambda> at 0x000001AA1F5CEB60>
# <function <lambda> at 0x000001AA1F5CEC00>

# lam_fun=lambda x,y,z,k:(x*y*z)+k
# print(lam_fun(1,2,3,4))
#o/p:10

#concept:ternary operator
# trueresult if condition else falseresult
# trueresult1 if condition else trueresult2 if condition else falseresult

#example:

# age=2
# if age>18:
#     print("eligible")
# else:
#     print("not eligible")
#o/p:not eligible

# age=20
# result="eligible" if age>18 else "not eligible"
# print(result)
# o/p:eligible

#map(),filter(),reduce()
# 1.map()
# syntax:map(func,seq)

#ex-1
# lst=[10,20,30,40,50]
# result=tuple(map(lambda x:x+5,lst))
# print(result)
# o/p:(15, 25, 35, 45, 55)


#ex-2
# names=("harish","dinesh","naveen","ratnam")
# emails=set(map(lambda name: name + "@ttt.com",names))
# print(emails)
# o/p:{'harish@ttt.com', 'ratnam@ttt.com', 'dinesh@ttt.com', 'naveen@ttt.com'}

#2.filter()
#syntax:filter(func,seq)

#ex_1
# number_list=[i for i in range(1,1000000)]
#print(number_list)
#display the 1 to 9999999

#ex_2

# number_list=[i for i in range(1,10)]
# even_num_list=list(filter(lambda x:x%2==0,number_list))
# odd_num_list=list(filter(lambda x:x%2 !=0,number_list))
# print(even_num_list)
# print(odd_num_list)
#o/p:[2, 4, 6, 8]
#[1, 3, 5, 7, 9]


#ex-2

# number_list=[i for i in range(1,100)]
# even_lst=[]
# print(number_list)#it displays 1 to 99 by using square brackets
# for i in number_list:
#     if i % 2 == 0:
#         even_lst.append(i)
# print(even_lst)#it displays even numbers 1 to 100 by using sruare brackets


#ex-4
import time

# et=ending time
# st=starting time

# number_list = [i for i in range(1, 100)]
# print(number_list)
#
# st = time.time()
# even_num_list = list(filter(lambda x: x % 2 == 0, number_list))
# odd_num_list = list(filter(lambda x: x % 2 != 0, number_list))
# et = time.time()
# print(et - st)
# print(even_num_list)
# print(odd_num_list)
#o/p:it displays time is 0.0



#ex-4

import time
# # #
# st = time.time()
# print(st)
# even_lst = []
# for i in number_list:
#     if i % 2 == 0:
#         even_lst.append(i)
# et = time.time()
# print(et)
# print(et - st)


##########
# reduce
# syntax
# ===========
# from functools import reduce
# reduce(func, seq)

# from functools import reduce
#
# lst = [x for x in range(1, 11)]
# res = reduce(lambda a, b: a + b, lst, 5)
# print(res)

#dec_30(ganga sir class):
# w3 school_function ex:
# def my_function():
#   print("Hello from a function")#calling function
# my_function()#without using this function it cannot display output
# o/p:Hello from a function
