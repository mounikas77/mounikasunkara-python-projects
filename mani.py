dec_29:
list_examples:
my_list=[1,2,3,4,5,6,7,8,9]
print(my_list)#print the given list.
print(type(my_list))#it gives the type of given list.
print(my_list[0])#it gives the zero index element in the given list.
#print(my_list[10])#it gives the index error.
my_list.append(11)#add the single value.
print(my_list)
#my_list.append(12,13,14)#it cannot add the multiple elements in that common brackets,so it gives type error.
print(my_list)
#my_list.append([12,13,14])#it displays type error.
print(my_list)
my_list.insert(2,7)#it replace the value 3 by 7 in the position of index_2.
print(my_list)
my_list.insert(9,15)
print(my_list)#same as above insert.
my_list.insert(12,20)
print(my_list)
my_list.insert(15,21)#it insert the value.it take any value in any index.
print(my_list)
print(my_list[12])#it gives the 12th index position value is 20.
#print(my_list[14])#it gives the index error is -list index out of range.
#print(my_list[15])#it gives the index error-list index out of range.
print(my_list[13])#it gives the 13th index value is 21.
print(my_list.remove(2))#it removes the value_2 without using index position
print(my_list)
print(my_list.remove(7))#it removes the value 7 at starting position only but it cannot remove other same 7 value.
print(my_list)
poped_element=my_list.pop(1)#delete the element index position 1 value is 3.
print(poped_element)
print(my_list)
poped_element=my_list.pop(8)#delete the value index position 8 th value.
print(poped_element)
print(my_list)