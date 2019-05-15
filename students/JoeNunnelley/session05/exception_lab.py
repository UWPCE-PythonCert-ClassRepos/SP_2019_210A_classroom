#! /usr/bin/env python3

"""
Exception Lab Excercise
Author: Joe Nunnelley
"""

def safe_input(message):
    """
    param1: the message to output
    returns: the input of the user or an error
    """
    input_value = ''
    try:
        input_value = input(message)
        print("Input: {}".format(input_value))
    except EOFError:
        print("Your input was invalid. EOFError")
    except KeyboardInterrupt:
        print("Your input was invalid. KeyboardInterrupt")

    return input_value


safe_input("Input Text: ")
safe_input("Input ^D: ")
safe_input("Input ^C: ")
