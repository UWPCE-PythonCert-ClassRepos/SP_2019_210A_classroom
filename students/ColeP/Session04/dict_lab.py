#!/usr/bin/env python3

# dictionaries 1

d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d1)
d1.pop('cake')
print(d1)
d1['fruit'] = 'Mango'
print(d1)

for i in d1:  # prints keys
    print(i)

for i in d1:  # prints values
    print(d1[i])

if 'cake' in d1:
    print(True)
else:
    print(False)

if 'Mango' in d1.values():
    print(True)
else:
    print(False)

# dictionaries 2
d2 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

for i in d2:
    counter = 0
    for j in d2[i]:
        if j == 't':
            counter += 1
    print(counter)

# sets 1

s2 = set()
s3 = set()
s4 = set()

for i in range(0, 21, 2):
    s2.add(i)
for i in range(0, 21, 3):
    s3.add(i)
for i in range(0, 21, 4):
    s4.add(i)

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# set 2
p = 'Python'
s5 = set()
for i in p:
    s5.add(i)

print(s5)
s5.add('i')

s6 = set()
for q in 'marathon':
    s6.add(q)
s6 = frozenset(s6)

print(s5.union(s6))

print(s5.intersection(s6))

