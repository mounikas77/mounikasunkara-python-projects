#nov_30
#dictionary:
# 1.group of key_value of pairs:
# 2.duplicate keys are not allowed,but values can be duplicated:
# 3.any data type can be allowed as key & value.
# 4.dictionaries are ordered from 3.7
# 5.dictionaries are mutable so that we can add,delete,edit dictiories.
# 6.dictionaries are dynamic
# 7.keys should be immutable.


#1.to create a empty dictionary:
# 2 ways
# d={}
# print(d)
# d=dict()
# print(d)
# o/p:{}
# {}


#2.accessing values using keys:example program
# user_info={
#     "user_1234":{
#         "user_id":"user_1234",
#         "user_name":"mouni@1234",
#         "gender":"female",
#         "age":25
#     },
# "user_1111":{
#         "user_id":"user_1111",
#         "user_name":"mani@1234",
#         "gender":"male",
#         "age":25
#     },
# }
# print(user_info['user_1234'])
# print(user_info['user_1111'])
# o/p:{'user_id': 'user_1234', 'user_name': 'mouni@1234', 'gender': 'female', 'age': 25}
# {'user_id': 'user_1111', 'user_name': 'mani@1234', 'gender': 'male', 'age': 25}



# 3.dictionary methods:
# update(),items(),values(),keys(),pop(),popitem(),get(),setdefault(),clear()


#4.to update the dictionay and print "d"
# d={
#     "name":"mounika",
# }
# additional_info={"course":"python",
#                  "webframework":"django",
#                 "DB":["posygres","mysql"]
# }
# d.update(additional_info)#o/p:{'name': 'mounika', 'course': 'python', 'webframework': 'django', 'DB': ['posygres', 'mysql']}
# print(d)#o/p:{'name': 'mounika'}


#5.to change the value
# d={
#     1:True,
#     2:False
# }
# print(d)#o/p:{1: True, 2: False}
#print(d[1])#o/p:True
#d[1]="hello"
#print(d)#o/p:{1: 'hello', 2: False}


#6.to get the value
# d={
#     1:True,
#     2:False
# }
#print(d[3])#o/p:KeyError: 3
# values=d.values()
# print(values)#o/p:dict_values([True, False])
# print(type(values))#o/p:<class 'dict_values'>
# for value in values:
#     print(value)#o/p:True
# False

# va=d.setdefault(3,"harish")
# print(va)
# print(d)#o/p:{1: True, 2: False, 3: 'harish'}


# 7.without key_value pair it returns
# d={
#     3:True,
#     2:False
# }
# val = d.get(1, "Key Not available")
# print(val)#o/p:Key Not available



#functions:
# group of statements
# reusability
# types of functions
# 1.Builtin functions
# 2.user_defined functions


creating a parameterless function
