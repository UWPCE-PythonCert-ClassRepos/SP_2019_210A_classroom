#!/usr/bin/env python3

# --------------------------------------------------------------
# Task One
#    Write a format string that will take the
#       following four element tuple:
#
#        ( 2, 123.4567, 10000, 12345.67)
#
#        and produce:
#
#        'file_002 :   123.46, 1.00e+04, 1.23e+04'
#
# Let’s look at each of the four tuple elements in turn:
# 1) The first element is used to generate a filename that
#       can help with file sorting. The idea behind the
#       “file_002” is that if you have a bunch of files
#       that you want to name with numbers that can be sorted,
#       you need to “pad” the numbers with zeros to get
#       the right sort order.
# 2) The second element is a floating point number.  You
#       should display it with 2 decimal places shown.
# 3) The third value is an integer, but could be any
#       number.  You should display it in scientific notation,
#       with 2 decimal places shown.
# 4) The fourth value is a float with a lot of digits
#       – display it in scientific notation with
#       3 significant figures.
# --------------------------------------------------------------

# print("Task One:")
# n1 = (2, 123.4567, 10000, 12345.67)
# print("file_00%d:  %.2f, %.2e, %.3e" % n1)


# --------------------------------------------------------------
# Task Two
#   Using your results from Task One, repeat the
#   exercise, but this time using an alternate type
#   of format string (hint: think about alternative
#   ways to use .format() (keywords anyone?), and also
#   consider f-strings if you’ve not used them already).
# ---------------------------------------------------------------

# print("\nTask Two:")
# print("file_00{:d}:  {:.2f}, {:.2e}, {:.3e}"\
#      .format(2, 123.4567, 10000, 12345.67))


# --------------------------------------------------------------
# Task Three
#   Using your results from Task One, repeat the
#   exercise, but this time using an alternate type
#   of format string (hint: think about alternative
#   ways to use .format() (keywords anyone?), and also
#   consider f-strings if you’ve not used them already).
# ---------------------------------------------------------------

print("Task Three:")

'''
In [20]: formatter((2,3,5))
Out[20]: 'the 3 numbers are: 2, 3, 5'

In [21]: formatter((2,3,5,7,9))
Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'
'''
# Task Three_2:
# def formatter(x, y, z):
#     tup =  "the 3 numbers are: {:d}, {:d}, {:d}".format(x, y, z)
#     return tup
#
#
# print((formatter(3, 2, 5)))


# Task Three_3
def formatter(tup):
    tup = str(tup)
    counter = 0
    for i in tup:
        counter += 1
    tup = "the " + str(counter) + " numbers are: {:d}, {:d}, {:d}".format(*str)
    return tup, counter
print(formatter(2, 3, 5))



