#!/usr/bin/env python3

"""
Not much to submit due to the code being provided.
Typing out the code to start gaining the muscle memory
and written understanding of comprehensions
"""

def delicay_comprehension():
    feast = ["lambs", "sloths", "organutans", "breakfast cereals", "fruit bats"]

    comprehensions = [delicay.capitalize() for delicay in feast]

    # prints Lambs
    print(comprehensions[0])

    # prints Sloths
    print(comprehensions[1])

delicay_comprehension()


def filter_feast():
    feast = ["spam", "sloths", "orangutans", "breakfast cereals", "fruit bats"]

    comp = [delicay for delicay in feast if len(delicay) > 6]

    # prints 5
    print(len(feast))


    # prints 3
    print(len(comp))

filter_feast()


def unpacking_tuples():
    list_of_tuples = [(1, "lumberjack"), (2, "inquisition"), (4, "spam")]

    comprehension = [skit * number for number, skit in list_of_tuples]

    # prints "lumberjack"
    print(comprehension[0])

    # print 16
    print(len(comprehension[2]))

unpacking_tuples()


def double_list():
    eggs = ["poached egg", "fried egg"]
    meats = ["lite spam", "ham spam", "fried spam"]

    comprehension = ["{0} and {1}".format(egg, meat) for egg in eggs for meat in meats]

    # prints 6
    print(len(comprehension))

    # prints "poached egg and lite spam"
    print(comprehension[0])

double_list()


def set_comprehensions():
    comprehension = { c for c in "aaabbbcccc"}

    # prints a random set of only "a  b c"
    print(comprehension)

set_comprehensions()


def dictionary_comprehensions():
    dict_of_weapons = {"first": "fear",
                       "second": "surprise",
                       "third": "ruthless efficiency",
                       "fourth": "fanatical devotion",
                       "fifth": None
}

    dict_comprehensions = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon }

    # sets all keys to upper case and prints them followed by the value
    print(dict_comprehensions)

dictionary_comprehensions()