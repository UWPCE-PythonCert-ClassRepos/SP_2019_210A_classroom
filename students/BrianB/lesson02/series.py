#!/usr/bin/env python3

#--------------------------------------------------
# Who: Brian Brumleve
# What: Lesson02 - Series
# When: April 17, 2019
# Program Description:
#   This program uses a common script to develop
#   a listing of Fibonacci Series numbers and
#   Lucas Numbers.  The program is also capable
#   of creating a unique series of numbers.
#--------------------------------------------------


# Fibonacci Series
#   This function assigns optional parameters (OP)
#   specific to the Fibonacci Series.  These
#   optional parameters represent the first two
#   values of F(0) and F(1).  The math for
#   developing the Fibonacci Series is performed
#   in the sum_series() function, which is called
#   to by the fibonacci() function.
def fibonacci(n, a=0, b=1):
    return sum_series(n, a, b)


# Lucas Numbers
#   This function assigns optional parameters (OP)
#   specific to the Lucas Number series.  These
#   optional parameters represent the first two
#   values of L(0) and L(1).  The math for develop-
#   ing the Lucas Numbers is performed in the
#   sum_series() function, which is called to by
#   the fibonacci() function.
def lucas(n, a=2, b=1):
    return sum_series(n, a, b)


# Sum_Series: Fibonacci Series, Lucas Numbers
#    & Other Series
#   This function assigns optional parameters (OP)
#   specific to the Fibonacci Series by default.
#   If the optional parameters are overwritten by
#   with new inputs, the sum_series will create an
#   entirely new series unless the input parameters
#   happen to match those of the Lucas Numbers.  Then
#   the Lucas Numbers will be created.
def sum_series(n, a=0, b=1):
    a, b = a, b
    if n == 0:
        # returns 1st OP; ensures
        # correct series is maintained
        return a
    # loops through a range of numbers
    for _ in range(n - 1):
        # assigns and re-assigns
        # new values based on the
        # location within the range
        a, b = b, a + b
    # returns the final value
    # for series based on the
    # iterative number
    return b


# Testing the 3 series codes with
# assertions
def series_tests(__init__):
    if __init__ == "__main__":
        # Fibonacci Series Number Assertion tests
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13
        assert fibonacci(8) == 21
        assert fibonacci(9) == 34
        assert fibonacci(10) == 55

        # Lucas Number Assertion tests
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(2) == 3
        assert lucas(3) == 4
        assert lucas(4) == 7
        assert lucas(5) == 11
        assert lucas(6) == 18
        assert lucas(7) == 29

        # Sum_Series Assertion tests
        # Optional Parameters omitted...
        # defaulting to a Fibonacci Series
        assert sum_series(0) == 0
        assert sum_series(5) == 5
        assert sum_series(9) == 34
        # A Fibonacci Series Number
        assert sum_series(3, 0, 1) == 2
        assert sum_series(4, 0, 1) == 3
        assert sum_series(6, 0, 1) == 8
        assert sum_series(1, 2, 1) == 1
        # A Lucas Number
        assert sum_series(2, 2, 1) == 3
        assert sum_series(4, 2, 1) == 7
        # A series all its own
        assert sum_series(8, 3, 3) == 102
        assert sum_series(9, 3, 3) == 169
        assert sum_series(10, 3, 3) == 267
        assert sum_series(11, 3, 3) == 432
        assert sum_series(12, 3, 3) == 699
        assert sum_series(13, 3, 3) == 1131
    return


print("All the tests work!")
