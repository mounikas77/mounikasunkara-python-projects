#1)EXAMPLE OF USING IF_ELSE LADDER IN PYTHON
# z = 1000
# if  z == 100:
#      print("z is 100")
# elif z == 200:
#      print("z is 200")
# elif z == 300:
#      print("z is 300")
# elif z == 1000:
#     print("z is 1000")
# else:
#      print("z is unknown")



#2)A)PYTHON IF_ELSE STATEMENTS USING RELATIONAL OPERATORS.
# m=25
# n=25
# if(m>n):
#     print("m is greaterthan n")
# elif m == n:
#     print("m is equal to n")
# else:
#     print("m is lessthan n")



#2)B)PYTHON IF_ELSE STATEMENTS USING RELATIONAL OPERATOR.
# p=30
# q=20
# if((p < q) | (p == q)):
#     print(" either p is lessthan q or p is equal to q")
# elif((p == 30) & (q == 30)):
#     print("p and q are equal")
# elif(p != q):
#     print("p is not equal to q")
# else:
#     print("p is greaterthan q")



#3)PYTHON IF_ELSE STATEMENTS USING TRUE OR FALSE.
# if True:
#     print("statement is true")
# else:
#     print("statement is false")



#4)A)PYTHON NESTED IF_ELSE STATEMENTS.
# z=10
# if z<0:
#     print("z is lessthan 0")
# else:
#     if z<5:
#         print("z is lessthan 5")
#     else:
#         print("z is greater than")


#4)B)PYTHON NESTED IF_ELSE STATEMENTS.
# count=200
# if count<400:
#     print("The count is below 400")
#     if count<300:
#         print("The count is below 300")
#     else:
#         print("The count is lessthan 400 and greaterthan or equal to 300")


#5.PYTHON IF_ELSE STATEMENTS USING MEMBERSHIP OPERATORS(IN,NOT IN)
# letter="t"
# if letter in "python":
#     print("yes")
# else:
#     print("no")
# if letter not in 'java':
#         print("yes")
# else:
#         print("no")


#6)A)PYTHON SHORTHAND IF_ELSE STATEMENTS(IF_ELSE IN ONE LINE).
# x=55
# y=110
# print("x") if x > y else print("y")

#6)B)PYTHON SHORTHAND IF_ELSE STATEMENTS(IF_ELSE IN ONE LINE).
# s = 200
# r = 400
# if s!=r:
#     print("s is not equal to r")
# else:
#     print("s is equal to r")

#7.PYTHON IF_ELSE SYATEMENTS USING AND OPERATOR.
# s=3000
# t=1000
# if s>t and t%2 ==0:
#     print("Both conditions are true")


#8.PYTHON IF_ELSE STATEMENTS USING OR OPERATOR.
# x=200
# y=1000
# if((x<y) or (y%11 == 0)):
#     print("Atleast one condition is true")


#9.USING PASS INSIDE IF_ELSE STATEMENTS IN PYTHON.
# x = 100
# y = 10
# if x > y:
#     pass



#10.PYTHON IF_ELSE STATEMENTS USING LAMBDA FUNCTION.
# h = lambda k: k**5 if k % 5 == 0 else k**7
# print(h(5))
# print(h(7))


#11.PYTHON IF_ELSE STATEMENTS USING INPUT TAKEN FROM THE USER.
# print("enter a number: ")
# number=int(input())
# if number < 20:
#     print("the number lessthan 20")
# elif number == 20:
#     print("the number equal to 20")
# else:
#     print("the number is greaterthan 20")



#12.PYTHON PROGRAM TO CHECK IF THE NUMBER IS DIVISIBLE BY 5 OR NOT.
# d=int(input("enter a number: "))
# if (d % 5 == 0):
#     print("number is divisible by 5")
# else:
#     print("number is not divisible by 5")

#13.PYTHON PROGRAM TO CHECK IF THE NUMBER IS ODD OR EVEN.
# number=int(input("enter a number: "))
# if number % 2 == 0:
#     print("given number is even")
# else:
#     print("given number is odd")


#14.PYTHON PROGRAM TO CHECK IF THE NUMBER IS DIVISIBLE BY BOTH 5 AND 7 OR NOT
# number=int(input("enter a number: "))
# if (number%5 == 0) and (number%7 == 0):
#     print("number is divisible by both 5 and 7")
# else:
#     print("number is not divisible by both 5 and 7")

#12/12/2023
#examples in list in utube:how many times number will be displayed program.
# numbers=[1,2,3,4,5,2,2,6,7]
# target=int(input('enter the number to find the number of occurance:'))
# counter=0
# for number in numbers:
#     if number == target:
#         counter += 1
# print(f"the number {target} occurs {counter} times in the list")
# o/p:enter the number to find the number of occurance:2
# the number 2 occurs 3 times in the list

