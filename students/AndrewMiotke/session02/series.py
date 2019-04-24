#!/usr/bin/env python3

def fibonacci(n):
    """Computes through the a series of numbers by summing the previous two numbers, see Fibonacci Number on wikipedia"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# Only printing to see the output. The tests should prove it's accuracy
print(fibonacci(7))

def lucas(n):
    """The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1, see Lucas Number on wikipedia"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

print(lucas(4))

def sum_series(n, t=0, r=1):
    """
    sum_series() will compute both the Fibonacci series and the lucas series based on the parameters passed into the function call
    To run the Fibonacci series, just pass in the value into the sum_series() call,
    To run the Lucas series, pass in the value followed by a 2 and 1.
    """
    if n == 0:
        return t
    elif n == 1:
        return r
    else:
        return sum_series(n-2) + sum_series(n-1)

print(sum_series(4, 2, 1))

if __name__ == "__main__":
    # test fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # test lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    # test if sum_series is equal to fibonacci
    assert sum_series(5) == fibonacci(5)

    # test if sum_series is equal to lucas
    # assert sum_series(5) == lucas(5)

    print("✅ All tests passed")