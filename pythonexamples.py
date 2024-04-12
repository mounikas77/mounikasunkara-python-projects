# harish anna python examples
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))


# a=30
# b=1.5
# print(a+b)
# age="10"
# print(type(age))
#
# age_int=int(age)
# print(type(age_int))
#
# age_float=float(age)
# print(type(age_float))
# print(age_float)

# name="harish"
# name_int=int(name)
# print(type(name_int))


# a=1
# name="harish"
# print(a+name)


# ravi anna python examples
# list_1=[5,2,6,3,4,2,10,15,11]
# list_2=[1,1,9]
# list_1.extend(list_2)
# print(list_1)
# result = []
# for num in range(len(list_1)-1):
# print(list_1[num] <= list_1[num+1])
# result.append(list_1[num] <= list_1[num+1])
# print(result)
# print(len(list_1))
# for num in range(len(list_1)):
# print(num)
# print(list_1[num],num)
# print(list_1[num]<=list_1[num+1])


# sample_list=["cd","a","b","bbb","c","aa"]
# #print(sorted(sample_list))
# print(sorted(sample_list,key=lambda x:len(x)))
# print(sorted(sample_list,key=len))


# input_list = [5, 2, 10, 1, 4, 8, 9, 3]
# for num in range(len(input_list) - 1):
# print(num,input_list[num] <= input_list[num+1])
# print("{} {} {} {}".format(num, input_list[num], input_list[num + 1],input_list[num] <= input_list[num+1]))


# input_list=[5,2,10,1,4,8,9,3]
# print(input_list)
# for int,num in enumerate(input_list):
#     print(int,num)


# input_list=[5,2,10,1,4,8,9,3]
# print(sorted(input_list))
# print(reversed(input_list))
# word="ravi"
# print(sorted(word))


# print(chr(97))
# lower_case=[]
# upper_case=[]
# for apl in range(97,123):
#     print(lower_case.append(chr(apl)))
# print(lower_case)


# key_list=["a","b","c"]
# value_list=[1,2,3]
# print(dict(zip(key_list,value_list)))
# print(list(zip(key_list,value_list)))

# print([num for num in range(1,11) if num %2 == 0])


# import sys
# print(sys.builtin())
#


# print(ord("a"))#it gives the ASCII value of small letter
# print(chr(99))#it gives the which is 99th alphabet of ASCII characters
# print(ord("mouni"))

# n=("tweak")
# print(n[2:4])
# print(n[1:])
# print(n[-1::-2])
# print(n[-2:-8])
# print(n[::-1])
# print("mouni"+"chinnu")
# print("first"*2)
#
#
# word="tweak"
# word.join()
#
# print()


# l=[1,1,2,3,2,5,6,5]
# l1=[]
# l2=set(l)
# print(l2)
# print(set(l1))
# print(list())


# list=[1,1,2,3,2,5,6,5]
# res_list=[]
# for element in list:
#     if element not in res_list:
#         res_list.append(element)
# print(res_list)

# list=[1,1,2,3,2,5,6,5]

# name="abbcbba"
# if (name==name[::-1]):
#     print("palidrome")
# else:
#     print("notpolindrome")
#
#
# name="mounika"
# if (name==name[::-1]):
#     print("palidrome")
# else:
#     print("notpolindrome")

#
# list=[1,2,3,2,1,10]###it displays the how many no of not repeated elements
# #unique_list=set(list)
# count = 0
# for i in list:
#     c = list.count(i)
#     if c > 1:
#         count +=1
# print(count)


# unique_list=[1,2,3,2,1,10]
# unique_list=list(set(unique_list))#naveen anna
# count = 0
# for i in unique_list:
#     c = unique_list.count(i)
#     if c > 1:
#         count +=1
# print(count)


# input_list=[1,2,3,5,2,10]##count the number of 2
# list1=set(input_list)
# list=0
# for item in input_list:
#     a=input_list.count(item)
#     if a>1:
#         list=list+1
# print(list)

#

# harish anna(20/11/2023)
# a=1,2,3
# print(a)
# # d,e,f,g=a
# b,c=a
# d,b*c=a


# a=[1,2,3,4]
# a1=a#aliasing (or) pass by reference
# a[0]=100
# print(a1)

# l=[1,2,3,4]
# l1=l.copy()#cloning(or) exat copy
# l[0]=100
# print(l1)
# print(l)


# l=[1,2,3,[2,3,4]]
# l1=l.copy()
# l[3][1]=100
# print(l1)

