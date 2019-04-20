# deliberately implementing bugs to confuse python interpreter
# name_error: exception when calling an undeclaired function/parameter
# type_error: exception when adding two or more parameters which have different types
# syntax_error: exception when missing or having extra punctuations. Violation of the python syntax.
# attribute_error: exception when trying to access attributes of a certain parameter/object which does not have that attribute



def name_error():
    print("the name error function")
    # a typo of function name which could lead to a name error
    pintx("lel")
name_error()

def type_error():
    x = '1' + 1
    # adding an int and a char triggers type error
    print(x)

type_error()

def syntax_error():
    # misuse of syntax
    print()(

syntax_error()

def attribute_error():
    x = 1
    # x does not have a append function since x is an integer
    x.append(0)

attribute_error()