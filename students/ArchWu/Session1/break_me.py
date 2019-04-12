def name_error():
    print("the name error function")
    pintx("lel")
name_error()

def type_error():
    x = '1' + 1
    print(x)

type_error()

def syntax_error():
    print()

syntax_error()

def attribute_error():
    x = 1
    x.append(0)

attribute_error()