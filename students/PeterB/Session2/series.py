# fibonacci number = 0,1,1,3,5,8,13, 21

def fibonacci(n):
    a,b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

for i in range(0,10):
    print ((fibonacci(n))


def lucas(n):
    a, b = 2, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

    for i in range(0, 10):
        print((lucas(n))

#
# # sum_series
#
#def sum_series(n, b=0, c=1):
    if n < 0:
        return None
    elif n == 0:
        return b
    elif n == 1:
        return c
    else:
        return sum_series(n - 1, b, c) + sum_series(n - 2, b, c)
#
#
#
# # TESTING
#
#
# def fibonacci(n):
#     """ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 """
#     pass
#
#
# def lucas(n):
#     """ 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 """
#     pass
#
#
# def sum_series(n, b=0, c=1):
#     """
#     compute the nth value of a summation series.
#
#     :param b=0: value of zeroth element in the series
#     :param c=1: value of first element in the series
#
#     This function should generalize the fibonacci() and the lucas(),
#     so that this function works for any first two numbers for a sum series.
#     Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
#     And sum_series(n, 2, 1) should be equivalent to lucas(n).
#
#     sum_series(n, 3, 2) should generate antoehr series with no specific name
#
#     The defaults are set to 0, 1, so if you don't pass in any values, you'll
#     get the fibonacci sercies
#     """
#     pass
#
# if __name__ == "__main__":
#     # run some tests
#     assert fibonacci(0) == 0
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
#     assert fibonacci(4) == 3
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8
#     assert fibonacci(7) == 13
#
#     assert lucas(0) == 2
#     assert lucas(1) == 1
#
#     assert lucas(4) == 7
#
#     # test that sum_series matches fibonacci
#     assert sum_series(5) == fibonacci(5)
#     assert sum_series(7, 0, 1) == fibonacci(7)
#
#     # test if sum_series matched lucas
#     assert sum_series(5, 2, 1) == lucas(5)
#
#     # test if sum_series works for arbitrary initial values
#     assert sum_series(0, 3, 2) == 3
#     assert sum_series(1, 3, 2) == 2
#     assert sum_series(2, 3, 2) == 5
#     assert sum_series(3, 3, 2) == 7
#     assert sum_series(4, 3, 2) == 12
#     assert sum_series(5, 3, 2) == 19
#
#     print("tests passed")
#