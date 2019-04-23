#! /usr/bin/env python3
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

    - with the first and last items exchanged.
    - with every other item removed.
    - with the first 4 and the last 4 items removed, and then every other item in the
      remaining sequence.
    - with the elements reversed (just with slicing).
    - with the last third, then first third, then the middle third in the new order.
"""
# 1 - exchange first and last
def exchange_first_last(seq):
    return seq[-1::] + seq[1:-1] + seq[0:1]

# 2 - remove every other item
def every_other_item_removed(seq):
    return seq[0::2]

# 3 - remove 4 on each end and return every other item
def remove_four_bookends_and_every_other(seq):
    internal = seq[4:-4]
    if len(internal) > 0:
        return every_other_item_removed(internal)
    else:
        print('No sequence remains')
        return None

# 4 - reversed by slicing a sequence
def reversed_by_slicing(seq):
    return seq[::-1]

# 5 - swap sequences by thirds
def swap_thirds(seq):
    """
    swap thirds evenly if length divisble by 3
    swap n1, n2, n3 => n3, n2, n1
    swap n1 + 1, n2, n3  => n3, n1+ 1, n2 for count % 3 = 1
    swap n1 + 1, n2 + 1, n3 => n3, n1 + 1, n2 + 1 for count % 3 = 2
    """
    sub = len(seq) // 3
    return seq[-sub::] + seq[0:sub] + seq[sub:-2]


if __name__ == "__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [2, 4, 5, 6, 7, 8]

    print('Running exchange_first_last tests...')
    assert exchange_first_last(a_string) == 'ghis is a strint'
    assert exchange_first_last(a_tuple)  == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_tuple)  == (32, 54, 13, 12, 5, 2)
    print('No asserts. Functionality correct')
    print()

    a_string = 'this is a string'
    a_tuple = (1,2,3,4,5,6,7,8,9)
    a_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

    print('Running every_other_item_removed tests...')
    assert every_other_item_removed(a_string)   == 'ti sasrn'
    assert every_other_item_removed(a_tuple)    == (1, 3, 5, 7, 9)
    assert every_other_item_removed(a_list)     == ['one', 'three', 'five', 'seven']
    print('No asserts. Functionality correct')
    print()

    a_string = 'this is a longer string'
    a_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('Running remove_four_bookends_and_every_othertests...')
    assert remove_four_bookends_and_every_other(a_string)   == ' salne t'
    assert remove_four_bookends_and_every_other(a_tuple)    == (4, 6)
    assert remove_four_bookends_and_every_other(a_list)     == [4, 6]
    print("No asserts. Functionality correct.")
    print()

    print('Running reversed_by_slicing tests...')
    assert reversed_by_slicing(a_string)    == 'gnirts regnol a si siht'
    assert reversed_by_slicing(a_tuple)     == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    assert reversed_by_slicing(a_list)      == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print('No asserts. Functionality correct.')
    print()

    print('Running swap_thirds tests...')
    assert swap_thirds('abcdef')            == 'efabcd'
    assert swap_thirds((1, 2, 3, 4, 5, 6))  == (5, 6, 1, 2, 3, 4)
    assert swap_thirds([1, 2, 3, 4, 5, 6])  == [5, 6, 1, 2, 3, 4]
    assert swap_thirds('abcdefg') == 'fgabcde'
    assert swap_thirds('abcdefgh') == 'ghabcdef'
    assert swap_thirds((1, 2, 3, 4, 5, 6, 7)) == (6, 7, 1, 2, 3, 4, 5)
    assert swap_thirds([1, 2, 3, 4, 5, 6, 7]) == [6, 7, 1, 2, 3, 4, 5]
    assert swap_thirds((1, 2, 3, 4, 5, 6, 7, 8)) == (7, 8, 1, 2, 3, 4, 5, 6)
    assert swap_thirds([1, 2, 3, 4, 5, 6, 7, 8]) == [7, 8, 1, 2, 3, 4, 5, 6]
    print('No asserts. Functionality correct.')
