#! /usr/bin/env python3

""" break me : output error handling
    Errors:
    NameError, TypeError, SyntaxError, AttributeError
"""

def name_error():
    print("the name error function")
    try:
        printx("hello")
    except NameError:
        print('name exception caught')

def type_error():
    print('the type error function')
    try:
       mylist = [4,5]
       print("2" + mylist)
    except TypeError:
        print('type error caught')

def attribute_error():
    print("the attribute error function")
    try:
        print("joe".x)
    except AttributeError:
        print('attribute error caught')

def syntax_error():
    print("the syntax error function")
    try:
       print("uncomment line below to see an actual SyntaxError")
       #4.split()
    except SyntaxError:
        print('syntax error caught')


name_error()
type_error()
attribute_error()
syntax_error()
