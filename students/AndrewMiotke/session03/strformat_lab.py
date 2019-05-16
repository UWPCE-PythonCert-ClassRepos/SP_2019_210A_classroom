#!/usr/bin/env python3
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
# This is missing some tasks since I didn't notice these exercises existed until I was halfway through with the mailroom excersize.

def task_one():
    one_string = "file_{:>03} {:>G} {} {}"
    print(one_string.format(2, 123.4567, 10000, 12345.67))


def task_three():
    t = (1, 2, 3, 4, 5)
    three_string = "the 3 numbers are: {:d}, {:d}, {:d}, {:d}"
    print(three_string.format(*t))


def task_four():

    r = ( 4, 30, 2017, 2, 27)
    return sorted(r)


def formatter(in_tuple):
    form_string = "{:d}, {:d}"
    return form_string.format(*in_tuple)

print(formatter((1, 2)))


# I know this can be done better and not every value set to it's own variable :(
def task_five():
    orange = "orange"
    orange_weight = 1.3
    lemon = "lemon"
    lemon_weight = 1.1
    print(f"The weight of an {orange} is {orange_weight} and the weight of a {lemon} is {lemon_weight}")
    print(f"The weight of an {orange.upper()} is {orange_weight * 1.2} and the weight of a {lemon.upper()} is {lemon_weight * 1.2}")


if __name__ == "__main__":
    task_one()
    task_three()
    task_four()
    task_five()