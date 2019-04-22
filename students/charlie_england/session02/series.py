
def fib(n):
    """
    compute nth fibonnaci number
    """
    a, b = 0,1
    if n == 0:
        return a
    for _ in range(n-1):
        a,b = b, a+b
    return b

def lucas(n):
    """
    compute the nth Lucas number
    """
    a, b = 2,1
    if n == 0:
        return a
    for _ in range(n-1):
        a,b = b, a+b
    return b


def sum_series(n,a=0,b=1):
    """
    return the nth in a series where the next number is the sum of the last 2 (Fibonnaci or Lucas are 2 series types)
    default is the Fibonnaci series but a and b are optional starting parameters which can change the series types
    """
    if n == 0:
        return a
    for _ in range(n-1):
        a,b = b, a+b
    return b

#-----------------------TESTS------------------------#

#testing to make sure that the first 7 degrees of the Fibonnaci series return the correct number
assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13

#testing to make sure that the first 7 degrees of the Lucas series return the correct number
assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(2) == 3
assert lucas(3) == 4
assert lucas(4) == 7
assert lucas(5) == 11
assert lucas(6) == 18
assert lucas(7) == 29

#tests the default sum_series to 7 degrees (default is the fibonnaci series)
assert sum_series(0) == 0
assert sum_series(1) == 1
assert sum_series(2) == 1
assert sum_series(3) == 2
assert sum_series(4) == 3
assert sum_series(5) == 5
assert sum_series(6) == 8
assert sum_series(7) == 13

#tests the  sum_series to 7 degrees given a starting parameter of 2 and 1 (default is the fibonnaci series and this changes
# to the lucas series given the starting parameters of 2 and 1)
assert sum_series(0,2,1) == 2
assert sum_series(1,2,1) == 1
assert sum_series(2,2,1) == 3
assert sum_series(3,2,1) == 4
assert sum_series(4,2,1) == 7
assert sum_series(5,2,1) == 11
assert sum_series(6,2,1) == 18
assert sum_series(7,2,1) == 29