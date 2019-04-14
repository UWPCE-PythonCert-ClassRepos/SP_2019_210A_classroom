def NameError():
    printx("Here's a name error")
    # printx doesn't exist

def TypeError():
    name = "Andrew"
    age = 30

    print(name + age)
    # can't add a string to an int

def SyntaxError()
    print("here's a syntax error")
    # missing a : at the end of the function definition

def AttributeError():
    name = "Gus"
    print(name.len())
    # correct syntax is print(len(name))

NameError()
TypeError()
SyntaxError()
AttributeError()
