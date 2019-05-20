#-----------------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Changelog: Miguel Rovira-Gonzalez, Created Script, May 11th, 2019
# Title: Comprehensions Lab, Week 5 Homework
#------------------------------------------------------------------#
"""
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

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


def food_dict_display(food_dict):
    food_display = "{name} is from {city}, and he likes {cake} cake, {fruit} salad, and {pasta} pasta.".format(**food_dict)
    return food_display


def list_comprehension(start=None, stop=None):
    return dict(zip([number for number in range(start, stop + 1)], [hex(number) for number in range(start, stop + 1)]))


def dict_comprehension(start=None, stop=None):
    return {number: hex(number) for number in range(start, stop + 1)}


def food_pref_dict(food_dict):
    return {k: food_dict[k].lower().count("a") for k in food_dict}


def set_comprehension(start, stop, mod_number):
    return set([number for number in range(start, stop + 1) if number % mod_number == 0])


def main():
    print(food_dict_display(food_prefs), "\n")
    print(list_comprehension(0, 15), "\n")
    print(dict_comprehension(0, 15), "\n")
    print(food_pref_dict(food_prefs), "\n")
    print(set_comprehension(0, 20, 2))


if __name__ == '__main__':
    main()

