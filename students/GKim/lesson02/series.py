
def fibonacci(n):
    """ compute the nth Fibonacci number """
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b
    


def lucas(n):
    """ compute the nth Lucas number """
    a, b = 2, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(n-1):
            a, b = b, a + b
        return b


def sum_series(n, a=0, b=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    # if n == 0:
    #     return a
    # elif n == 1:
    #     return b 
    for _ in range(n):
        a, b = b, a + b
    return a

# ----------------------------------- #

if __name__ == "__main__":
    # run some tests
    # assert fibonacci(0) == 0
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

    assert sum_series(4,3,2) == 12
    assert sum_series(5,3,2) == 19
    assert sum_series(6,3,2) == 31
    assert sum_series(0,3,2) == 3
    assert sum_series(1,3,2) == 2

    print("tests passed")
