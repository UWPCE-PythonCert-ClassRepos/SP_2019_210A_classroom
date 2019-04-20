#---Dev Script---#
# Dev: Miguel Rovira-Gonzalez
# Script Creation Date: Monday 4/15/19
# Description: Lesson 1
# Create 4 function that results in an Exception
# 1) NameError, 2)TypeError, 3) SyntaxError, and 4) AttributeError

# 1) Creating a NameError Exception
def NameError():
    name = 'Miguel'
    print(nam)

# This is an name error since I printed nam instead of name (nam is not an assigned variable)
NameError()

# 2) Creating a TypeError Exception
def TypeError():
    5 + 'Miguel'

# This is an type error since python is trying to add perform arithmetic on a number and a string
TypeError()


# 3) Creating a SyntaxError
def correct_syntax_please():
    print("I love correct syntax but today that isn't going to happen, sorry I am not sorry")
    print 'oops I did it'

# This is a syntax error since in Python 2 you could call the print function without using a parenthesis, but not in Python 3
correct_syntax_please()

# 4) Creating an AttributeError
def errors_in_my_attributes():
    listerror = [1,2,3,4,5,6]
    upper = listerror.upper()
    print(upper)

# This is an attribute error since there is no upper method associated with the list class
errors_in_my_attributes()

