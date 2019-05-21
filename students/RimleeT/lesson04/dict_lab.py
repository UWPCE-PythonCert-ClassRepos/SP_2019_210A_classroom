"""Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True)."""


dict1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
print ( dict1)
dict1.pop('cake')
print ( 'After deleting "cake" : ',dict1)
dict1['fruit'] = 'Mango'
print ( 'After adding "fruit" : ',dict1)
for key in dict1:
    print('Keys are: ', key)
for key,values in dict1.items():
    print('Values are: ', values)
if 'cake' in dict1:
    print('Cake exists as key')
else:
    print('Cake does not exist as key')
if 'Mango' in dict1.values():
    print('Mango exists as value')
else:
    print('Mango does not exist as value')


"""Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).
The result should look something like:
{"name": 0
 "city": 2
 "cake": 2
}"""

new_dict = {}
for key,value in dict1.items():
    new_dict[key] = value.count('t')
print(new_dict)


"""Sets
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True)."""

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i%2==0:
        s2.add(i)
for i in range(21):
    if i%3==0:
        s3.add(i)
for i in range(21):
    if i%4==0:
        s4.add(i)
print('s2: ', s2)
print('s3: ', s3)
print('s4: ', s4)
print('s3 is subset of s2? ' , s3.issubset(s2))
print('s4 is subset of s2? ' , s4.issubset(s2))

"""Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
Display the union and intersection of the two sets."""


s2 = frozenset()
s1 = {'P','y','t','h','o','n'}
s1.add('i')
s2 = ('m','a','r','a','t','h','o','n')
print('s1: ', s1)
print('s2: ', s2)
print('union: ', s1.union(s2))
print('intersection: ', s1.intersection(s2))


      


            