# import copy
# l=[1,2,3,[4,5,6],7]
#
# l1=copy.deepcopy(l)
# l[3][1]=100
# print(l1)

# ***********************

# ravi anna(20/11/2023)afternoon
# list_a=[4,2,3,1]
# print(sum(list_a))#it displays sum


# str_a="hello word"
# print(sorted(str_a))#it displays sorted elements


# print([num for num in range(1,11)])#list comprehension


# print([num for num in range(1,11) if num%2==0])#list comprehension-->debugging cheyalemu,it is disadvantage

# em_list=[]
# ename=(1,11)
# for num in range(1,11):
#     if num%2==0:
#         em_list.append(num)
# print(em_list)


# [number for number in range(1,11)]
# print([number for number in range(1,11)])

# it displays the given numbers are even or odd
# input_list=[0,1,2,3,4,5,6,7,8,9,10]
# empty_list=[]
# for num in input_list:
#     if num%2==0:
#         empty_list.append("even")
#     else:
#         empty_list.append("odd")
# print(empty_list)


# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(["even" if num%2==0 else "odd" for num in input_list])#list comprehension

# input_list=[0,1,2,3,4,5,6,7,8,9,10]
# empty_list=[]
# for num in input_list:
#     if num%2==0:
#         empty_list.append("even")
#     elif num%3 == 0:
#          empty_list.append("odd")
# else:
#     empty_list.append("odd")
# print(empty_list)

# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([num**2 if num%2==0 else num for num in input_list])


# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([num ** 2 if num % 2 == 0 else num if num == 0 else num+1 for num in input_list])

# print(["even" if num % 2 == 0 else "odd" for num in input_list])  # list comprehension

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(tuple(num ** 2 if num % 2 == 0 else num if num == 0 else num+1 for num in input_list))

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print({num ** 2 if num % 2 == 0 else num if num == 0 else num+1 for num in input_list})

# input_list_1=[1,2,3,4]
# input_list_2=["a","b","c","d","e"]
# print({key:value for key,value in zip(input_list_1,input_list_2)})
# print({num:num**2 for num in input_list_1})

# input_list_1=[1,2,3,4]
# input_list_2=["a","b","c","d","e"]
# dict_1={}
# for k,v in zip(input_list_1,input_list_2):
#     print(k,v)
#     dict_1.update({k:v})
# print(dict_1)
# print({num:num**2 for num in input_list_1})

# print([chr(num) for num in range(97,123)])#it displays small letters


# l=[]#out put raledu
# ll=[]
# for num in range(97,123):
#      l.append(chr(num)),ll.append(chr(num).upper)
# print(l)
# print(ll)

# mounika = [chr(num) for num in range(65, 90)]#it displays capital letters
# mounika_upper = [aa.upper() for aa in mounika]
# print(mounika_upper)

# upper kavalante  97 to 122
# lowe kavalante 65 to 90

# input_list_2=[1,2,3,4]
# input_list_1=["a","b","c","d","e"]
# print({key:value for key,value in zip(input_list_1,input_list_2)})


# print([chr(num) for num in range(97,123)])
# print([chr(num) for num in range(97,123)])#it displays small letters


# empty_dict={}
# for num in range(97,123):
#     #print(num)
#     empty_dict.update({chr(num):num})
# print(empty_dict)


# print({chr(num):num for num in range(97,123)}


# november-21
""" string methods """  # it is doc string
# sample_1="ravi chandra"
# print(sample_1.capitalize())#it displays first letter capital
#
# sample_2="Ravi chandra"
# print(sample_2.upper())#it displays all letter capital
#
# sample_3="121,ravi"
# print(sample_3.upper())#it displays all letter capital
#

# sample_1="ravi chandra in python"
# print(sample_1.title())#it displays the each word first letter is capital

# sample_1="ravi chandra is a python"
# print(sample_1.count("a"))#it displays which letter is how many times returns to the given sentence (or) word.


# sample_1="ravi chandra"
# print(sample_1.find("c"))#it displays index position of the given word (or) sentence.


# sample_1="ravi chandra"
# print(sample_1.replace("chandra","chand"))#it displays the old name replace the new name.

# sample_1="ravi,cha.ndra"
# print(sample_1.split("," "."))#it displays the split of the given word (or) sentence.

# sample_1="ravi chandra"
# print(sample_1.split(" "))#it displays the separate the given word by using comma.


