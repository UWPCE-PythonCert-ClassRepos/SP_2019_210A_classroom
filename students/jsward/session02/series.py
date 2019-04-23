

def fibonacci(nums_to_compute):
    # First solution
    """
    Print the Fibronacci number series.
    :param nums_to_compute:
    :return: none
    """
    results = [0, 1]
    while len(results) <= nums_to_compute:
        results.append(sum(results[-2:]))
    return results[nums_to_compute]


def fib(n):
    # Solution from class
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def lucas(n):
    """
    Print the Lucas number series
    :param n: number from the Lucas seies to return:
    :return: nth number from the Lucas series
    """
    results = [2, 1]
    while len(results) <= n:
        results.append(sum(results[-2:]))
    return results[n]


def sum_series(nth, n1=0, n2=1):
    """
    Return the nth number in the series defined by n1 and n2
    :param nth: number to return from within the series
    :param n1: 1st number from which to start the series
    :param n2: 2nd number from which to start the series
    :return: nth number from the series
    """
    results = [n1, n2]
    while len(results) <= nth:
        results.append(sum(results[-2:]))
    return results[nth]


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

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19
