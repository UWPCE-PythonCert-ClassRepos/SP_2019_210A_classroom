#Series
#FredBallyns
#Session02


def fibonacci(n):
    """ compute the nth Fibonacci number """
    #Use Recursive script
    #Counts zero as the zeroth number
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)



def lucas(n):
    """ compute the nth Lucas number """
    #Use growing list
    # set first two values
    nums=[]
    nums.append(2)
    nums.append(1)
    index = 2
    while index <= n:
        nums.append(nums[index-1]+nums[index-2])
        index = index +1
    return nums[n]





def sum_series(n, a=0, b=1):
    """
    compute the nth value of a summation series.

    :param a=0: value of zeroth element in the series
    :param b=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies"""
    
    if n == 0:
        return a
    elif n ==1:
        return b
    else:
        for _ in range(n-1):
            a, b = b, a + b
        return b






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

    print("tests passed")