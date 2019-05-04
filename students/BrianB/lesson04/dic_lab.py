#! bin/usr/env python3

'''
Dictionaries 1
    Create a dictionary containing “name”, “city”, and “cake” for
        “Chris” from “Seattle” who likes “Chocolate” (so the keys
        should be: “name”, etc, and values: “Chris”, etc.)
        
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
        Display the dictionary keys.
        Display the dictionary values.
        Display whether or not “cake” is a key in the dictionary
            (i.e. False) (now).
        Display whether or not “Mango” is a value in the dictionary
            (i.e. True).

Dictionaries 2
    Using the dictionary from item 1: Make a dictionary using
        the same keys but with the number of ‘t’s in each value
        as the value (consider upper and lower case?).

'''


def dict_1():
    d1 = {
        'name': 'Chris',
        'city': 'Seattle',
        'cake': 'Chocolate'
        }

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
    for (key, value) in d1.items():
        print(key, ': ', value)

    # display the dictionary keys
    print('\n', d1.keys())

    # display the dictionary values
    print('\n', d1.values())

    # test if 'cake' is no longer a key
    for key, value in d1.items():
        if key == 'fruit':
            print('\nIs cake a key? ', False)

    # test if 'mango' is a value
    for key, value in d1.items():
        if value == 'Mango':
            print('\nIs mango a value?', True, '\n')

    # print number of t's in values
    # expect to see {name: 0, city: 2, fruit: 0}
    for key, value in d1.items():
        for item in value:
            if 't' in item.lower():
                print(key, ':', len(item))
            else:
                print(key, ':', 0)
            break
    return d1


# display dictionary keys:
dict_1()


