#!/usr/bin/env python3

d = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
    }


def dict_1():
    """
    reads a dictionary

    Returns: dictionary, deletes one key, adds a new key: value, displays the
    new key: value, displays dictionary keys and values and test if 'cake' is
    a key and test if 'Mango' is a value

    """
    d1 = d

    # display dictionary
    print('Original Dictionary: ', d1)

    # delete key, cake
    del d1['cake']

    # display dictionary without cake
    print('\nDictionary with key "cake" deleted: ', d1, '\n')

    # add dictionary with a fruit
    d1.update({'fruit': 'Mango'})

    # display dictionary with new key and value
    print('Key, value with fruit, mango added:')
    for key, value in d1.items():
        print(key, ': ', value)

    # display the dictionary keys
    print('\n', d1.keys())

    # display the dictionary values
    print('\n', d1.values())

    # test if 'cake' is no longer a key
    #for key, value in d1.items():
    if 'cake' in d1.keys():
        print(True)
    else:
        print(False)

    # test if 'mango' is a value
    if 'Mango'in d1.values():
        print(True)
    else:
        print(False)
    return d1


def dict_2():
    """
    reads a dictionary

    Returns: the count of 't' in dictionary values

    """
    d2 = d
    print("The count of 't's in each value are: ")
    while True:
        for key, value in d2.items():
            print(key, ':', value.lower().count('t'))
        break
    return d2


if __name__ == "__main__":
    # display dictionary keys:
    dict_1()
    # dictionary 2 function call
    dict_2()
