"""
series.py

Calculate summation value of a given number
"""


def fibonacci(n):
    """
    Compute the nth Fibonacci value using recursion.

    :param n: value of desired index
    :return: value of fibonacci calculation of nth index
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Compute the nth Lucas value using recursion.

    :param n: value of desired index
    :return: value of lucas calculation of nth index
    """

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """
    Compute the nth value in a summation series using recursion.

    :param n: value of desired index
    :param n0: value of zeroth element in the series
    :param n1: value of first element in the series
    :return: value of summation calculation of nth index similar to Fibonacci
    """

    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)


if __name__ == '__main__':
    # test fibonacci series
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765
    assert fibonacci(25) == 75025

    # test lucas series
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # test if sum_series matched fibonacci
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test sum_series with custom initial values
    assert sum_series(5, 5, 7) == 50
    assert sum_series(5, 5, 9) == 60
    assert sum_series(7, 5, 9) == 157
    assert sum_series(9, 3, 9) == 369

    print("All assertions pass")

