"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
"""


def first_last(string):
    a = string[:1]
    z = string[-1:]
    mid = string[1:-1]

    return(z + mid + a)

print(first_last("how is this test"))


def every_other(string):
    return string[::2]

print(every_other("how is this test"))


def first4_last4(string):
    return string[4:-4:2]

print(first4_last4("how is this test"))

def reverse(string):
    return string[::-1]

print(reverse("how is this test"))

def third(string):
    x = len(string)/3
    beg = string[:x]
    end = string[x + 1:]
    mid = 