# sample_1="apple,orange,banana"
# print(sample_1.split(","))#it displays the given data by using comma and square bracket.


# name="maunika"
# for num in range(len(name)):
#     if name[num]=="a":
#         print(num)#it displays the index position of the given string.
#

# name_strip="***ravi*****"
# print(name_strip.strip("*"))#it gives the name
# print(name_strip.lstrip("*"))#it gives the left side name
# print(name_strip.rstrip("*"))#it gives the right side name


# aws_username=input("enter your username: " )
# if aws_username[0].isupper() and not aws.username[-1].isalnum():
#     print("user name is valid")
# else:
#     print("username is in valid")


# sample_1=["a","b","c","d"]
# print(" ".join(sample_1))#it displays a b c d that means space of the each letter.


# sample_1=["a","b","c","d"]
# print("".join(sample_1))#it displays the without space of the each letter.

'''input: "d@r!eambi#g$"
output: "g@i!bmae#rd$"'''

# input = "p y t h o n"
# x=input.replace(" " ,"@")****vvvvimp
# print(x)
# print(input.replace["h" ,"$"])****it is wrong
# print(input)


# def rearrange_string(input_str):
#     # Check if the input string is not empty
#     if not input_str:
#         return "Input string is empty"
#
#     # Determine the length of the input string
#     length = len(input_str)
#
#     # Calculate the number of groups (assuming each group has 4 characters)
#     num_groups = length // 4
#
#     # Rearrange the characters in each group
#     rearranged_groups = [input_str[i*4:(i+1)*4][::-1] for i in range(num_groups)]
#
#     # Concatenate the rearranged groups to get the final output
#     output_str = ''.join(rearranged_groups)
#
#     return output_str

# Test the function with the provided input
# input_str = "d@r!eambi#g$"
# output_str = rearrange_string(input_str)
# print(output_str)


# november-22(Rclass)
# l_1=[1,2,3]
# l_2=[4,5,6]
#  l_1.append(l_2)
# l_2=[4,5,6]
# l_1.extend(l_2)
# print(l_1)

# l_3=["a","b","c"]
# l_3.insert(0,"b")
# print(l_3)
#
# l_3.pop(0)
# print(l_3)

# l_1=[1,2,3]
# l_1.insert(1,"z")
# print(l_1)
# l_1.insert(1,[2,3])
# l_1.insert(2,"abc")
# print(l_1)


# l_6=[1,1,2,2,3,4,4,4,5]
# for num in set(l_6):{1,2,3,4,5}
# print(l_6.count(num))
# print(f"{num} count of num {l_6.count(num)}")
# print(list(set(l_6)))


# l_7=["a","b","c","d"]
# l_7.reverse()
# print(l_7)#it displays

# l_8=["c","b","d","e","a"]
# l_8.sort()
# print(l_8)


# l_9=["a","b","c","d"]
# l_9.remove("c")
# print(l_9)

# l_9=["a","b","c","d"]
# x=l_9.copy()
# print(x)


# ***************************
# november-23(rclass)
# sample_set={8,7,2,3,4,2,4,5,5}
# print(sample_set)#it contains assending order
# sample_set1={"g","a","b","d"}
# print(sample_set1)#it displays different order

# sample={4,5,6,7,82,3,1,0}
# sample.add("s")
# print(sample)#it add random in any place

# sample.update(["a","b","c","d","e"])#it add multiple list elements
# sample.update({"x","v","z"})#it add multiple set elements in any place
# print(sample)

# sample_1={"a","d","g","h","g"}
# sample_2={1,2,3,4}
# sample.update(sample_1,sample_2)#it adds multiple set values
# print(sample)

# sample_set_1={1,2,3,4,5,6,7,8}
# sample_set_1.remove(3)#leni element ni echina error ni display chestundi
# print(sample_set_1)
# sample_set_1.discard(3)
# sample_set_1.discard(19)#leni element echina error ni display cheyadu anni elements display chestundi
# print(sample_set_1)


# sample_set_1={1,2,4,5,6,9}
# sample_set_1.pop()
# print(sample_set_1)#it delete the first element in the set
# sample_set_1.pop(4)#it cannot use of index 4
# print(sample_set_1)


# sample_set_1={1,2,3,4}
# sample_set_2={6,4,7,8,9}
# print(sample_set_1.union(sample_set_2))#it adds the both two sets

