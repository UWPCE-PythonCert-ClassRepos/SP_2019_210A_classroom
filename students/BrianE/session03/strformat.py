#!/usr/env python3

"""
    strformat_lab.py
"""

# Task 1
"""
    Write a format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67) and produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""

file_tuple01 = (2, 123.4567, 10000, 12345.67)
converted_tuple = f"file_{file_tuple01[0]:0>3d}:\t{file_tuple01[1]:.2f}, {file_tuple01[2]:.2E}, {file_tuple01[3]:.3E}"
print(f"Task 1: \nOriginal file tuple:\t\t{file_tuple01}\nConverted file details: \t{converted_tuple}")


# Task 2
"""
    Using your results from Task One, repeat the exercise, but this time using an alternate type of format string 
"""

print("\nTask2:\nfile_00{:d}:  {:.2f}, {:.2e}, {:.3e}".format(*file_tuple01))


# Task 3
"""
    Rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" to take an arbitrary number of inputs
"""

print("\nTask 3")


def formatter(in_tuple):
    """
    Convert tuple to string
    :param in_tuple: input tuple
    :return: formatted string
    """

    fstring = ""
    for _ in range(0, len(in_tuple)):
        fstring += '{:d}, '
    return fstring.format(*in_tuple)[:-2]


print(formatter((1, 2, 3, 4)))

# Task 4
"""
    Given a 5 element tuple: ( 4, 30, 2017, 2, 27), use string formatting to print: '02 27 2017 04 30'
"""
print("\nTask 4:")
tuple_5 = (4, 30, 2017, 2, 27)
print(f"{tuple_5[3]:0>2d}, {tuple_5[4]:0>2d}, {tuple_5[2]}, {tuple_5[0]:0>2d}, {tuple_5[1]:0>2d}")

# Task 5
"""
    Given the following four element list: ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display: The weight of an orange is 1.3 and the weight of a lemon is 1.1
"""
print("\nTask5:")
fruit_list = ['oranges', 1.3, 'lemons', 1.1]
fruit_fstring = f"The weight of an {fruit_list[0][:-1]} is {fruit_list[1]} \
and the weight of a {fruit_list[2][:-1]} is {fruit_list[3]}"
fruit_fstring_increased = f"The weight of an {fruit_list[0][:-1].capitalize()} is {(fruit_list[1] * 1.2)} \
and the weight of a {fruit_list[2][:-1].capitalize()} is {(fruit_list[3] * 1.2)}"
print(fruit_fstring)
print(fruit_fstring_increased)

# Task 6
"""
    Print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the 
    hundreds and thousands to test your alignment specifiers.
"""

print("\nTask 6:")
items = [("Product 1", 10, 3.99),
         ("Product Two", 9, 25.99),
         ("Product 30000", 150, 6500.00),
         ("Product 4", 950, 249.99)]

for item in items:
    print("|Name: {0:15} | Age: {1:5} | Price: {2:10}|".format(*item))

"""
    Given a tuple with 10 consecutive numbers, 
    can you work how to quickly print the tuple in columns that are 5 characters wide?
"""

tuple_10 = range(10)
print()
print("{0:5} {1:5} {2:5} {3:5} {4:5} {5:5} {6:5} {7:5} {8:5} {9:5}".format(*tuple_10))

