# jan_11(thursday)
# exception handling:(python life videos)
# interupting normal excution of a code is called error (or) if exception:
# we will handle by using error  handling:
# try:
#     print('b') #risky code #print function lo quotations lo unte answer correct ga vastundi
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("always")
# o/p:try lo print lo quotation petakamundu e output
# error
# always
# o/p:try lo print lo quotation petinataruvatha e output
# b
# no error
# always
#########################example program:
# if you have one try block you can write any number of exception blocks
# without try block we cannot write except block
# try:
#     print("a"+33) # here we cannot concate with one data type to another data type
# except TypeError:
#     print("type error")
# except valueEerror:
#    print("value error")
# o/p:type error
#####################################
# try:
#     print("a"+33) # here we cannot concate with one data type to another data type
# except:
#     print("type error")
# except:
#    print("value error")
# o/p:
# except:
#     ^^^^^^^
# SyntaxError: default 'except:' must be last
########################
# def fun(a):
#     if a < 4:
#         b = a / (a - 3)
#     print("Value of b = ", b)
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")
# o/p:ZeroDivisionError Occurred and Handled
####################3
# note:(exception handlinn)(for example above program)
# if any program "try" and "except" is compulsory for exception handling
#     but "else" and "finally" is optional
