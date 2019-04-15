"""
breakme.py 

example for session01
"""


def name_error():
    try:
        breakme()
    except NameError as e:
        print('NameError: ' + str(e))

def type_error():
    try:
        string = 'bla'
        print(sum(string))
    except TypeError as e:
        print('TypeError: ' + str(e))

# commenting out SyntaxError example so rest of code executes
#def syntax_error():
#    try:
#        print('Syntax error via mismatched quotes")
#    except SyntaxError as e:
#        print("SyntaxError: " + str(e))

def attribute_error():
    try:
        string = 'bla'
        string.append('bla')
        print(string)
    except AttributeError as e:
        print('AttributeError: ' + str(e))

def main():
    name_error()
    type_error()
#   syntax_error()
    attribute_error()


if __name__ == '__main__':
    main()
