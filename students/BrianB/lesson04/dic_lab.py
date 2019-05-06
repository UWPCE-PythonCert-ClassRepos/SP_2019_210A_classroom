#! bin/usr/env python3

d = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
    }


def dict_1():
    """Working with a dictionary"""
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
    for key, value in d1.items():
        if key == 'fruit':
            print('\nIs cake a key? ', False)

    # test if 'mango' is a value
    for key, value in d1.items():
        if value == 'Mango':
            print('\nIs mango a value?', True, '\n')
    return d1


def dict_2():
    """Working with a dictionary"""
    d2 = d
    print("The count of 't's in each value are: ")
    while True:
        for key, value in d2.items():
            print(key, ':', value.lower().count('t'))
        break
    return d2


# display dictionary keys:
dict_1()

# dictionary 2 function call
dict_2()
