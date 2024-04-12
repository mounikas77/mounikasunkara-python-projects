# jan-3
#functions:(meme programmers)
#* grouping a block of code
#* sub part of a program
#########
# when we declare functions
### to organize the code
#### code reusability
### write once use multiple times ######
### ex: like cone designs--one design with different colours
## ex: one function you pass the different parameters

#functions are two types:
# 1.built in functions
# 2.user defined functions
# #1.built in functions:
# * already creating functions just we use this functions
# #ex:input(),print(),round(),abs().
# #2.user defined functions:
# * our own creation of functions
#
# # how to declare a function
# # syntax:
# def functionName():
#     Block of code
#
# use function name as camel case or snake case naming convention
############
# def sampleFunction():
#     print("function created succesfully")
# sampleFunction()# this means function calling for one time

###########
# def sampleFunction():
#      print("function created succesfully")
# sampleFunction()# this means function calling for one time
# sampleFunction()
# sampleFunction()
# sampleFunction()#this means function calling for four times

############
#ex:
# def addition():
#     a=10
#     b=10
#     c=a+b
#     print(c)
# add1=addition()
# print(add1)
# o/p:20
# None
#################
# def addition():
#     a=10
#     b=10
#     c=a+b
#     return c
# print(addition())
#o/p:20
###############
# def addition():
#     a=10
#     b=10
#     c=a+b
#     return c
# add1=addition()
# print(add1)
# o/p:20
##################
##### ANOTHER WAY FOR DEFINING FUNCTIONS
# SYNTAX FOR FUNCTION
# def functionName(parameters):
#     function body/block
#     function call syntax:
#     functionName(arguements)
######################################
# def addNumbers(number1,number2):
#     return number1+number2
# print(addNumbers(3,7))
# o/p:10
############
# def addNumbers(number1,number2):
#     return number1+number2
# print(addNumbers(3))
# o/p:TypeError: addNumbers() missing 1 required positional argument: 'number2'
#############
# def addNumbers(number1,number2):
#     return number1+number2
# print(addNumbers(3,7))
# print(addNumbers(30,70))
# print(addNumbers(20,20))
# o/p:10
# 100
# 40
################(hari anna)
#a=range(10)
# print(type(a))
# print(a)
# o/p:
# <class 'range'>
# range(0, 10)

###########################################################
#practice:(practice for functions)
# def samplefunction():
#     print("python developer")
# samplefunction()
# o/p:python developer
############
# def samplefunction():
#     print("python developer")
# samplefunction()
# samplefunction()
# samplefunction()
# samplefunction()
# o/p:
#
# python developer
# python developer
# python developer
# python developer
#########################
# def addition():
#     a=10
#     b=10
#     c=a+b
#     print(c)
# addition()
#o/p:20
###############
# def addition():
#     a=10
#     b=10
#     c=a+b
#     print(c)
# add1=addition()
#print(add1)
#o/p:20
#none
################
# def addition():
#     a=10
#     b=10
#     c=a+b
#     return c
# addition()
# o/p:blank page display
##########################
# def addition():
#     a=10
#     b=10
#     c=a+b
#     return c
# print(addition())
# o/p:20

############
# def addition():
#     a=10
#     b=10
#     c=a+b
#     return c
# add1=addition()
# print(add1)
# o/p:20

#############
# def addNumbers(number1,number2):
#     return number1+number2
# print(addNumbers(3,7))
# o/p:10

################
# def addNumbers(number1,number2):
#     return number1+number2
# print(addNumbers(3,7))
# print(addNumbers(30,70))
# print(addNumbers(20,70))
# print(addNumbers(13,7))
# o/p:10
# 100
# 90
# 20
##############
# def addition(a,b,c=10):
#     a=10
#     b=10
#     d=a+b+c
#     return d
# print(addition(1,2))
#o/p:30
# def addition(a,b,c=10):
#     a=10
#     b=10
#     d=a+b+c
#     return c
# print(addition(1,2))
#o/p:10
##############
# def values(*args):
#     print(args)
# values(1,2,3)
# values(1,2,3,4,5)
# o/p:(1, 2, 3)
# (1, 2, 3, 4, 5)
################
# def values(**args):
#     print(args)
# values(1,2,3)
# values(1,2,3,4,5)
# o/p:TypeError: values() takes 0 positional arguments but 3 were given
########################
# def values(**args):
#     print(args)
# values(a=1,b=2)
#o/p:{'a': 1, 'b': 2}
#############

