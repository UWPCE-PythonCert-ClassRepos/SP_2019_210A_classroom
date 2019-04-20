"""
	In the break_me.py file write four simple Python functions:
	Each function, when called, should cause an exception to happen
	Each function should result in one of the four most common exceptions you’ll find.
	for review: NameError, TypeError, SyntaxError, AttributeError
"""

#NameError 
first_number = print("Input your first number")
def name_error (first_number):	
	print('first_number', fist_number)
name_error(first_number)

#TypeError
arg1 = 7
arg2 = "7"
def type_error(arg1,arg2):
	sum = arg1+arg2
	print(sum)
type_error(arg1,arg2)

#SyntaxError
def syntax_error() :
	print("I made a mistake

#AttributeError
import random
def attribute_error():
	print(random.dance())
attribute_error()
	
#------------------END----------------#