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
              "pasta": "lasagna",
              }

def print_dict(kwargs):
    printed = print("\n{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta\n".format(**kwargs))
    return printed

def list_comp(start = None, stop = None):
    lst_comp = dict([(x, hex(x)) for x in range(start, stop +1)])
    # lst_comp = dict(((x, hex(x)) for x in range(start, stop +1))) # use generator expression to iterate with out having to create another list to throw away
    # lst_comp = dict(zip([x for x in range(start, stop +1)], [hex(x) for x in range(start, stop +1)]))
    return lst_comp


def dict_comp(start = None, stop = None):
    return {k: hex(k) for k in range(start, stop + 1)}

def count_a(kwargs):
    # new_dict = {}
    new_dict = {k:  kwargs[k].lower().count("a") for k in kwargs}
    return new_dict

def set_gen(start = None, stop = None, quant = None):
    # return set(range(start, stop + 1, steps))
  # return [set(range(start, stop + 1, x + 1)) for x in range(quant)]
  return [set(x for x in range(start, stop + 1) if x % quant == 0)]




def main():
    print_dict(food_prefs)

    lst_comp_answer = list_comp(1, 15)
    print(lst_comp_answer)

    dict_comp_answer = dict_comp(1, 15)
    print(dict_comp_answer)

    a_dct = count_a(food_prefs)
    print(a_dct) 

    set_num = set_gen(0, 20, 4) 

    # print(set2)
    # print(set3)
    print(set_num)

if __name__ == "__main__": main()
    