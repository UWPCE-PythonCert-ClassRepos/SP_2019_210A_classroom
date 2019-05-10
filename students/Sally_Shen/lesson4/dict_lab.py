'''
Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
'''

dict1 = dict([('name', 'Chris'), ('city', 'Seattle'), ('cake', 'Chocolate')])
print(dict1)


del dict1['cake']
print(dict1)

dict1['fruit'] = 'Mango'
print(dict1)


print(dict1.keys())

print(dict1.values())

is_key = 'cake' in dict1.keys()
print(is_key)

is_value = 'Mango' in dict1.values()
print(is_value)



'''
Dictionaries 2
'''

dict2 = {}

for key in dict1.keys():
    dict2[key] = dict1[key].lower().count('t')

print(dict2.keys())
print(dict2.values())


'''
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
'''
s2 = set()
s3 = set()
s4 = set()

for num in range(0,21):
    if num % 2 ==0:
        s2.add(num)
    if num % 3 ==0:
        s3.add(num)
    if num % 4 ==0:
        s4.add(num)
print(s2)
print(s3)
print(s4)
# Check subsets
print(s3.issubset(s2))
print(s4.issubset(s2))



'''
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
Display the union and intersection of the two sets.
'''

add_letter = set('Python')
add_letter.add('i')
print(add_letter)


frozen_set = frozenset('marathon')
print(frozen_set)

print('Union of the two sets is', add_letter.union(frozen_set))
print('Intersection of the two set is', add_letter.intersection(frozen_set))

