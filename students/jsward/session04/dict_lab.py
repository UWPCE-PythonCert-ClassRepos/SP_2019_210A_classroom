#!/usr/bin/env python

################
# Dictionaries 1
################
stuff = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print(stuff)

stuff.pop("cake")

print(stuff)

stuff["fruit"] = "Mango"

print(stuff)

print(stuff.keys())

print(stuff.values())

print(stuff.__contains__("cake"))

if list(stuff.values()).count("Mango") > 0:
    print(True)
else:
    print(False)

################
# Dictionaries 2
################
stuff = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

new_dict = {key: value.lower().count('t') for key, value in stuff.items()}

print(new_dict)

######
# Sets
######
s2 = set([r for r in range(21) if r % 2 == 0])
print(s2)
s3 = set([r for r in range(21) if r % 3 == 0])
print(s3)
s4 = set([r for r in range(21) if r % 4 == 0])
print(s4)
print(set(s3).issubset(s2))
print(set(s4).issubset(s2))

s5 = set([l for l in "Python"])
s5.update('i')
print(s5)
fs1 = frozenset([l for l in "Marathon"])
print(fs1)

print(s5.union(fs1))
print(s5.intersection(fs1))