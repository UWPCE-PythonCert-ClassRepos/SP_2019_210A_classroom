#!/usr/bin/env python3

"""
Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”
(so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
"""
# Creates the dict
dictionaries_one = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(dictionaries_one)

# Removes the cake item
dictionaries_one.pop("cake")
print(dictionaries_one)

# Add fruit entries
dictionaries_one["fruit"] = "Mango"
print(dictionaries_one)

"""
    - Display the dictionary keys.
    - Display the dictionary values.
    - Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    - Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
print(dictionaries_one.keys())
print(dictionaries_one.values())
# Not sure which one for "cake" is more correct and if adding .keys() is too verbose
print("cake" in dictionaries_one)
print("cake" in dictionaries_one.keys())

print("Mango" in dictionaries_one.values())

"""
Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the
same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
"""
# Make copy of dictionaries_one to not overwrite the original example
dictionaries_two = dictionaries_one.copy()


# iterate over each key value and find the 't'
# make each key's value the number to 't's found in the values
for i in dictionaries_two.values():
    n = i.count("t")
    print(n)


"""
Sets 1
"""
s2 = set()
s3 = set()
s4 = set()

def loop_over_numbers():
    for number in range(1, 21):
        if number % 2 == 0:
            # s2.update([number])
            s2.add(number)
            print(s2)
        elif number % 3 == 0:
            s3.add(number)
            print(f"s3: {s3}")
        elif number % 4 == 0:
            s4.add(number)
            print(f"S4: {s4}")

    print(s2)
    print(s3)
    print(s4)
    print(s3 == s2)
    print(s4 == s2)

loop_over_numbers()

"""
Sets 2
"""
def create_python_set():
    python_set = set("Python")
    python_set.add("i")
    frozen_marathon = frozenset("marathon")

    join_sets = python_set.union(frozen_marathon)
    return join_sets

print(create_python_set())