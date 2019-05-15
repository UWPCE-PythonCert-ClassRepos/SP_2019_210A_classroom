#!/usr/bin/env python3


#class DictLabComprehensions():
#    '''
#    dict_lab.py updated
#
#    return: dict_lab with comprehensions
#    '''
#
#    @property
def dict_1():
    """
    reads a dictionary

    Returns: dictionary, deletes one key, adds a new key: value, displays
    the new key: value, displays dictionary keys and values and test if
    'cake' is a key and test if 'Mango' is a value.

    """

    food_prefs = {"name": "Chris",
                  "city": "Seattle",
                  "cake": "chocolate",
                  "fruit": "mango",
                  "salad": "greek",
                  "pasta": "lasagna"}

    # Print the dict by passing it to a string format method,
    # so that you get something like:
    #
    #   “Chris is from Seattle, and he likes chocolate cake,
    #    mango fruit, greek salad, and lasagna pasta”
    return '''{} is from {}, and he likes {}, {}, {} and {}.'''\
        .format(food_prefs.values(), food_prefs.values(),
                food_prefs.values(), food_prefs.values(),
                food_prefs.values(), food_prefs.values())

#class SetLabComprehensions():
#    '''
#    set_lab.py updated
#
#    return: set_lab with comprehensions
#    '''
    # source of info on sets and frozen sets:
    #   https://www.python-course.eu/sets_frozensets.php

    # Create sets s2, s3 and s4 that contain numbers
    #   from zero through twenty, divisible by 2, 3 and 4
    #s2 = set()
    #s3 = set()
    #s4 = set()
#
    #for number in range(21):
    #    if not number % 2:
    #        s2.add(number)
    #    if not number % 3:
    #        s3.add(number)
    #    if not number % 4:
    #        s4.add(number)
#
    #print(s2)
    #print(s3)
    #print(s4)
#
    ## Display if s3 is a subset of s2 (False)
    ## print(all([z in s2 for z in s3]))
    #print(s3.issubset(s2))
#
    ## Display if s4 is a subset of s2 (True)
    ## print(all([z in s2 for z in s4]))
    #print(s4.issubset(s2))
#
    ## Create a set with the letters in ‘Python’
    ## and add ‘i’ to the set.
    #s = set('Python')
    #s.add('i')
#
    #print(s)
#
    ## Create a frozenset with the letters in ‘marathon’.
    #fz = frozenset('marathon')
    #print(fz)
#
    ## Display the union and intersection of the two sets.
    #a = s.union(fz)
    #print('union of "python" and "marathon: ', a)
    #a = s.intersection(fz)
    #print('intersection of "python" and "marathon: ', a)


if __name__ == "__main__":
    # display dictionary keys:
    #d = DictLabComprehensions()
    print(dict_1())
