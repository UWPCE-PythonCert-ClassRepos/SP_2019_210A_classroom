'''
Lesson 01: Python Pushups Part 1 of 2
Task Number: 01 - Explore Errors
Student Name: Jasneet Chandok
Last Update Date: 04/14/19
'''
#!/usr/bin/env python3.6

def Name_Error():
    '''printx function doesn't exist'''
    printx("Name Error Example")

def Type_Error():
    ''' Can't add a string to an integer'''
    name = input("Your Name")
    age = int(input ("Your Age"))
    print(name + age)

def Syntax_Error()
    ''' Function is missing a ':' after parenthesis'''
    print("Syntax Error Example")

def Attribute_Error():
    ''' Interger object has no attribute append'''
    intAge = 40
    intAge.append(4)

Name_Error()
Type_Error()
Syntax_Error()
Attribute_Error()