# sample_set_1={1,2,3,4}
# sample_set_2={6,4,7,8,9}
# print(sample_set_1.union(sample_set_2))#it adds the both two sets
# print(sample_set_1 | sample_set_2)#its like union
# print(sample_set_1.intersection(sample_set_2))#it diplays only same element in two sets
# print(sample_set_1 & sample_set_2)#its like intersection


# sample_set_1={1,2,3}
# sample_set_2={6,7,8,9}
# print(sample_set_1 & sample_set_2)#it displays set()

# sample_set_1={1,2,3,4}
# sample_set_2={6,4,7,8,9}
# print(sample_set_1 + sample_set_2)#it cannot work in set
# print(sample_set_1 - sample_set_2)#it displays only sample_set_1 values
# print(sample_set_1.difference(sample_set_2))#it like "-" same


# sample_set_1={1,2,3,4,19}
# sample_set_2={6,7,8,9,4,5}
# print(sample_set_1.symmetric_difference(sample_set_2))#both sets lo unna same element radu

# sample_set_1={1,2,3,4,5}
# sample_set_2={4,3,5,6,7,8}
# print(sample_set_1.issubset(sample_set_2))#it gives false
# print(sample_set_1 <= sample_set_2)#its like issubset(comparision operator)


# main_list=[1,1,2,3,4,4,5,6,5]
# print(list(set(main_list)))#in this output we cannot use built in methods , functions by using simple set() its out put is [1,2,3,4,5,6]


# main_list=[1,1,2,3,4,4,5,6,5]
# empty_list=[]
# for value in main_list:
#    # print(value)
#     if value not in empty_list:
#         print(value)
#         empty_list.append(value)
# print(empty_list)
#
#
# main_list=[1,1,2,3,4,4,5,6,5]
# l=[]
# list=[value for value in main_list]#list comprehension lo ravatledu
#
# 1.core signals(in google,like programs)
# 2.bubble sort
# 3.patterns
# 4.100 programs(you can get the 100 programs we can deal functions easily)
# 5.dictionary datatype
# 6.functions(def,lambda)list comprehension lo def ni use cheyalemu
# 7.classes
# 8.in chatgpt lo math module lo modification cheyali
# 9.events ni enni create chestaru aws lambda lo
# 10 random modules
# 11.iterators
# 12.math modules
# 13.recurssion functions
# 14.stack over flow ni google lo type cheste its like chargpt
# 15.pagnision means in django
#
# class mani:
# def mounika():
#     a=10
#     b=20
#    print(a)
#   # mounika()

# ******************************
# november-24(rclass)
# question-1
# input:[1,2,-3,-4,-5,6]
# output:[1,2,3,4,5,6]
# sample_1=[1,2,-3,-4,-5,6]
# print(list(abs(sample_1)))

# sample_1 = [1, 2, -3, -4, -5, 6]#correct output but thinking wrong
# print([1,2,-3*-1,-4*-1,-5*-1,6])

# print(list(set(sample_1)))#wrong
# sample_2=[]
# for i in sample_1:
#      sample_2=sample_2 +str(abs(i))
# print(sample_2)
# print(abs(sample_1))
# print([1,2]+1)

# input = "p y t h o n"#for example nenu use chedamanukunanu
# x=input.replace(" " ,"@")
# print(x)

# input = "1, 2, -3, -4, -5, 6"#out put correct but way of thinking wrong
# x = input.replace("-3", "3")
# print(x)
# a = x.replace("-4", "4")
# print(a)
# z = a.replace("-5", "5")
# print([(z)])
# for int !== + in input:
#         print(abs(int))
#         else:
#         print (int)#wrong


# for int in sample_1:
#     if int!=+int:
#         print(n=-int*-1)
#     else:
#         print(int)#wrong

# int=[1,2,-3,-4,-5,6]
# print(abs([int]))

# input =int(input([1, 2, -3, -4, -5, 6]))
# em_list=[]
# for i in em_list:
#     if i==abs(input):
#          print(em_list)
#     else:
#          print("negative value")#wrong-


# input_list=[1,2,-3,-4,-5,6]
# print(abs(input_list) for out_1 in input_list)#wrong-1


# input_list = [1, 2, -3, -4, -5, 6]#success-chatgpt
# output_list = [abs(number) for number in input_list]
# print(output_list)


# input= [1, 2, -3, -4, -5, 6]#success-1
# result=[]
# for value in input:
#     if value < 0:
#         #print(-value)
#         result.append(-value)
#     else:
#          result.append(value)
# print(result)


