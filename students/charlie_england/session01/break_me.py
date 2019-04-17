'''
breakme le gasp
NameError, TypeError, SyntaxError, AttributeError
Create 4 functions that will give each error, syntax error will happen before code is run
'''

def name_error():
    #referencing something that does not exist
    non_existant_variable + 1

def type_error():
    #error when values cannot be combined together
    "2" + 2

def syntax_error():
    #parsing errors
    #fr x in range(1,10):
        #print(x)
    pass

def attribute_error():
    #trying to use an attribute (function) of an object when the function does not exist
    integer = 8
    integer.append(1) #cannot append to an integeter, can append to a list

