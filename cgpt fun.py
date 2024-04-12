#functions practice(jan-5)
#1.Calculate the Area of a Circle:
# import math
#
# def calculate_circle_area(radius):
#     return math.pi * radius**2
#
# # Example usage:
# radius = 5
# area = calculate_circle_area(radius)
# print(f"The area of the circle with radius {radius} is: {area}")
# o/p:Enter the radius of the circle: 4
# The area of the circle is: 50.26548245743669
##################
#2.Check if a Number is Prime:
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
# o/p:Enter a number: 2
# 2 is a prime number.
#################
#3.Calculate Factorial:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# num = int(input("Enter a number: "))
# print(f"The factorial of {num} is: {factorial(num)}")
# o/p:Enter a number: 5
# The factorial of 5 is: 120
##################
#4.Reverse a String:
# def reverse_string(s):
#     return s[::-1]
#
# text = input("Enter a string: ")
# reversed_text = reverse_string(text)
# print(f"The reversed string is: {reversed_text}")
# o/p:Enter a string: mounika
# The reversed string is: akinuom
###################



