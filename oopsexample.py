#nov-28
#oopsexamples(mclass)
#  class sampleclass:
#     attribute1=10
#     attribute2=20
# print(sampleclass.attribute1)
# print(sampleclass.attribute2)#it displays attributes.
#o/p:10
#20

#NOV_29
#OOPS (RCLASS)
# class User:
#     attri_1=10
#     attri_2=20
# obj_1=User()
# obj_2=User()
# obj_1.attri_1=30
# print(obj_1.attri_1)
# #print(obj_1.attri_1)
# print(obj_2.attri_2)
# obj_1.attri_1=30
# print(obj_1.attri_1)
#o/p:30
# 20
# 30


# class User:
#     def sample(self):
#         return "object oriented programming"
# obj_1=User()
# print(obj_1.sample())
#o/p:object oriented programming


# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def calarea(self):
#         return self.length*self.width
# rectangle_1=Rectangle(10,30)
# print(rectangle_1.calarea())
#o/p:300


# class Voter2023:
#     def __init__(self,name,age,):
#         self.name=name
#         self.age=age
#     def eligibility(self):
#         if self.age>=18:
#             return "eligibility for vote"
#         else:
#             return "not eligibility for vote"
# person_1=Voter2023("mouni",25)
# print(person_1.eligibility())
#o/p:eligibility for vote


# dec-7(m)geeks
#
# Creating a class and object with class and instance attributes
#
#
# Python3
#
#
# class Dog:
    # class attribute
#   attr1 = "mammal"

    # Instance attribute
    #def __init__(self, name):
        #self.name = name


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
Output
Rodger is a
mammal
Tommy is also
a
mammal
My
name is Rodger
My
name is Tommy





#dec-6(m)
#inheritence ex in geeks
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()





