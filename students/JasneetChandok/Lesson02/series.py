#!/usr/bin/env python3

"""
a template for the series assignment
"""


def fibonacci(n):
    """ compute the nth Fibonacci number """
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    pass


def lucas(n):
    """ compute the nth Lucas number """
    if(n == 0):
        return 2
    elif (n == 1):
        return n
    else:
        return(lucas(n-1) + lucas(n-2))
    pass


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n0 == False:
        if n > 1:
            return fibonacci(n - 1) + fibonacci(n - 2)
        if n == 1:
            return n1
        elif n <= 0:
            return n0
    else:
        if n > 1:
            return lucas(n - 1) + lucas(n - 2)
        elif n == 1:
            return n1
        elif n <= 0:
            return n0
    pass

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13


    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7


    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

print("Tests Passed")
