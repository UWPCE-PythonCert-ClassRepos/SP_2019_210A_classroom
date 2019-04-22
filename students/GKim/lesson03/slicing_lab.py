"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
"""
a_string = "How is this test"
a_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

def first_last(string):
    a = string[:1]
    z = string[-1:]
    mid = string[1:-1]

    return(z + mid + a)

def every_other(string):
    return string[::2]

def first4_last4(string):
    return string[4:-4:2]


def reverse(string):
    return string[::-1]


def third(string):
    x = int(len(string)/3)
    beg = string[:x]
    end = string[-x:]
    mid = string[x:x + x]
    return end + beg + mid
    

print(first_last(a_string))
print(first_last(a_tuple))
print(every_other(a_string))
print(every_other(a_tuple))
print(first4_last4(a_string))
print(first4_last4(a_tuple))
print(reverse(a_string))
print(reverse(a_tuple))
print(third(a_string))
print(third(a_tuple))