#november_22
#program_1
'''Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence
on a single line.'''


# l=[]
# for num in range(2000,3201):
#     if (num%7==0) and (num%5!=0):
#         l.append(num)
#print(l)


#program_2
''' Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a
single line.'''

# def fact(x):
#     if x==0 :
#         return 1
#     else:
#         return x*fact(x-1)
# x=int(input("enter a value: "))
#print(fact(x))


#program_3
''' With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print the
dictionary.'''

# n=int(input("enter a value: "))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#print(d)


#program_4
''' Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every
number.'''

# values=(input("enter a values: "))
# l=values.split()
# t=tuple(l)
# print(l)
# print(t)


#program_5
# class inputoutputstring(object):
#     def __init__(self):
#         self.s=" "
# def getstring(self):
#     self.s=(input("enter a string: "))
#     def printstring(self):
#         print(self.s.upper())
# strobj=inputoutstring()
# strobj.getstring()
# strobj.printstring()


print(\"mounika is a python programmer"\)