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
    this implementation handles lucas and fibonacci series only

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

def generalized_series(n, first, second):
    """
    A more generalized algorithm that handles any progressive series
    of the general pattern Fn = Fn-1 + Fn - 2 for n where n >= 0 and
    F0 = x and F1 = y
    """

    # sanitize input to ensure its an integer
    n = int(n)

    if n < 0:
        return 0
    elif n == 0:
        return first
    elif n == 1:
        return second
    elif n > 1:
        return generalized_series(n - 1, second, first + second)

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
    """
    since `first` and`second` are optional and default to the fibonacci
    initialization values implicitly, we can pass a single parameter
    (the number to calculate a result for) and get the fibonacci behavior.

    we can also explicitly call the sum_series function with the same
    fibonacci initialization values and get the same result. tests below
    show this behavior.

    in order to get the lucas alrogithmic behaviour we must pass the
    full initialization value set to the function.

    this implementation handles lucas and fibonacci series

    """

    # implicit fibonacci
    print('Sum Series with implicit Fibonacci initializtion')
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
    print("Testing Complete and Passed. No Failed Assertions")
    print()

    # explicit fibonacci
    print('Sum Series with explicit Fibonacci initialization')
    assert sum_series(0, 0, 1)   == fibonacci(0)
    assert sum_series(1, 0, 1)   == fibonacci(1)
    assert sum_series(2, 0, 1)   == fibonacci(2)
    assert sum_series(3, 0, 1)   == fibonacci(3)
    assert sum_series(4, 0, 1)   == fibonacci(4)
    assert sum_series(5, 0, 1)   == fibonacci(5)
    assert sum_series(6, 0, 1)   == fibonacci(6)
    assert sum_series(10, 0, 1)  == fibonacci(10)
    assert sum_series(-1, 0, 1)  == fibonacci(-1)
    assert sum_series(5.5, 0, 1) == fibonacci(5.5)
    print("Testing Complete and Passed. No Failed Assertions")
    print()

    # explicit lucas - no implicit available
    print('Sum Series with explicit Lucas initialization')
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
    print()

    # more generilzed solution
    print('Generalized Series tests')
    assert generalized_series(0, 2, 4)      == 2
    assert generalized_series(1, 2, 4)      == 4
    assert generalized_series(5, 2, 4)      == 26
    assert generalized_series(2, 3, 4)      == 7
    assert generalized_series(3, 20, 10)    == 40
    assert generalized_series(-1, 20, 10)   == 0
    assert generalized_series(5.5, 2, 4)    == 26
    assert generalized_series(-1, 0, 1)     == fibonacci(-1)
    assert generalized_series(0, 0, 1)      == fibonacci(0)
    assert generalized_series(1, 0, 1)      == fibonacci(1)
    assert generalized_series(10, 0, 1)     == fibonacci(10)
    assert generalized_series(5.5, 0, 1)    == fibonacci(5.5)
    assert generalized_series(0, 2, 1)      == lucas(0)
    assert generalized_series(1, 2, 1)      == lucas(1)
    assert generalized_series(10, 2, 1)     == lucas(10)
    assert generalized_series(5.5, 2, 1)    == lucas(5.5)
    print("Testing Complete and Passed. No Failed Assertions")
    print()

    # this takes minutes to complete - ick!
    #print(fibonacci(40))

    def fast_fib(n):
        """ a fast non-recursive fibonacci calculator"""
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b

        return b

    print(fast_fib(40))
    print(fast_fib(1000))
