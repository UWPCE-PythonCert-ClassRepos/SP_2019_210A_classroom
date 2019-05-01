#!/usr/env python3

"""
SlicingLab.py

Sequence manipulation to achieve the following:
    * the first and last items exchanged.
    * every other item removed.
    * the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    * the elements reversed (just with slicing).
    * the last third, then first third, then the middle third in the new order.
"""


def exchange_first_last(sequence):
    """
    Return sequence with first and last elements exchanged.

    :param sequence: input sequence (string, list, tuple, etc)
    :return: sequence of same type with first and last elements swapped
    """

    return sequence[-1::] + sequence[1:-1] + sequence[:1]


def remove_every_other_element(sequence):
    """
    Return sequence with every other element removed.

    :param sequence: input sequence (string, list, tuple, etc)
    :return: sequence with every other element removed
    """

    return sequence[::2]


def remove_first_last_4_every_other(sequence):
    """
    Return sequence with first/last four removed along with every other element removed.

    :param sequence: input sequence (string, list, tuple, etc)
    :return: sequence with first/last four removed along with every other element removed
    """

    return sequence[4:-4][::2]


def reverse(sequence):
    """
    Return sequence with elements reversed.

    :param sequence: input sequence (string, list, tuple, etc)
    :return: sequence with elements reversed
    """

    return sequence[::-1]


def reorder_third(sequence):
    """
    Return sequence with elements reordered, starting with last third, then first third and finally middle.

    :param sequence: input sequence (string, list, tuple, etc)
    :return: sequence with elements reordered, starting with last third, then first third and finally middle.
    """

    group_size = len(sequence) // 3
    return sequence[(group_size * 2)::] + sequence[:group_size:] + sequence[group_size:(group_size * 2):]


def main():
    a_string = "this is a string"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a_tuple = (20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_list) == [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
    assert exchange_first_last(a_tuple) == (31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20)

    assert remove_every_other_element(a_string) == "ti sasrn"
    assert remove_every_other_element(a_list) == [1, 3, 5, 7, 9, 11, 13]
    assert remove_every_other_element(a_tuple) == (20, 22, 24, 26, 28, 30)

    assert remove_first_last_4_every_other(a_string) == " sas"
    assert remove_first_last_4_every_other(a_list) == [5, 7, 9]
    assert remove_first_last_4_every_other(a_tuple) == (24, 26)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_list) == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse(a_tuple) == (31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20)

    assert reorder_third(a_string) == "stringthis is a "
    assert reorder_third(a_list) == [9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8]
    assert reorder_third(a_tuple) == (28, 29, 30, 31, 20, 21, 22, 23, 24, 25, 26, 27)

    print("All assertions passed!")


if __name__ == '__main__':
    main()

