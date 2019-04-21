def fib(n):
    """Return nth fibonacci number with recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib (n - 2)

def fib2(n):
    """Another function that returns nth fibonacci number with lower time and space used."""
    a, b = 0, 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def lucas(n):
    """Return nth lucas number with low time and space complexity: O(n) time complexity and O(1) space complexity."""
    a, b = 2, 1
    if n == 0:
        return 2
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def sum_series(n, n0 = 0, n1 = 1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """
    if n0 == 0 and n1 == 1:
        return fib2(n)
    elif n0 == 2 and n1 == 1:
        return lucas(n)
    else:
        a, b = n0, n1
        if n == 0:
            return n0
        for _ in range(n - 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    """Test the correctness of above functions"""
    assert fib(0) == 0
    assert fib2(0) == 0
    assert fib(1) == 1
    assert fib2(1) == 1
    assert fib(2) == 1
    assert fib2(2) == 1
    assert fib(3) == 2
    assert fib2(3) == 2
    assert fib(4) == 3
    assert fib2(4) == 3
    assert fib(5) == 5
    assert fib2(5) == 5
    assert fib2(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7

    assert sum_series(100, 2, 1) == lucas(100)
    assert sum_series(100) == fib2(100)
    assert sum_series(5, 3, 2) == 19
    assert sum_series(4, 3, 2) == 12
    assert sum_series(3, 3, 2) == 7
    assert sum_series(2, 3, 2) == 5
    assert sum_series(0, 3, 2) == 3
    # 3, 2, 5, 7, 12, 19
    assert sum_series(5, 8, 17) == 109
    assert sum_series(0, 8, 17) == 8
    # 8, 17, 25, 42, 67, 109
    print('Tests Passed!')
