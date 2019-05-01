#!/usr/bin/env python3

d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d1)
d1.pop('city')
print(d1)
d1['fruit'] = 'Mango'
print(d1)

for i in d1:
    print(i)
    print(d1[i])
