#!/usr/bin/env python3

"""
demo of indexing vs slicing
"""


def exchange_first_last(seq):
    """
    From the slicing lab:
     - exchanging the first and last items in a sequence.

    This should work with any sequence:
    """
    first = seq[:1]
    print(first)
    mid = seq[1:-1]
    print(mid)
    last = seq[-1:]
    print(last)
    return last + mid + first

# try it out:

# with a list
result = exchange_first_last([1, 2, 7, 2, 5, 3])
assert result == [3, 2, 7, 2, 5, 1], f"got: {result}"

# with a tuple
result = exchange_first_last((1, 2, 7, 2, 5, 3))
assert result == (3, 2, 7, 2, 5, 1), f"got: {result}"

# with a string
result = exchange_first_last("this is something")
assert result == "ghis is somethint", f"got: {result}"

