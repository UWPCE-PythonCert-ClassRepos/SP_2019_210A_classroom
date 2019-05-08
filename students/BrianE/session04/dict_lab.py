#!/usr/bin/env python3

"""
Dictionaries 1
    * Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
      (so the keys should be: “name”, etc, and values: “Chris”, etc.)
    * Display the dictionary.
    * Delete the entry for “cake”.
    * Display the dictionary.
    * Add an entry for “fruit” with “Mango” and display the dictionary.
        * Display the dictionary keys.
        * Display the dictionary values.
        * Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
        * Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""

# Construct dictionary
dict_1 = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
print(dict_1)

# Remove cake entry
del dict_1['cake']
print(dict_1)

# Add fruit to dictionary
dict_1['fruit'] = 'Mango'

# Display keys
print(dict_1.keys())

# Display values
print(dict_1.values())

# Test for specific keys/values
print(f'"cake" is a key within dict_1: {"cake" in dict_1.keys()}')
print(f'"Mango" is a value within dict_1: {"Mango" in dict_1.values()}')


"""
Dictionaries 2
    * Using the dictionary from item 1: Make a dictionary using the same keys but with 
      the number of ‘t’s in each value as the value (consider upper and lower case?).
"""

dict_2 = {}

for key in dict_1.keys():
    dict_2[key] = dict_1[key].lower().count('t')  # Count 't' in each key's value

print()
print(dict_2.keys())
print(dict_2.values())


"""
Sets 1
    * Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
    * Display the sets.
    * Display if s3 is a subset of s2 (False)
    * and if s4 is a subset of s2 (True).
"""

# Generate sets
s2 = set([num for num in range(0, 21) if num % 2 == 0])
s3 = set([num for num in range(0, 21) if num % 3 == 0])
s4 = set([num for num in range(0, 21) if num % 4 == 0])
print(f'\ns2 = {s2}\ns3 = {s3}\ns4 = {s4}')

# Check subsets
print(f'{s3} is a subset of {s2}: {s3.issubset(s2)}')
print(f'{s4} is a subset of {s2}: {s4.issubset(s2)}')


"""
Sets 2
    * Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    * Create a frozenset with the letters in ‘marathon’.
    * display the union and intersection of the two sets.
"""

s5 = set('frozen')
s5.add('i')
fs = frozenset('marathon')

print()
print(f'Union of {s5} and {fs} = {s5.union(fs)}')
print(f'Intersection of {s5} and {fs} = {s5.intersection(fs)}')
