#------------------- Script Details--------------------------------------#
# Week 3 Homework: Slicing Lab
# Miguel Rovira-Gonzalez, 4/30/19, Created the Slicing Lab Script
#-----------------------------------------------------------------------#
"""Goal of the Lab:
Write some functions that take a sequence as an argument, and return a copy of that sequence:
    with the first and last items exchanged. [complete]
    with every other item removed. [complete]
    with the first 4 and the last 4 items removed, and then every other item in the remaining sequence. [complete]
    with the elements reversed (just with slicing). [complete]
    with the last third, then first third, then the middle third in the new order. [complete]
This should work with any sequence
"""
seq = [1, 5, 10, 15]
tup = (1, 5, 10, 15)
long_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_char = "Pythonisfun"

def exchange_first_last(seq):
    """
    Flipping the first and last element in a sequence and returning a sequence [List, Tuple, String]
    :param seq: the parameter sequence
    :return: the sequence with the first and last element flipped"
    """
    return seq[-1:] + seq[1:3] + seq[:1]

assert exchange_first_last(seq) == [15, 5, 10, 1]
assert exchange_first_last(tup) == (15, 5, 10, 1)
print("Tuple First Last Test Passed", exchange_first_last(tup))
print("First Last Assertion Test Passed:", exchange_first_last(seq))

def every_other(seq):
    """
    Removing every other item in a sequence
    :param seq: the parameter sequence
    :return: the sequence with every other item removed"
    [Slicing Start: Slicing End: Step]
    """
    return seq[::2]

assert every_other(seq) == [1,10]
print("Every other test method worked:", every_other(seq))

def first_last_four_every(long_seq):
    """
    Removing the first four and then the last four elements
    :param long_seq: the parameter sequence
    :return  Return a sequence the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    """
    return long_seq[4:-4][::2]

assert first_last_four_every(long_seq)
print("First_last_four_every test passed", first_last_four_every(long_seq))

def reverse(seq):
    """
    Reversing the order of the elements in a sequence
    :param seq: sequence that will be reversed
    :return: sequence with elements reversed
    """
    return seq[::-1]

assert reverse(seq) == [15, 10, 5, 1]
print("Reverse test passed:", reverse(seq))

def find(str_length):
    """
    with the last third, then first third, then the middle third in the new order.
    :param str_length:
    :return: new sequence with the last third, then first third, then the middle third in the new order
    """
    str_char = int(len(str_length) / 3)
    first_str = str_length[:str_char]
    end_str = str_length[-str_char:]
    mid_str = str_length[str_char:str_char + str_char]
    return end_str + first_str + mid_str

assert find(string_char) == 'funPython'
print("Python is fun, it is:", find(string_char))














