def fib(n):
    """Computes through the a series of numbers by summing the previous two numbers, see Fibonacci Number on wikipedia"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Only printing to see the output. The tests should prove it's accuracy
print(fib(10))


def lucas(n):
    """The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1, see Lucas Number on wikipedia"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

print(lucas(10))

def sum_series(n, t=0, r=1):
    if n == 0:
        return t
    elif n == 1:
        return r
    else:
        return sum_series(n-2) + sum_series(n-1)

print(sum_series(10, 2, 1))