# input= [1, 2, -3, -4, -5, 6]#success-2
# result=[]
# for value in input:
#     result.append(abs(value))
# print(result)


# input=[1,2,-3,-4,-5,6]
# print([abs(value) for value in input])#success-3

# input=[1,2,-3,-4,-5,6]
# print([-value if value<0 else value for value in input])#success-4


# question-2
# input:[1,2,3,2,4,2,5]
# output:[1,4,3,4,4,4,5]

# input=[1,2,3,2,4,2,5]#success question_2 here we can take + or * by using if condition.
# result=[]
# for value in input:
#     if value == 2:
#          #print(value)
#          result.append(value*2)
#     else:
#           result.append(value)
# print(result)


# input = [1, 2, 3, 2, 4, 2, 5]
# print([value + 2 if value == 2 else value for value in input])  # success question_2 for list comprehension


# november-27(rclass)
# dict:
# hashable functions
# sample_dict = {"a": 1, "b": 2, "c": 3}
# print(sample_dict.copy())#copy the dict

# sample_dict = {"a": 1, "b": 2, "c": 3}
# sample_dict.clear()
# print(sample_dict)#to clear the data


# sample_dict = {"a": 1, "b": 2, "c": 3}
# print(sample_dict.get('c'))#to get particular data

# sample_dict = {"a": 1, "b": 2, "c": 3}
# sample_dict.pop('a')
# print(sample_dict)#to remove particular data it take only keys.


# sample_dict = {"a": 1, "b": 2, "c": 3}
# sample_dict.popitem()
# print(sample_dict)#to remove the last data.o/p:{'a': 1, 'b': 2}

# sample_dict = {"a": 1, "b": 2, "c": 3}
# sample_dict_1={"c":4,"d":5}
# sample_dict.update(sample_dict_1)
# print(sample_dict)#to add the dictionary.


# sample_dict = {"key1": 1, "key2": 2, "key3": 3}
# for num in range(4,11):
#     sample_dict.update({'key'+str(num):num})
# print(sample_dict)
# o/p:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9, 'key10': 10}


# sample_dict = {"key1": 1, "key2": 2, "key3": 3}
# for num in range(4,11):
#      sample_dict.update({'key':num})
# print(sample_dict)
# o/p:{'key1': 1, 'key2': 2, 'key3': 3, 'key': 10}


# sample_dict = {"key1": 1, "key2": 2, "key3": 3}
# for pair in sample_dict:
#     print(pair)
# o/p:key1
# key2
# key3


# sample_dict = {"key1": 1, "key2": 2, "key3": 3}
# for pair in sample_dict.items():
#     print(pair)
# o/p:('key1', 1)
# ('key2', 2)
# ('key3', 3)


# sample_dict = {"key1": 1, "key2": 2, "key3": 3}
# for num in range(4,11):
#     sample_dict.setdefault("key"+str(num),num)
# print(sample_dict)
# o/p:{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9, 'key10': 10}


'''functions
1.camelcase-first letter small next letter capital
dict.'''
# django
# models ,views,forms,urls,dockers


# question_1
# input:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output:[2,1,4,3,6,5,8,7,10,9]
# main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty_list = []
# for value in main_list:
#     if value % 2 == 0:
#         #print(value)
#         empty_list.append(value-1)
#     else:
#         #print(value)
#         empty_list.append(value+1)
# print(empty_list)
# o/p:[2, 1, 4, 3, 6, 5, 8, 7, 10, 9]"success for loop.


# input:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output:[2,1,4,3,5,8,7,10,9]
# list comprehension
# input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([value - 1 if value % 2 == 0 else value + 1 for value in input])


# november_28(rclass)functions
# def functionOne(value_a,value_b):
#     return value_a + value_b
# print(functionOne(10,20))
# print(functionOne(40,100))
# print(functionOne(50,5))
# o/p:30
# 140
# 55

# def functionOne(sample_list_1):
#     return sum(sample_list_1)
# print(functionOne([2,6,7,10,11]))
# o/p:36


# from function import userFunction
#
# list_a = list(range(1, 21))
# print(sorted(list_a, key=userFunction))
#o/p:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# from function import userFunction
# name="ravi"
# print(userFunction(name))

#ganga example:dec-30(oops-class)
# from practice1mouni import add
# c=add(1,2)
# print(c)

# function ex:
# def my_function():
#   print("Hello from a function")
# my_function()
# o/p:Hello from a function
