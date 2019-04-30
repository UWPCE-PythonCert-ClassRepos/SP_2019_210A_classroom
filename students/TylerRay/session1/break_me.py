"""
breakme
"""

def name_error():
    print("the name error function")
    printd("something") #spelled print wrong--aka type or reference something that doesn't exist

def type_error():
    print("Please input an integer to solve the following equation: X + 1")
    vx = input() # Does not require an int input therefore the following won't work:
    print(vx + 1) # Can't add an integer and a string

def syntax_error(): # As just one example of a syntax error: If i removed the ':' from syntax_error() then I'd get a fatal syntax error
    print("I couldn't get a non-fatal syntax error.\nHowever if I had omitted the ':' from the end\nof the syntax_error function it would be a syntax error.")

intVariable = 1

print('''
    Welcome to the Error Experience
    
    Please select which error you'd like to experience
    NameError, TypeError, SyntaxError, AttributeError
    1. Name Error 
    2. Type Error
    3. Syntax Error
    4. Attribute Error
''')


menuChoice = int(input())

while menuChoice in range(1,5):
    if menuChoice == 1:
        name_error()
        menuChoice = None
    if menuChoice == 2:
        type_error()
        menuChoice = None
    if menuChoice == 3:
        syntax_error()
        menuChoice = None
    if menuChoice == 4:
        intVariable.append(1) # You cannot append a variable containing just an integer. Append isn't a valid command in this situation.