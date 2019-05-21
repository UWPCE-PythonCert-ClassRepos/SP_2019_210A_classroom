
'''Some Examples'''
feast = ['lambs', 'sloths', 'orangutans',
             'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

print(comprehension[0])
print(comprehension[2])

comprehension = {c for c in 'aabbbcccc'}
print(comprehension)


dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third':'ruthless efficiency',
                   'forth':'fanatical devotion',
                   'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print(len(dict_comprehension))


'''count even numbers'''

def count_evens(nums):
    comprehension = [x for x in nums if (x % 2 == 0) ]
    return len(comprehension)

print(count_evens([2,4,5,7]))
assert count_evens([2,4,5,6,3]) == 3
assert count_evens([3,4,33,21,55,32,45,62,0]) == 4

'''dict and set comprehension
Dictionaries and set lab in lesson4
'''
dict1 = {'name': 'Chris',
         'city': 'Seattle',
         'cake': 'Chocolate'}
print(dict1)

dict2 = {key: value.lower().count('t') for key, value in dict1.items()}

'''
dict2 = {}
for key in dict1.keys():
    dict2[key] = dict1[key].lower().count('t')
    #key = key.lower().count('t')
    #print(key)
'''

print(dict2.keys())
print(dict2.values())

'''Another comprehensions in dicts exercise'''

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
'''
Print the dict by passing it to a string format method, so that you get something like:

“Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
'''

print("{name} is from {city}, and he likes {cake} cake,{fruit} fruit,{salad} salad, and {pasta}pasta".format(**food_prefs))

'''
Using a list comprehension, build a dictionary of numbers from zero to fifteen 
and the hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number as a string)
'''
numbers = [number for number in range(16)]
print(numbers)
hex_numbers = [hex(x) for x in range(16)]
print(hex_numbers)

'''
dict comprehension
'''
comprehension = {number : hex(number) for number in range(16)}
print(comprehension)

'''
Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value.
You can do this either by editing the dict in place, 
or making a new one. If you edit in place make a copy first!
'''
count_a = {key: value.lower().count('a') for key, value in food_prefs.items()}
print(count_a)



'''
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Do this with one set comprehension for each set.
'''
s2 = {x for x in range(21) if x % 2 == 0}
print(s2)
s3 = {x for x in range(21) if x % 3 == 0}
print(s3)
s4 = {x for x in range(21) if x % 4 == 0}
print(s4)

'''
find the set when divisors are more than three
'''
y = [2,3,4,5]
divisors = {x for x in range(21) for each in y if x % each == 0}
print(divisors)






#[(numbers, hexadecimal)]
# def dict_comprehension():
#
#     return {v : k for k, v in food_prefs.items()}
#
# print(dict_comprehension())
#comprehension = "{0} is from {1}, and he likes {2}".format(food_prefs[name], food_prefs[city], [value, key for key, value in food_prefs.items()])