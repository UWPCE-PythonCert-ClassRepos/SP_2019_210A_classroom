#! /usr/bin/env python3

"""
String Formatting Exercises
Author: Joe Nunnelley
"""
def task1(a_tuple):
    """
    Write a format string that will take the following
    four element tuple:

        ( 2, 123.4567, 10000, 12345.67)

        and produce:

        'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """
    file_name = "file_{:03d} :".format(a_tuple[0])
    col1 = "   {:06.2f}".format(a_tuple[1])
    col2 = ", {:.2e}".format(a_tuple[2])
    col3 = ", {:.2e}".format(a_tuple[3])
    return file_name + col1 + col2 + col3


def task2(a_tuple):
    """
    Using your results from Task One, repeat the exercise,
    but this time using an alternate type of format string
    (hint: think about alternative ways to use .format()
    (keywords anyone?), and also consider f-strings if you’ve
    not used them already).
    """
    file_name = f'file_{a_tuple[0]:03d} :'
    col1 = f'   {a_tuple[1]:06.2f}'
    col2 = f', {a_tuple[2]:.2e}'
    col3 = f', {a_tuple[3]:.2e}'
    return file_name + col1 + col2 + col3


def task3(a_tuple):
    """
    Dynamically Building up format strings

        Rewrite:

    "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

    to take an arbitrary number of values.

    Hint: You can pass in a tuple of values to a function with a *:

    In [52]: t = (1,2,3)

    In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
    Out[53]: 'the 3 numbers are: 1, 2, 3'

    The idea here is that you may have a tuple of three numbers,
    but might also have 4 or 5 or 2 or….

    so you can dynamically build up the format string to accommodate
    the length of the tuple.

    The string object has the format() method, so you can call it
    with a string that is bound to a name, not just a string literal.
    For example:

    In [16]: form_string = "{:d}, {:d}"

    In [17]: nums = (34, 56)

    In [18]: fstring.format(*nums)
    Out[18]: '34, 56'

    So in the example above, how would you make a form_string that
    was the right length for an arbitrary tuple?

    Put your code in a function that will return the final string
    like so:

    In [20]: formatter((2,3,5))
    Out[20]: 'the 3 numbers are: 2, 3, 5'

    In [21]: formatter((2,3,5,7,9))
    Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'

    It will look like:

    def formatter(in_tuple):
        do_something_here_to_make_a_format_string

        return form_string.format(*in_tuple)
    """
    tuple_len = len(a_tuple)
    form_string = "the {} numbers are " + "{:d}, " * (tuple_len - 1) + "{:d}"
    return form_string.format(tuple_len, *a_tuple)


def task4(a_tuple):
    """
        Given a 5 element tuple:
            ( 4, 30, 2017, 2, 27)
            use string formating to print:
            '02 27 2017 04 30'
    """
    return f'{a_tuple[3]:02d} {a_tuple[4]} {a_tuple[2]} {a_tuple[0]:02d} {a_tuple[1]}'


def task5():
    """
    Task Five

    f-strings are new to Python (version 3.6), but are very powerful
    and efficient. This means they are worth understanding and using.
    And this is made easier than it might be because they use the same,
    familiar formatting language that is conventionally used in Python
    (in .format()).

    So in this exercise we are going to specifically use f-strings.

    Here’s the simplest example, to show how you can use available
    variables in a f-string:

    In [2]: name = 'Andy'
    In [3]: f'Your name is {name}'
    Out[3]: 'Your name is Andy'

    In addition to referencing variables in the local scope,
    f-strings can evaluate simple expressions in line like so:

    In [5]: f"Your name is {name.upper()}"
    Out[5]: 'Your name is ANDY'

    In [6]: name = "andy"

    In [7]: f"Your name is {name.upper()}"
    Out[7]: 'Your name is ANDY'

    or

    In [8]: a = 5

    In [9]: b = 10

    In [10]: f"The sum is: {a+b}"
    Out[10]: 'The sum is: 15'

        Here’s a task for you: Given the following four element list:

            ['oranges', 1.3, 'lemons', 1.1]

        Write an f-string that will display:

            The weight of an orange is 1.3 and the weight of a lemon is 1.1

        Now see if you can change the f-string so that it displays
        the names of the fruit in upper case, and the weight 20% higher
        (that is 1.2 times higher).
    """
    pass


def task6():
    """
    Task Six

    Often it’s convenient to display data in columns. String formatting
    helps to make this straightforward.

    Suppose you’d like to display something like:

        ‘First $99.01 Second $88.09 ‘

    One way to do that is:

    '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')

    In this simple example everything aligns nicely. But that will
    not be the case when the numbers to the left of the decimal place
    vary. Then you will need to use alignment specifiers. Do some
    research on this using the links below. Then:

        Write some Python code to print a table of several rows,
        each with a name, an age and a cost. Make sure some of the
        costs are in the hundreds and thousands to test your alignment
        specifiers.
        And for an extra task, given a tuple with 10 consecutive
        numbers, can you work how to quickly print the tuple in
        columns that are 5 charaters wide? It can be done on one
        short line!
    """
    pass

if __name__ == "__main__":
    A_TUPLE1 = (2, 123.4567, 10000, 12345.67)
    print("Begin Testing")
    print(task1(A_TUPLE1))
    print(task2(A_TUPLE1))
    print(task3((0, 1, 2, 3, 4)))
    assert task4((4, 30, 2017, 2, 27)) == '02 27 2017 04 30'
    task5()
    task6()
    print("All tests passed")
