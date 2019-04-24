# Break things

def name_error():
    print("blah{}".format(undefined_variable))

def type_error():
    a = 1
    b = '2'
    return a + b

def syntax_error():
    # as;dlfkja;sd
    pass

def attribute_error():
    car = 'foo'
    doesnt_exist = car.wing
    pass

# ne = name_error()
# te = type_error()
# se = syntax_error()
ae = attribute_error()

