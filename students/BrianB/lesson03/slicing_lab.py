#!/usr/bin/env python3

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def exchange_first_last(seq):
    """Returns an exchange of the first element with the last element."""
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence


def every_other(seq):
    """Returns every other element in the sequence."""
    a_new_sequence = seq[0:-1:2]
    return a_new_sequence


def first_last_four_every_other(seq):
    """Returns the first four elements, then the last four\
    elements and every other element."""
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence


def reverse_order(seq):
    """Returns the elements in reverse order"""
    a_new_sequence = seq[::-1]
    return a_new_sequence


def new_order(seq):
    """Returns a New Order: the last three elements, then\
    the first three elements and then the middle three elements"""
    a_length = len(seq) // 3
    a_new_sequence = seq[a_length*2:] + seq[:a_length] + seq[a_length:a_length*2]
    return a_new_sequence


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
# Assert New Order
assert new_order(a_string) == "stringthis is a "
assert new_order(a_tuple) == (5, 32, 2, 54, 13, 12)

print("The assertions work!")
