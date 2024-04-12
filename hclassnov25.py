#november_25(hclass)
#generators example:
# def f1():
#     yield 1
#     yield 2
#     yield 3
# result = f1()
# for value in result:
#      print(value)


#example_2
# def f2():
#     for i in range(10):
#         yield i
# result = f2()
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())



#generators starting
# def f1():
#     return 1
#     return 2
#     return 3
# print(f1())#it gives the value 1 "in this time we use the generators



#def:generators are like functions which contain "yield" keyword.
#we cannot use result statement.
# def f1():
#     yield 1
#     yield 2
#     yield 3
# result = f1()
# for value in result:
#     print(value)

#nove_29(hclass)
#1.factorial of a number
#2.a,e,i,o,u _display
#3.list of duplicates ni findout cheyadam
#4.string in palindrome.
#5.search in word given sentence.

#program _1
# Calculate factorial using a for loop
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# # Example: Find the factorial of 5
# result = factorial(5)
# print(f"The factorial is: {result}")
#o/p:The factorial is: 120


#program _2

# Function to display vowels in a string
# def display_vowels(input_string):
#     vowels = "aeiouAEIOU"
#
#     print("Vowels in the string:")
#     for char in input_string:
#         if char in vowels:
#             print(char)


# Taking input from the user
#user_input = input("Enter a string: ")

# Calling the function to display vowels
#display_vowels(user_input)
#o/p:Enter a string: mounika
#Vowels in the string:
# o
# u
# i
# a


#program_3
# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()
#
#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#
#     return list(duplicates)
#
# # Example usage:
# my_list = [1, 2, 3, 4, 2, 7, 8, 1, 3]
# result = find_duplicates(my_list)
#
# if result:
#     print(f"Duplicates found: {result}")
# else:
#     print("No duplicates found.")
# #o/p:Duplicates found: [1, 2, 3]


#program_4
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_s = ''.join(s.split()).lower()

    # Compare the original string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
#o/p:Enter a string: mounika
#mounika is not a palindrome.(or)
#Enter a string: level
#level is a palindrome.


#program _5
def search_word(text, word):
    if word in text:
        print(f"The word '{word}' is present in the text.")
    else:
        print(f"The word '{word}' is not found in the text.")

# Example usage:
user_text = input("Enter a text: ")
search_word_input = input("Enter the word to search: ")

search_word(user_text, search_word_input)





def search_word(text, word):
    index = text.find(word)
    if index != -1:
        print(f"The word '{word}' is found at index {index}.")
    else:
        print(f"The word '{word}' is not found in the text.")

# Example usage:
user_text = input("Enter a text: ")
search_word_input = input("Enter the word to search: ")

search_word(user_text, search_word_input)
