# d = {"a": 2, "b": 1, "c": 0, "d": 12, "e": -1}
#
# # Sort dictionary by keys
# sorted_by_keys = dict(sorted(d.items()))
# print("Sorted by keys:", sorted_by_keys)
#
# # Sort dictionary by values
# sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
# print("Sorted by values:", sorted_by_values)
# print(d.items())



###############################
# types of arguments in functions:
# parameters-the values given at the time of declaration
# arguments-the values given at the time of call
##########
##types
#1.positional arguments
#2.keyword arguments
#3.default arguments
#4.variable length arguments (or) arbitary arguments
###########
# 1. positional arguments
######
# def function(a,b,c):
#     return a,b,c
# function(10,20,30)
# o/p:display the empty page

##########
# def function(a,b,c):
#     return a,b,c
# print(function(10,20,30))
# #o/p:display the empty page
#############

# def function(a,b,c):
#     return a,b,c
# a=10
# b=20
# c=30
# print(function(b,a,c))
# o/p:(20, 10, 30)

#######

# def function(a,b,c):
#     return a,b,c
# a=10
# b=20
# c=30
# print(function(b,a))
#o/p:TypeError: function() missing 1 required positional argument: 'c'

##############
# def function(a,b,c):
#     return a,b,c
# a=10
# b=20
# c=30
# print(function(a,b))
# o/p:TypeError: function() missing 1 required positional argument: 'c'

###############
#######2.keyword arguments
# def function(a,b,c):
#     return a,b,c
# print(function(a=10,b=20,c=30))
#o/p:(10, 20, 30)

# ##############
# def function(a,b,c):
#     return a,b,c
# print(function(b=20,a=10,c=30))
# o/p:(10, 20, 30)

###########
# def function(a,b,c):
#     return c,a,b
# print(function(b=20,a=10,c=30))
# o/p:(30, 10, 20)

##############3
# def function(a,b,c,d):
#     return c,a,b,d
# print(function(a=10,c=30))
# o/p:TypeError: function() missing 2 required positional arguments: 'b' and 'd'
#######here main thing is how many parameters are passed into the function
#################

####3.default arguments
# def function(a=10,b=20,c=30):
#     return a,b,c
# print(function())
# o/p:(10, 20, 30)

##############
# def function(a=10,b=20,c=30,e=40):
#     return a,b,c,d
# print(function())
# o/p:NameError: name 'd' is not defined. Did you mean: 'id'?
##############

# def function(a=10,b=20,c=30):
#     return a,b,c
# print(function(1,2,3))
# o/p:(1, 2, 3)
#############3
# def function(a=10,b=20,c=30):
#     return a,b,c
# print(function(1,2,3,4,5))
# o/p:TypeError: function() takes from 0 to 3 positional arguments but 5 were given

##############
# def function(a=10,b=20,c=30):
#     return a,b,c
# print(function())
# o/p:(10, 20, 30)
#############
# def function(a=10,b=20,c=30,d=40):
#     return a,b,c,d
# print(function())
# o/p:(10, 20, 30, 40)

#############
# def function(a=10,b=20,c=30,d=40):
#     return a,b,c,d
# print(function(1))
# o/p:(1,20, 30, 40)

#############
# def function(a=10,b=20,c=30,d=40):
#     return a,b,c,d
# print(function(1,2))
# o/p:(1, 2, 30, 40)

#################
# def function(a=10,b=20,c=30,d=40):
#     return a,b,c,d
# print(function(b=90,c=80))
# o/p:(10, 90, 80, 40)

