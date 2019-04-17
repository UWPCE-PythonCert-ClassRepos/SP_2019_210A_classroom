#
#Assignment1: break_me.py
#generate 4 errors: name error; type error; syntax error; attribute error
def name_error():
    print ("the name error function")
    printx("actual name error")

#name_error()

def type_error():
    a = 5
    b = "1"
    x = a + b
#type_error()

#def syntax_error():
#    -pass

#syntax_error()

def attribute_error():
    a = 100
    b = a.split(" ")

attribute_error()
