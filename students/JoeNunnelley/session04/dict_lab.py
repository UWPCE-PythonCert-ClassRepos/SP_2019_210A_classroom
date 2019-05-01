#! /usr/bin/env python3
"""
Session 04: Dictionaries and Sets Lab
Author : Joe Nunnelley
"""


def dictionaries_one():
    """
    Dictionaries 1

        Create a dictionary containing “name”, “city”, and “cake” for “Chris”
        from “Seattle” who likes “Chocolate” (so the keys should be: “name”,
        etc, and values: “Chris”, etc.)
        Display the dictionary.
        Delete the entry for “cake”.
        Display the dictionary.
        Add an entry for “fruit” with “Mango” and display the dictionary.
            Display the dictionary keys.
            Display the dictionary values.
            Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
            Display whether or not “Mango” is a value in the dictionary (i.e. True).
    """
    person = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(person)
    person.pop("cake")
    print(person)
    person['fruit'] = 'Mango'
    print(person)
    print(person.keys())
    print(person.values())

    if 'cake' in person.keys():
        print('found cake')
    else:
        print('no cake found')

    if 'Mango' in person.values():
        print('found value Mango')
    else:
        print('did not find value Mango')

def dictionaries_two():
    """
    Dictionaries 2

        Using the dictionary from item 1: Make a dictionary using the same keys but with
        the number of ‘t’s in each value as the value (consider upper and lower case?).
    """
    person = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    person['Tomato'] = '20'
    new_dict = {}
    for key, _ in person:
        count = key.upper().count('T')
        print('key [{}] has [{}] letters t'.format(key, count))
        new_dict[key] = count

    print(new_dict)

def sets_one():
    """
    Sets

        Create sets s2, s3 and s4 that contain numbers from zero through twenty,
        divisible by 2, 3 and 4.
            Display the sets.
            Display if s3 is a subset of s2 (False)
            and if s4 is a subset of s2 (True).
    """

    set_2 = set(range(0, 21, 2))
    set_3 = set(range(0, 21, 3))
    set_4 = set(range(0, 21, 4))
    print(set_2)
    print(set_3)
    print(set_4)

    print("Set_3 is subset of Set_2: {}".format(set_3.issubset(set_2)))
    print("Set_4 is subset of Set_2: {}".format(set_4.issubset(set_2)))


def sets_two():
    """
    Sets 2

        Create a set with the letters in ‘Python’ and add ‘i’ to the set.
        Create a frozenset with the letters in ‘marathon’.
        display the union and intersection of the two sets
    """

    snake = set(['P', 'y', 't', 'h', 'o', 'n'])
    snake.add('i')
    frozen_snake = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
    print(snake)
    print(frozen_snake)
    print("Union: {}".format(snake.union(frozen_snake)))
    print("Intersection: {}".format(snake.intersection(frozen_snake)))

if __name__ == "__main__":
    dictionaries_one()
    dictionaries_two()
    sets_one()
    sets_two()
