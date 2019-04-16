#SarahR. 04/15/19
#Assigment01: Python PushUp Part 01 of 02
#Functions are written to provide 4 types of errors:
# NameError, TypeError, SyntaxError and AttributeError


def name_error(): # A non-defined variable (y) is called.
	x = "The NameError function"
	print(y)

name_error()

def type_error(): # One argument is given when none is asked.
	value = input("Enter a whole number")
	x = 5/int(value) 
	print (x)

type_error(100)

def syntax_error(): # The method "int" asks for parentheses 
	value = input("Enter a number:")
	print int(value)

syntax_error()

def attribute_error(): # Tuples do not have "append" method.
	A_Tuple = ("c", "v", "b")
	A_Tuple.append((1, 2))
	print (test)
	
attribute_error()


