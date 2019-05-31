#!/usr/bin/env python3

# Slicing Lab


def exchange_first_last(sequence):
    first = sequence[:1]
    last = sequence[-1:]
    middle = sequence[1:-1]
    exchanged = last + middle + first
    return exchanged


def remove_every_other(sequence):
    evens = sequence[0::2]
    return evens


def remove_first_and_last_4(sequence):
    middle = sequence[4:-4]
    evens = middle[0::2]
    return evens


def reversed(sequence):
    reversed = sequence[::-1]
    return reversed


def thirds(sequence):
    # last, first, middle
    size_of_3rds = int(len(sequence) / 3)
    first_3rd = sequence[0:size_of_3rds]
    last_3rd = sequence[-size_of_3rds:]
    middle_3rd = sequence[size_of_3rds:-size_of_3rds]
    new_sequence = last_3rd + first_3rd + middle_3rd
    return new_sequence


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
long_string = "abcdefghijklmnopqrst"
long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

assert remove_first_and_last_4(long_string) == "egikmo"
assert remove_first_and_last_4(long_tuple) == (5, 7, 9, 11, 13, 15)

assert reversed(a_string) == 'gnirts a si siht'
assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert thirds(a_string) == "tringthis is a s"
assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