############
####4.variable length arguments (or) arbitary arguments
# def sample(*args):
#     return args
# print(sample(1,2,3,4,5))
# o/p:(1, 2, 3, 4, 5)
###########
# def sample(args):
#     return args
# print(sample(1,2,3,4,5))
# o/p:TypeError: sample() takes 1 positional argument but 5 were given

################
# def sample(args):
#     return args
# print(sample(1))
# o/p:1

# ############
# def sample(args):
#     return args
# print(sample(1,2))
# o/p:TypeError: sample() takes 1 positional argument but 2 were given
###############
# def sample(*args):
#     return args
# print(sample())
# o/p:()
###############
# def sample(*mouni):
#     return mouni
# print(sample())
# o/p:()
###############3
# def sample(**kwargs):
#     return kwargs
# print(sample(a=10,b=20,c=30,d=40))
# o/p:{'a': 10, 'b': 20, 'c': 30, 'd': 40}
#################
# def sample(**kwargs):
#     return kwargs
# print(sample())
#o/p:{}

###############
# def sample(**mouni):
#     return mouni
# print(sample(a=10,b=20,c=30))
# o/p:{'a': 10, 'b': 20, 'c': 30}

#################################################

##practice for functions in types of arguments:
#1.positional arguments
#2.default arguments
#3.key word arguments
#4.variable length arguments (or) arbitary arguments
#################
############example function programs
####1.addition of two numbers
######Example 1: Python Function Arguments
#function with two arguments
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ",sum)
#
# # function call with two values
# add_numbers(5, 4)
# o/p:Sum:  9
#''''''In the above example, we have created a function named add_numbers() with arguments: num1 and num2.''''''
##################
###Example 2: Function return Type
# function definition
# def find_square(num):
#     result = num * num
#     return result
#
# # function call
# square = find_square(3)
#
# print('Square:',square)
# Output: Square: 9
# ''''''The return Statement in Python
# A Python function may or may not return a value. If we want our function to return some value to a function call, we use the return statement. For example,
# #def add_numbers():
#     ...
#     return sum
####Here, we are returning the variable sum to the function call.
####Note: The return statement also denotes that the function has ended. Any code after return is not executed.
######In the above example, we have created a function named find_square(). The function accepts a number and returns the square of the number.

#################
#####Example 3: Add Two Numbers
##### function that adds two numbers
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
#
# # calling function with two values
# result = add_numbers(5, 4)
#
# print('Sum: ', result)
# Output: Sum: 9
###################
# Python Library Functions
# In Python, standard library functions are the built-in functions that can be used directly in our program. For example,
#
# print() - prints the string inside the quotation marks
# sqrt() - returns the square root of a number
# pow() - returns the power of a number
# These library functions are defined inside the module. And, to use them we must include the module inside our program.
#
# For example, sqrt() is defined inside the math module.
############
# Example 4: Python Library Function
# import math
#
# # sqrt computes the square root
# square_root = math.sqrt(4)
#
# print("Square Root of 4 is",square_root)
#
# # pow() comptes the power
# power = pow(2, 3)
#
# print("2 to the power 3 is",power)
# o/p:Square Root of 4 is 2.0
# 2 to the power 3 is 8
##########
# In the above example, we have used
#
# math.sqrt(4) - to compute the square root of 4
# pow(2, 3) - computes the power of a number i.e. 23
# Here, notice the statement,

# import math
# Since sqrt() is defined inside the math module, we need to include it in our program.
##############
############Benefits of Using Functions
#1. Code Reusable - We can use the same function multiple times in our program which makes our code reusable. For example,

# function definition
# def get_square(num):
#     return num * num
#
# for i in [1,2,3]:
#     # function call
#     result = get_square(i)
#     print('Square of',i, '=',result)
# o/p:Square of 1 = 1
# Square of 2 = 4
# Square of 3 = 9

