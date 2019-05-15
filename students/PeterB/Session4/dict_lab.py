#!/usr/bin/env python3

# part 1

dict1={'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(dict1)
dict1.pop('cake')
print(dict1)
dict1['fruit']='Mango'
print(dict1.keys())
print(dict1.values())

if 'cake' in dict1.keys():
    print(True)
else:
    print(False)

if 'Mango' in dict1.values():
        print(True)
else:
        print(False)


# part 2

dict1={'name':'0','city':'2','fruit':'0'}
print(dict1)

# sets

contain = 0
s1list = []; s2list = []; s3list = []
while contain <=20:
    if contain%2==0:
        s1list.append(contain)
    if contain%3==0:
        s2list.append(contain)
    if contain%4==0:
        s3list.append(contain)
    contain += 1
print(s1list); print(s2list); print(s3list)


# set 2

word = list("Python")
s4 = set(word)
print(s4)
s4.add('i')
print(s4)

word2 = 'marathon'
s5 = frozenset(word2)
print(s5)
print(s4.union(s5))
print(s4.intersection(s5))