#! /usr/bin/env python3

"""
Lesson 2 : The Series Project
Author : Joe Nunnelley
"""
def fibonacci(n):
    """Return the nth fibonacci number"""

    # sanitize input by ensuring its an integer
    n = int(n)

    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n == 1:
        return 1
    elif n <= 0:
        return 0

def lucas(n):
    """Return nth lucas number"""

    # sanitize input by ensuring its an integer
    n = int(n)

    if n > 1:
        return lucas(n - 1) + lucas(n - 2)
    elif n == 1:
        return 1
    elif n <= 0:
        return 2

def sum_series(n, first=0, second=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """

    # sanitize input by ensuring its an integer
    n = int(n)

    if not first:
        """Return the fibonacci number for the value provided"""
        if n > 1:
            return fibonacci(n - 1) + fibonacci(n - 2)
        if n == 1:
            return second
        elif n <= 0:
            return first
    else:
        if n > 1:
            return lucas(n - 1) + lucas(n - 2)
        elif n == 1:
            return second
        elif n <= 0:
            return first

if __name__ == "__main__":
    print("Testing Fibonnaci Algorithm")
    assert fibonacci(0)     == 0
    assert fibonacci(1)     == 1
    assert fibonacci(2)     == 1
    assert fibonacci(3)     == 2
    assert fibonacci(4)     == 3
    assert fibonacci(5)     == 5
    assert fibonacci(6)     == 8
    assert fibonacci(10)    == 55
    assert fibonacci(-1)    == 0
    assert fibonacci(5.5)   == 5
    print("Testing Complete and Passed. No Failed Assertions")
    print()

    print("Testing Lucas Algorithm")
    assert lucas(0)     == 2
    assert lucas(1)     == 1
    assert lucas(2)     == 3
    assert lucas(3)     == 4
    assert lucas(4)     == 7
    assert lucas(5)     == 11
    assert lucas(6)     == 18
    assert lucas(10)    == 123
    assert lucas(-1)    == 2
    assert lucas(5.5)   == 11
    print("Testing Complete and Passed. No Failed Assertions")
    print()

    print("Testing Sum Series Algorithm")
    assert sum_series(0)         == fibonacci(0)
    assert sum_series(1)         == fibonacci(1)
    assert sum_series(2)         == fibonacci(2)
    assert sum_series(3)         == fibonacci(3)
    assert sum_series(4)         == fibonacci(4)
    assert sum_series(5)         == fibonacci(5)
    assert sum_series(6)         == fibonacci(6)
    assert sum_series(10)        == fibonacci(10)
    assert sum_series(-1)        == fibonacci(-1)
    assert sum_series(5.5)       == fibonacci(5.5)
    assert sum_series(0, 2, 1)   == lucas(0)
    assert sum_series(1, 2, 1)   == lucas(1)
    assert sum_series(2, 2, 1)   == lucas(2)
    assert sum_series(3, 2, 1)   == lucas(3)
    assert sum_series(4, 2, 1)   == lucas(4)
    assert sum_series(5, 2, 1)   == lucas(5)
    assert sum_series(6, 2, 1)   == lucas(6)
    assert sum_series(10, 2, 1)  == lucas(10)
    assert sum_series(-1, 2, 1)  == lucas(-1)
    assert sum_series(5.5, 2, 1) == lucas(5.5)
    print("Testing Complete and Passed. No Failed Assertions")