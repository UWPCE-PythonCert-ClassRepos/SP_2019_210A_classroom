#!/usr/bin/env python3

""" Returns None rather than a KeyboardInterrupt error"""

def save_input():
    try:
        get_input = input("Give some input: ")

    except EOFError as EOF_save_error:
        return None
    except KeyboardInterrupt as KeyboardInterrupt_save_error:
        return None

save_input()

