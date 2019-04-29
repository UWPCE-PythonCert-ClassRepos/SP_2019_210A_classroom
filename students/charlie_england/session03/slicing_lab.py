#!/usr/bin/env python3

# Tasks
# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.

def first_last(s):
    #swap first and last item
    return (s[-1] + s[1:len(s)-1] + s[0])

def every_other(s):
    #remove every other item
    return s[::2]

def rem_4(s):
    #remove the first 4, last 4 and every other item
    return (s[4:len(s)-3:2])

def rev_string(s):
    #reverse string with slicing
    return s[::-1]

def thirds(s):
    #last 3rd : first 3rd: middle 3rd:
    return (s[-int(len(s)/3):] + s[:int(len(s)//3)*2] + s[int(len(s)/3):int(len(s)/3)])

assert first_last("reverse") == "eeversr"
assert every_other("every other removed") == "eeyohrrmvd"
assert rem_4("4444234564444") == "246"
assert rev_string("123456") == "654321"
assert thirds("123456789") == "789123456"