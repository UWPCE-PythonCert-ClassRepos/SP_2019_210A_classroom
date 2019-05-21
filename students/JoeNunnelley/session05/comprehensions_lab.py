#! /usr/bin/env python3

"""
List comprehensions

Note: this is a bit of a “backwards” exercise – we show you code, you figure out what it does.

As a result, not much to submit – don’t worry about it – you’ll have a chance to use these in other exercises.

>>> feast = ['lambs', 'sloths', 'orangutans',
             'breakfast cereals', 'fruit bats']

>>> comprehension = [delicacy.capitalize() for delicacy in feast]

What is the output of:

>>> comprehension[0]
Lambs

>>> comprehension[2]
Orangutans

(figure it out before you try it)
Filtering lists with list comprehensions

>>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

>>> comp = [delicacy for delicacy in feast if len(delicacy) > 6]

What is the output of:

>>> len(feast)
5

>>> len(comp)
3

(figure it out first!)
Unpacking tuples in list comprehensions

>>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

>>> comprehension = [ skit * number for number, skit in list_of_tuples ]

What is the output of:

>>> comprehension[0]
lumberjack

>>> len(comprehension[2])
16

Double list comprehensions

>>> eggs = ['poached egg', 'fried egg']

>>> meats = ['lite spam', 'ham spam', 'fried spam']

>>> comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

What is the output of:

>>> len(comprehension)
6

>>> comprehension[0]
poached egg and lite spam

Set comprehensions

>>> comprehension = { c for c in 'aabbbcccc'}

What is the output of:

>>> comprehension
{'a', 'b', 'c'}

"""


"""
Dictionary comprehensions

>>> dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
>>> dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

What is the output of:

>>> 'first' in dict_comprehension
False
>>> 'FIRST' in dict_comprehension
True
>>> len(dict_of_weapons)
5
>>> len(dict_comprehension)
4
"""


"""
Other resources

See also:

https://github.com/gregmalcolm/python_koans/blob/master/python3/koans/about_comprehension.py

From Greg Malcolm’s excellent Python Koans series:

https://github.com/gregmalcolm/python_koans
Count Even Numbers

This is from CodingBat “count_evens” (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even integers in the given list.

Note: the % “mod” operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) == 3

count_evens([2, 2, 0]) == 3

count_evens([1, 3, 5]) == 0

Can you do this with a single line comprehension?

def count_evens(nums):
   return len([num for num in nums if num % 2 == 0])

dict and set comprehensions

Revisiting the dict/set lab – see how much you can do with comprehensions instead.

(Dictionary and Set Lab)

Specifically, look at these:

First a slightly bigger, more interesting (or at least bigger..) dict:
"""

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
"""
Working with this dict:

    Print the dict by passing it to a string format method, so that you get something like:

    “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”

    Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number as a string)

    Do the previous entirely with a dict comprehension – should be a one-liner

    Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!

    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

            Do this with one set comprehension for each set.
            What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
                create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
                loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.
                The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.
            Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)

"""

defined_format = "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta"

print(defined_format.format(**food_prefs))

hex_dict = {num: hex(num) for num in range(0,15)}
print(hex_dict)

a_dict = {item: item.count('a') for item in food_prefs}
print(a_dict)

divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10]
s_sets = []
for div in divisors:
    s_sets.append({ item for item in range(0,21) if item % div == 0 })

print(s_sets)

print(
    [ { item for item in range(0,20) for s in [2,3,4,5,6,7,8,9,10] if item % s == 0  } ]
)