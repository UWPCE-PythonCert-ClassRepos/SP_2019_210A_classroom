def name_error():
    print("the name error function")
    pintx("name")
name_error()

def syntaxError():
    return hello there

def typeError():
    return len(42)

def attribute_error():
    x = 1
    # cant append an integer
    x.append(0)
attribute_error()

