#140 plus practice programs
#1.print("hello python")

# Addition
# num1 = float(input("Enter the first number for addition: "))
# num2 = float(input("Enter the second number for addition: "))
# sum_result = num1 + num2
# print(f"sum: {num1} + {num2} = {sum_result}")
# o/p:Enter the first number for addition: 5
# Enter the second number for addition: 6
# sum: 5.0 + 6.0 = 11.0

# subtraction
# num1=int(input("enter the first number for sub :"))
# num2=int(input("enter the second value for sub :"))
# sub_result=num1-num2
# print(f"sub:{num1}-{num2}={sub_result}")
# o/p:enter the first number for sub :10
# enter the second value for sub :20
# sub:10-20=-10

# 2.num1=float(input("enter valu for addition:"))
# num2=float(input("enter valu for addition:"))
# sum_result=num1+num2
# print(f"sum:{num1}+{num2}={sum_result}")
# o/p:enter valu for addition:30
# enter valu for addition:30
# sum:30.0+30.0=60.0

# ############
# num1=int(input("enter valu for addition:"))
# num2=int(input("enter valu for addition:"))
# sum_result=num1+num2
# print(f"sum:{num1}+{num2}={sum_result}")
# o/p:enter valu for addition:30
# enter valu for addition:40
# sum:30+40=70

###################
# Division
# num3 = float(input("Enter the dividend for division: "))
# num4 = float(input("Enter the divisor for division: "))
# if num4 == 0:
#  print("Error: Division by zero is not allowed.")
# else:
#  div_result = num3 / num4
#  print(f"Division: {num3} / {num4} = {div_result}")

#  o/p:Enter the dividend for division: 25
# Enter the divisor for division: 5
# Division: 25.0 / 5.0 = 5.0

################
# num3=float(input("enter a dividend value for division:"))
# num4=float(input("enter a divisior value for division:"))
# if num4==0:
#     print("error:division by zero is not allowed")
# else:
#     div_result=num3/num4
#     print(f"{num3}/{num4}={div_result}")
# o/p:enter a dividend value for division:10
# enter a divisior value for division:2
# 10.0/2.0=5.0

# num3=int(input("enter a dividend value for division:"))
# num4=int(input("enter a divisior value for division:"))
# if num4==0:
#     print("error:division by zero is not allowed")
# else:
#     div_result=num3/num4
#     print(f"{num3}/{num4}={div_result}")
# o/p:enter a dividend value for division:10
# enter a divisior value for division:5
# 10/5=2.0


# num3=int(input("enter a dividend value for division:"))
# num4=int(input("enter a divisior value for division:"))
# if num4==0:
#     print("error:division by zero is not allowed")
# else:
#     div_result=num3//num4
#     print(f"{num3}//{num4}={div_result}")
# o/p:enter a dividend value for division:10
# enter a divisior value for division:5
#10//5=2  #this means output is int value.// it returns the flor division (int)value.
############################
#  area of triangle
#Input the base and height from the user
#base = float(input("Enter the length of the base of the triangle: "))
#height = float(input("Enter the height of the triangle: "))
#Calculate the area of the triangle
#area = 0.5 * base * height
#Display the result
#print(f"The area of the triangle is: {area}")
#o/p:Enter the length of the base of the triangle: 10
#Enter the height of the triangle: 20
#The area of the triangle is: 100.0


# base=float(input("enter the base of a triangle:"))
# height=float(input("enter a height of a triangle:"))
# area=0.5*base*height
# print(f"area of a triangle:{area}")
# o/p:enter the base of a triangle:2
# enter a height of a triangle:3
# area of a triangle:3.0
########################

# Input two variables
# a = input("Enter the value of the first variable (a): ")
# b = input("Enter the value of the second variable (b): ")
# Display the original values
# print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
# temp = a
# a = b
# b = temp
# Display the swapped values
# print(f"Swapped values: a = {a}, b = {b}")
# o/p:Enter the value of the first variable (a): 5
# Enter the value of the second variable (b): 9
# Original values: a = 5, b = 9
# Swapped values: a = 9, b = 5


#swapped means it change the a value is b and b value is a
# a=input("enter the value of first variable (a):")
# b=input("enter the value of first variable (b):")
# print(f"original values=a={a},b={b}")
# temp=a
# a=b
# b=temp
# print(f"swapped elements:a={a},b={b}")
# o/p:enter the value of first variable (a):5
# enter the value of first variable (b):9
# original values=a=5,b=9
# swapped elements:a=9,b=5

#######################
# import random
# print(f"Random number:{random.randint(1,100)}")
#o/p:60

# import random
# print(f"Random number:{random.randint(1,100)}")
# o/p:34

