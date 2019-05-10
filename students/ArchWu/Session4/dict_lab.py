#!/usr/bin/env python3

def dict1():
    """
    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).

    """

    print(record1)
    for v in record1:
        if 'cake' in v:
            v.remove('cake')
    print(record1)
    record1['fruit'] = 'Mango'
    print(record1)
    print(record1.values())
    exist_mango = False
    for v in record1.values():
        if 'cake' in v:
            print("Error!")
        exist_mango = exist_mango or 'Mango' in v
    print(exist_mango)

def dict2():
    """ dict tracking number of t's in keys """
    print(record1)
    record2 = {}
    for k, v in record1.items():
        count = 0
        for letter in v:
            if letter == 't' or letter == 'T':
                count += 1
        record2[k] = count
    print(record2)

def sets():
    """
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    """
    s2 = {x for x in range(20) if x % 2 == 0}
    s3 = {x for x in range(20) if x % 3 == 0}
    s4 = {x for x in range(20) if x % 4 == 0}
    print(s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

def sets2():
    s1 = {x for x in 'Python'}
    s1.add('i')
    s2 = frozenset({x for x in 'marathon'})
    print(s1 | s2)
    print(s1 & s2)


if __name__ == '__main__':
    record1 = {'name': 'Chris', 'city':'Seattle'}
    dict1()
    dict2()
    sets()
    sets2()