#13/12/2023
#list methods example program:
# mylist=[1,2,3,4,5,6,7,8]
# print(mylist[0])#it gives the index position 0 answer
# print(mylist[3])#it gives the index position 3 answer
# mylist.append(9)#it add the 9 of the last position of the list
# print(mylist)
# mylist.insert(2,7)#it insert the value 7 at the index position 2 place
# print(mylist)
# mylist.remove(4)#it removes the value 4 at the starting order of the position
# print(mylist)
# poppedelement=mylist.pop(2)#it removes the element 7 at the index position 2
# print(poppedelement)
# print(mylist)
# slicedlist=mylist[1:4]#it displays the elements index position 1 to index position 3.
# print(slicedlist)
# print(mylist)
# length=len(mylist)#it displays the length of the mylist
# print(length)
# print(mylist)
# mylist.sort()
# print(mylist)#it displays the sorting list at the assending order
# mylist.reverse()
# print(mylist)#it displays the list in reverse order
# ispresent=3 in mylist
# print(ispresent)#it gives true that means the value 3 is in the list other it rerurns false
# newlist=mylist+[10,11,12]
# print(newlist)#it add the list into newlist
# print(mylist)
# count=mylist.count(7)
# print(count)#it displays the value 7 that means how many times it repeated in the given list
# print(mylist)
# copiedlist=mylist.copy()
# print(copiedlist)#it displays the mylist is copied for the copiedlist
# maximum=max(mylist)
# print(maximum)#it displays the maximum element for the given mylist
# minimum=min(mylist)
# print(minimum)#it diplays the minimum element for the given mylist
# sumvalue=sum(mylist)
# print(sumvalue)#it displays the total sum of the given mylist
# mylist.clear()#diplays the clear the given list that means delete all elements for the given mylist
# print(mylist)
#o/p:
# 1
# 4
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 7, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 7, 3, 5, 6, 7, 8, 9]
# 7
# [1, 2, 3, 5, 6, 7, 8, 9]
# [2, 3, 5]
# [1, 2, 3, 5, 6, 7, 8, 9]
# 8
# [1, 2, 3, 5, 6, 7, 8, 9]
# [1, 2, 3, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 3, 2, 1]
# True
# [9, 8, 7, 6, 5, 3, 2, 1, 10, 11, 12]
# [9, 8, 7, 6, 5, 3, 2, 1]
# 1
# [9, 8, 7, 6, 5, 3, 2, 1]
# [9, 8, 7, 6, 5, 3, 2, 1]
# 9
# 1
# 41
# []

# list in extend method:
# mylst=[1,2,3]
# new_lst=[4,5,6]
# mylst.extend(new_lst)
# print(mylst)
# o/p:
# [1, 2, 3, 4, 5, 6]

# sample_list = ['aabbcaabcddabaca']
# for letters in sample_list:
#     for char in letters:
#         print(char)
#o/p:sample_list niluvuga vastundi

# sample_list = ['aabbcaabcddabaca']
# dict_1 = dict()
# for letters in sample_list:
#     for char in letters:
#         dict_1[char]=dict_1.get(char,0) + 1
# print(dict_1)
# for key,value in dict_1.items():
#     print(f"{key}{value}",end="")
# o/p:
# {'a': 7, 'b': 4, 'c': 3, 'd': 2}
# a7b4c3d2


# sample_list = 'a7b4c3d2'
# result = ''
# for char in sample_list:
#     if char.isalpha():
#         x = char
#         print(x)
#     else:
#         result = result + x * int(char)
#         print(result)
# print(result)
# o/p:
# a
# aaaaaaa
# b
# aaaaaaabbbb
# c
# aaaaaaabbbbccc
# d
# aaaaaaabbbbcccdd
# aaaaaaabbbbcccdd


#gopi anna(23/12/23)
#print("mounika" * 7 +"b" * 5)
#o/p:mounika name seveeen times niluvuga vastundi.
#i=5
#i=i+1
#i++
#i+=1
#i=+1
#print(i)

# a=5
# b=[1,2,3]
# c=b
# c.append(5)
# print(b)
# print(c)

# b=[1,2,3]
# c=b.copy()
# c.append(5)
# print(b)
# print(c)

# a=5
# del(a)
# print(a)

# a = 5
# b = 5
# a = 10
# print(id(a))
# print(id(b))
# print(a)



# key words ni display cheyadam:
# import keyword
#
# print(keyword.kwlist)
#o/p:it displays 35 keywords
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#slicing example:
# Example list
#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing examples
# sliced_1 = my_list[2:7]   # Elements from index 2 to 6 (exclusive)
# sliced_2 = my_list[:5]    # Elements from the beginning up to index 4
# sliced_3 = my_list[::2]   # Every second element starting from the beginning
# sliced_4 = my_list[1:8:3]  # Elements from index 1 to 7 (exclusive) with a step of 3

# print(sliced_1)  # Output: [2, 3, 4, 5, 6]
# print(sliced_2)  # Output: [0, 1, 2, 3, 4]
# print(sliced_3)  # Output: [0, 2, 4, 6, 8]
# print(sliced_4)  # Output: [1, 4, 7]



