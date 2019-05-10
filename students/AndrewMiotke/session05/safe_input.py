#!/usr/bin/env python3

""" Returns None rather than a KeyboardInterrupt error"""

def safe_input():
    try:
        get_input = input("Give some input: ")
        print(get_input)

    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

safe_input()