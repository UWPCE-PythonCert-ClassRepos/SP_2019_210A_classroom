'''''Goal: The Fibonacci Series is a numeric series starting with the integers 0 and 1.

In this series, the next integer is determined by summing the previous two'''


def fibonacci(n):
    if n < 2:
        return n

    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
    return a

print(fibonacci(4))


def lucas(n):

    a,b = 2,1
    for _ in range (n):
        a,b = b, a+b
    return a

print(lucas(0))

#2, 1, 3, 4, 7, 11, 18, 29, ...

#0, 1, 1, 2, 3, 5, 8, 13, ...

