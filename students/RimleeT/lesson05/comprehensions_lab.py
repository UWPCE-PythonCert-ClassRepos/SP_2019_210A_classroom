"""Count even numbers"""
def count_evens(nums):
    total_even = len([nums for item in nums if item % 2 == 0])
    return total_even

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0



food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

"""Print the dict by passing it to a string format method, so that you get something like:
“Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”"""
food_string = "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta"
print(food_string.format(**food_prefs))


"""Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). 
(the hex() function gives you the hexidecimal representation of a number as a string)"""
hex_list_dict = dict((i, hex(i)) for i in range(16))
print(hex_list_dict)


"""Do the previous entirely with a dict comprehension – should be a one-liner"""
hex_dict = {i: hex(i) for i in range(16)}
print(hex_dict)

"""Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!"""
a_dict = {key: value.count('a') for key, value in food_prefs.items()}
print(a_dict)


"""Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Do this with one set comprehension for each set.
What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.
The idea here is that when you see three (Or more!) lines of code that are almost identical, then you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.
Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
"""
set_lists = [{num for num in range(21) if num%divisor == 0} for divisor in [2,3,4]]
print(set_lists)