################
# In the above example, we have created the function named get_square() to calculate the square of a number. Here, the function is used to calculate the square of numbers from 1 to 3.
#
# Hence, the same method is used again and again.
#2. Code Readability - Functions help us break our code into chunks to make our program readable and easy to understand.
########################
####################practice(sb tech tuts)
#1.positional arguments
# def add(x,y):
#     sum=x+y
#     print(sum)
# add(100,200)
# o/p:300
#########
# def add(x,y):
#     sum=x+y
#     print(sum)
# add(100)
#o/p:TypeError: add() missing 1 required positional argument: 'y'
###########
# def add(x,y):
#     sum=x+y
#     print(sum)
# add(100,200,300)
# o/p:TypeError: add() takes 2 positional arguments but 3 were given

###################
#2.default arguments
# def add(x=100,y=200):
#     sum=x+y
#     print(sum)
# add(10,20)
# o/p:30
##############
# def add(x=100,y=200):
#     sum=x+y
#     print(sum)
# add(10)
#o/p:210
###########
# def add(x=100,y=200):
#     sum=x+y
#     print(sum)
# add()
# o/p:300
###########
# def add(x=100,y):
#     sum=x+y
#     print(sum)
# add()
# o/p:SyntaxError: parameter without a default follows parameter with a default
#############
# def add(x=100,200):
#     sum=x+y
#     print(sum)
# add()
# o/p:SyntaxError: invalid syntax
################
#3.keyword arguments
# def add(x,y=20,z=30):
#     sum=x+y+z
#     print(sum)
# add(10,20,30)
# o/p:60
############
# def add(x,y=20,z=30):
#     sum=x+y+z
#     print(sum)
# add(10,y=40)
#o/p:80
###########
# def add(x,y=20,z=30):
#     sum=x+y+z
#     print(sum)
# add(10,z=20)
# o/p:50
##############
# def add(x,y=20,z=30):
#     sum=x+y+z
#     print(sum)
# add(20,z=20,y=10)
# #o/p:50
#############
# def add(x,y=20,30):
#     sum=x+y+z
#     print(sum)
# add(20,z=20,y=10)
# o/p:SyntaxError: invalid syntax
###############
#4.variable length (or) arbitary arguments
# def robo(*mouni):
#     print(mouni)
# robo(10,20,30,40)
# o/p:(10, 20, 30, 40)
#############
# def robo(*mouni):
#     print(mouni)
# robo(10,20)
#o/p:(10, 20)
###########
# def robo(*mouni):
#     print(mouni)
# robo("mouni","ravi","raju")
# o/p:('mouni', 'ravi', 'raju')
############
# def robo(*mouni):
#     print(mouni)
# robo(1:"mouni",2:"ravi",3:"raju")
# o/p:SyntaxError: invalid syntax
##############
# def robo(**mouni):
#     print(mouni)
# robo(1:"mouni",2:"ravi",3:"raju")
# o/p:         ^
# SyntaxError: invalid syntax
############
# def robo(**mouni):
#     print(mouni)
# robo("1":"mouni","2":"ravi","3":"raju")
# #o/p:SyntaxError: invalid syntax
##################

#jan_6
# vide0-1
# 1.no return type no arguments
# def add():
#     a=100
#     b=200
#     sum=a+b
#     print(sum)
# add()
# o/p:300
###############
#2.no return type with arguments
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(100,200)
# o/p:300
###############
#3.with return type no arguments
# def add():
#     a=100
#     b=200
#     return a+b
# print(add())
# (or)
# sum=add()
# print(sum)
# o/p:300
# 300
#################
#4.with return type with arguments
# def add(a,b):
#     return a+b
# sum=add(100,200)
# print(sum)
# o/p:300
################################
#practice
##1.no returntype no arguments
# def add():
#     a=10
#     b=20
#     sum=a+b
#     print(sum)
# add()
# o/p:30

#############
#2.no return type with arguments
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(10,30)
# o/p:40

############
#3.with return type no arguments
# def add():
#     a=10
#     b=20
#     return a+b
# sum=add()
# print(sum)
#o/p:30
####################
#4.with return type with arguments
# def add(a,b):
#     return a+b
# sum=add(10,20)
# print(sum)
# o/p:30
#############55555







