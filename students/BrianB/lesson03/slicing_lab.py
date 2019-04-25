print("hello world")

#---------------------------------------------------------------------
# Goal:
# Get the basics of sequence slicing down.
#
# Tasks:
#  Write some functions that take a sequence as an argument, and
#  return a copy of that sequence:
#    1* with the first and last items exchanged.
#           SOLUTION == a_string[-1:] + a_string[1:-1] + a_string[:1] &
#                       a_tuple[-1:] + a_tuple[1:-1] + a_tuple[:1]
#    2* with every other item removed.
#           SOLUTION == a_string[0:-1:2] &
#                       a_tuple[0:-1:2]
#    3* with the first 4 and the last 4 items removed, and then
#       every other item in the remaining sequence.
#           SOLUTION == a_string[4:-4:2] &
#                       a_tuple[4:-4:2]
#    4* with the elements reversed (just with slicing).
#           SOLUTION == a_string[::-1] &
#                       a_tuple[::-1]
#    5* with the last third, then first third, then the middle
#       third in the new order.
#           SOLUTION == a_string[11:16] + a_string[0:5] + a_string[5:11] &
#                       a_tuple[4:6] + a_tuple[0:2] + a_tuple[2:4]
#
# NOTE: These should work with ANY sequence – but you can use
#       strings to test, if you like.
#
#
# Tests:
# a_string = "this is a string"
# a_tuple = (2, 54, 13, 12, 5, 32)
#
# assert exchange_first_last(a_string) == "ghis is a strint"
# assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
#---------------------------------------------------------------------

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """Returns an exchange of the first and last elements."""
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence


def every_other(seq):
    """Returns every other element."""
    a_new_sequence = seq[0:-1:2]
    return a_new_sequence


def first_last_four_every_other(seq):
    """Returns the first four, the last four and every other element."""
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence


def reverse_order(seq):
    """Returns the elements in reverse order"""
    a_new_sequence = seq[::-1]
    return a_new_sequence


def new_order(seq):
    """Returns the elements in a new order"""
    a_new_sequence = seq[]
    return a_new_sequence
    pass


# Assert Exchange First & Last
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
# Assert Every Other
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)
# Assert First Four, Last Four and Every Other
assert first_last_four_every_other(a_string) == " sas"
assert first_last_four_every_other(a_tuple) == ()
# Assert Reverse Order
assert reverse_order(a_string) == "gnirts a si siht"
assert reverse_order(a_tuple) == (32, 5, 12, 13, 54, 2)
# Assert Last Third, First Third and Middle Third
assert exchange_first_last(a_string) == "gtringthis is a s"
assert exchange_first_last(a_tuple) == (5, 32, 2, 54, 13, 12)

print("The assertions worked!")
