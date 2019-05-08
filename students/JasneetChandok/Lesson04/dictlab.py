#!/usr/bin/env python3.6

'''Lesson 4: Dictionary and Set Lab'''

# Dictionaries 1
dictSample = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
print(dictSample)

dictSample.popitem()
print(dictSample)

dictSample['fruit'] = 'Mango'
print(dictSample)

a = dictSample.keys()
print(a)
b = dictSample.values()
print(b)

'''
for k, v in dictSample.items():
    print('keys =',k,'values=',v)
'''
c = 'cake' in dictSample.keys()
print(c)

d = 'Mango' in dictSample.values()
print(d)


# Dictionaries 2
for dictkey in dictSample.keys():
    counter = 0
    for dictval in dictSample[dictkey]:
        if "t" == dictval.lower():
            counter += 1
    dictSample[dictkey] = counter
print(dictSample)


# Sets 1
s2 = set()
s3 = set()
s4 = set()

for num in range(0, 21):
    if num % 2 == 0:
        s2.add(num)
    if num % 3 == 0:
        s3.add(num)
    if num % 4 == 0:
        s4.add(num)

print('set2=', s2)
print('set3=', s3)
print('set4=', s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


# Sets 2
nameset = set("Python")
print(nameset)

nameset.add("i")
print(nameset)

nameset2 = frozenset("Marathon")
print(nameset2)

print('Union =', nameset.union(nameset2))
print('Intersection =', nameset.intersection(nameset2))