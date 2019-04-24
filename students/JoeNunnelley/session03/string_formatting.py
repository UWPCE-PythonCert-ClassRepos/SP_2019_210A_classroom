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
    so you can dynamically build up the format string to accommodate
    the length of the tuple.
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
    Given the following four element list:

    ['oranges', 1.3, 'lemons', 1.1]

    Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1

        Now see if you can change the f-string so that it displays
        the names of the fruit in upper case, and the weight 20% higher
        (that is 1.2 times higher).
    """
    a_row = ['oranges', 1.3, 'lemons', 1.1]
    print(f'The weight of an {a_row[0][0:-1]} is {a_row[1]} and the weight '
          f'of a {a_row[2][0:-1]} is {a_row[3]}')
    print(f'The weight of an {a_row[0][0:-1].upper()} is {a_row[1] * 1.2} '
          f'and the weight of a {a_row[2][0:-1].upper()} is {a_row[3] * 1.2}')


def task6():
    """
    Write some Python code to print a table of several rows,
    each with a name, an age and a cost. Make sure some of the
    costs are in the hundreds and thousands to test your alignment
    specifiers.

    And for an extra task, given a tuple with 10 consecutive
    numbers, can you work how to quickly print the tuple in
    columns that are 5 charaters wide? It can be done on one
    short line!
    """
    rows = [
        ['First', '$9999.08', 'Second', '$10000.01'],
        ['First', '$19999.08', 'Second', '$11000.01'],
        ['First', '$999.08', 'Second', '$1000.01'],
        ['First', '$99.08', 'Second', '$100.01'],
    ]

    for row in rows:
        print(f'{row[0]:10}{row[1]:>15}\t{row[2]:10}{row[3]:>15}')

    tuple_ten = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    tuple_len = len(tuple_ten)
    format_str = "{:=5}" * tuple_len
    print(format_str.format(*tuple_ten))
    print()


if __name__ == "__main__":
    A_TUPLE1 = (2, 123.4567, 10000, 12345.67)
    print("Begin Testing")
    assert task1(A_TUPLE1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task2(A_TUPLE1) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    assert task3((0, 1, 2, 3, 4)) == 'the 5 numbers are 0, 1, 2, 3, 4'
    assert task4((4, 30, 2017, 2, 27)) == '02 27 2017 04 30'
    task5()
    task6()
    print("All tests passed")