###########################
#kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
#conversion_factor = 0.621371
#miles = kilometers * conversion_factor
#print(f"{kilometers} kilometers is equal to {miles} miles")
# o/p:
# enter distance in kilometers : 100
# 100.0 kilometer is equal to 62.137100000000004 miles


# kilometers=float(input("enter distance in kilometers : "))
# convertion_factor=0.621371
# miles = kilometers * convertion_factor
# print(f"{kilometers} kilometer is equal to {miles} miles")
# o/p:enter distance in kilometers : 100
# 100.0 kilometer is equal to 62.137100000000004 miles


###########################
#celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
# o/p:Enter temperature in Celsius: 37
# 37.0 degrees Celsius is equal to 98.6 degrees Fahrenheit

#################################
# import calendar
# year=int(input("enter year:"))
# month=int(input("enter month"))
# cal=calendar.month(year,month)
# print(cal)
# o/p:enter year:2024
# enter month8
#     August 2024
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

############################
# import math
# # Input coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# # Calculate the discriminant
# discriminant = b**2 - 4*a*c
# # Check if the discriminant is positive, negative, or zero
# if discriminant > 0:
#  # Two real and distinct roots
#  root1 = (-b + math.sqrt(discriminant)) / (2*a)
#  root2 = (-b - math.sqrt(discriminant)) / (2*a)
#  print(f"Root 1: {root1}")
#  print(f"Root 2: {root2}")
# elif discriminant == 0:
#  # One real root (repeated)
#  root = -b / (2*a)
#  print(f"Root: {root}")
# else:
#  # Complex roots
#  real_part = -b / (2*a)
#  imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#  print(f"Root 1: {real_part} + {imaginary_part}i")
#  print(f"Root 2: {real_part} - {imaginary_part}i")
#
# o/p:Enter coefficient a: 1
# Enter coefficient b: 4
# Enter coefficient c: 8
# Root 1: -2.0 + 2.0i
# Root 2: -2.0 - 2.0i

##########################
# a = 5
# b = 10
# # Swapping without a temporary variable
# a, b = b, a
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# a=10
# b=16
# a,b=b,a
# print("after swapping:")
# print("a=",a)
# print("b=",b)
#o/p:after swapping:
# a= 16
# b= 10

#########################

# num = float(input("Enter a number: "))
# if num > 0:
#  print("Positive number")
# elif num == 0:
#  print("Zero")
# else:
#  print("Negative number")
# o/p:Enter a number: 9
# Positive number
# o/p:Enter a number: -4
# Negative number

# num=float(input("enter a number : "))
# if num>0:
#     print("positive number")
# elif num==0:
#     print("zero")
# else:
#     print("negative number")
# o/p:enter a number : 0
# zero
# o/p:enter a number : 39
# positive number


#############################

# num = int(input("Enter a number: "))
# if num%2 == 0:
#  print("This is a even number")
# else:
#  print("This is a odd number")
# o/p:Enter a number: 10
# This is a even number
# o/p:Enter a number: 37
# This is a odd number

# for num in range(1, 11):
#     if num % 2 == 0:
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")

# o/p:1 is an odd number
# 2 is an even number
# 3 is an odd number
# 4 is an even number
# 5 is an odd number
# 6 is an even number
# 7 is an odd number
# 8 is an even number
# 9 is an odd number
# 10 is an even number

# for num in range(1, 110):
#     if num % 2 == 0:
#         print(num)
# o/p:it displays the even numbers for 1 to 110


# for num in range(1, 11):
#     print(num)
# o/p:it displays complete 1 to 10 values.




#############################
# year = int(input("Enter a year: "))
# # divided by 100 means century year (ending with 00)
# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#  print("{0} is a leap year".format(year))
# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#  print("{0} is a leap year".format(year))
# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#  print("{0} is not a leap year".format(year))
#  o/p:Enter a year: 2024
# 2024 is a leap year
# o/p:Enter a year: 2025
# 2025 is not a leap year

#################################
# num = int(input("Enter a number: "))
# # define a flag variable
# flag = False
# if num == 1:
#  print(f"{num}, is not a prime number")
# elif num > 1:
#  # check for factors
#     for i in range(2, num):
#  if (num % i) == 0:
#  flag = True # if factor is found, set flag to True
#  # break out of loop
#  break
#  # check if flag is True
# if flag:
#  print(f"{num}, is not a prime number")
# else:
#  print(f"{num}, is a prime number")

 ########################
 # Python program to display all the prime numbers within an interval
 # lower = 1
 # upper = 10
 # print("Prime numbers between", lower, "and", upper, "are:")
 # for num in range(lower, upper + 1):
 #     # all prime numbers are greater than 1
 #     if num > 1:
 #         for i in range(2, num):
 #             if (num % i) == 0:
 #             break
 #     else:
 #         print(num)


