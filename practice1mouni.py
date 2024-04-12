#november-21(nov_20 Rclass)
#print([num for num in range(1,11)])
#''' it is list comprehension
# and it displays the 1 to 10 values in square brackets
#'''

#it displays the sum of given list.
# list_1=[1,2,3,4]
# print(sum(list_1))


#it displays the sorted of the given string that means assending order.
# str_1="mounika sunkara"
# print(sorted(str_1))

#it diplays the " " space is which value in ASCII letters
# print(ord(" "))# it diplays 32 ASCII value

#it displays the even numbers in the range 1 to 11 and it is list comprehension
#print([num for num in range(1,11) if num%2==0])


#it diplays even numbers for loop and if condition
# em_list=[]
# ename=(1,11)
# for num in range(1,11):
#     if num%2==0:
#         em_list.append(num)
# print(em_list)

#it displays the 1 to 10 in square brackets by using list comprehension.
#print([number for number in range(1,11)])



#it diplays given list are even and odd numbers by using for loop and if condition
# input_list=[1,2,3,4,5,6,7,8,9,10]
# empty_list=[]
# ename=(1,11)
# for num in input_list:
#     if num%2==0:
#         empty_list.append(even)
#     else:
#         empty_list.append(odd)
# print(empty_list)


#########string methods ###########
#1.capitalize()
#Definition and Usage
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# txt="python is a program"
# print(txt.capitalize())

# txt="python is FUN!"
# print(txt.capitalize())


# txt="36 my age."
# print(txt.capitalize())

#2.casefold()
# returns a string where all the characters are lower case.it like lower() method
# txt="Hello,And welcome To My World!"
# print(txt.casefold())


#3.center()
#The center() method will center align the string, using a specified character (space is default) as the fill character.
#Syntax:string.center(length, character)
# Parameter Values:
# Parameter	Description:
# length:	Required. The length of the returned string
# character:	Optional. The character to fill the missing space on each side. Default is " " (space)


# txt="banana"
# print(txt.center(20))


# txt="banana"
# print(txt.center(20,"0"))

# a="Mounika is a python programmer"
# b="MAHI IS MY SISTER"
# print(a.lower())#it gives all lower case letters
# print(a.upper())#it gives all upper case letters
# print(b.strip())#it gives removes the space at the starting and ending of given string.
# print(a.capitalize())#the first character is converted to uppercase and other letters to converted to lower case.
# print(a.title())#the first character in every word is upper case.
# print(b.casefold())#all the characters are in lower case its like lower() method.
# print(len(a))#to get the length of a string.
# print(b.replace("M","N"))#it replace a specified phrace or another specified phrace.(old value,new value,count)
# print(a.find("a"))#first occurance of the specified value it gives that index.
# print(b.isalnum())#check if all the characters in text is alphanumaric or not.(it is alphanumeric it returns true)
# print(a.islower())#it gives all the characters in text are lower case.
# print(b.isupper())#it displays given b is total uppercase it returns true otherwise it gives false.
# print(', '.join([a,b]))#it combines a and b
# print(a.rfind('i'))#it gives the last occurance of the given letter index.

# a=1
# b=2
# c=a+b
# print(c)

# def add(a,b):
#     c=a+b
#     print(c)
# add(1,2)

def add(a,b):
    c=a+b
    return(c)



