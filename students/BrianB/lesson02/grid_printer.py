#!/usr/bin/env python3

#--------------------------------------------------
# Who: Brian Brumleve
# What: Lesson02 - Grid Printer
# When: April 21, 2019
# Program Description:
#   This program uses a input parameters to print
#   out two grids.  One grid, my_grid1() prints a
#   grid that grows/shrinks based on a single
#   input parameter.  The second grid, my_grid2()
#   prints a grid that grows/shrinks in the # of
#   columns and rows as well grows/shrinks the
#   width of those columns and rows based on
#   two input parameters.
#--------------------------------------------------


# The row() function creates
# the tops and bottoms of the
# grids as the for-loop determines
# how wide each space between
# pluses "+" will be, as shown
# by the dash " - " lines.
def row(b, a=2):
    # The 1st part of this function,
    # normalizes the input, b, by
    # establishing the range is an
    # integer and ensuring integration
    # with the col() function to
    # ultimately print the correct
    # width rows: plus signs and dashes
    # and the correct width columns:
    # vertical lines and spaces.
    if b % 2 == 0:
        x = int(b) / 2
    elif b % 2 == 1:
        x = int(b - 1) / 2
    # The 2nd part of this function,
    # a for-loop prints a horizontal
    # row starting and stopping with a
    # "+" sign and iterating horizontally
    # as many dashes "-" as determined by x.
    for _ in range(a):
        # establishes the first print-out
        # of a row is the "+' sign
        print("+", end="")
        # prints as many dashes " - " as
        # multiplied by x
        print(" - "*int(x), end="")
    # ensures the last print-out
    # of a row is the "+' sign
    print("+")


# The col() function creates a row
# across starting and stopping
# with "|" and iterating as many
# spaces " " as is input.  The row
# across created by the col() function
# establishes the columns (or walls)
# of the grid
def col(b, a=2):
    # The 1st part of this function,
    # normalizes the value establishing
    # the range is an integer and
    # ensures integration with the
    # row() function to ultimately
    # print the correct width rows:
    # plus signs and dashes and the
    # correct width columns: vertical
    # lines and spaces.
    if b % 2 == 0:
        y = int(b) / 2
    elif b % 2 == 1:
        y = int(b-1) / 2
    # The 2nd part of this function,
    # this for-loop prints a horizontal a
    # row starting and stopping with a
    # "|" sign and iterating horizontally
    # as many empty 3-space blocks "   "
    # as is determined by y.
    for _ in range(a):
        # establishes the first print-out
        # of a column is the "|' symbol
        print("|", end="")
        # prints as many blank spaces " - "
        # as multiplied by y
        print("   "*int(y), end="")
    # ensures the last print-out
    # of a column is the "|' symbol
    print("|")


# my_grid1() function creates a 2x2 grid
# and grows and shrinks the width of the
# rows/columns with the input parameter, b.
def my_grid1(b, a=2):
    # The 1st part of this function,
    # normalizes the input allowing
    # my_grid1(b) with b=3 to result
    # in a grid that has 1 dash
    # between plus signs illustrating
    # a column with one dash.  This is
    # accomplished by halving the
    # input value b.
    if b % 2 == 0:
        x = int(b) / 2
    # This elif statement normalizes
    # odd numbers and floating point
    # numbers, if input.
    elif b % 2 == 1:
        x = int(b - 1) / 2
    # Print the top row, row().
    row(b, a)
    # Determines the number of
    # columns.
    for _ in range(a):
        # Determines the column width.
        for _ in range(int(x)):
            col(b, a)
        # Ensures the bottom row
        # is always a row().
        row(b, a)


# The my_grid2() function creates a
# grid by establishing the number of
# rows/columns with one input parameter,
# a, and the width of each row/column
# with the 2nd input parameter, b.
def my_grid2(a, b):
    # This 1st part of the function,
    # normalizes the value b to an
    # even integer and is able to
    # handle floating point numbers.
    # b*=2 converts all odd values
    # of b to even.
    b *= 2
    if b % 2 == 0:
        x = int(b) / 2
    # This normalizes floating
    # point numbers, if input.
    elif b % 2 == 1:
        x = int(b - 1) / 2
    # Print the top row, row().
    row(b, a)
    for _ in range(a):
        # Determines the number of
        # columns.
        for _ in range(int(x)):
            # Determines the column width.
            col(b, a)
        # Ensures the bottom row
        # is always a row().
        row(b, a)


# These commands call each function
# as defined by the parameters input
my_grid1(3)
my_grid2(3, 4)
