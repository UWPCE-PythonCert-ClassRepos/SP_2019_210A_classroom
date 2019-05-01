"""
This assignment
"""

def fib(n):
    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n-1):
        a,b = b, a + b
    return b

def luc(n):
    a, b = 2, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n-1):
        a,b = b, a + b
    return b

def numseries(n,a,b):
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n-1):
        a,b = b, a + b
    return b



assert fib(0) == numseries(0,0,1)
assert fib(1) == numseries(1,0,1)
assert fib(2) == numseries(2,0,1)
assert fib(3) == numseries(3,0,1)
assert fib(4) == numseries(4,0,1)
assert fib(44) == numseries(44,0,1)

assert luc(0) == numseries(0,2,1)
assert luc(1) == numseries(1,2,1)

assert numseries(0,3,4) == 3
assert numseries(1,3,4) == 4
assert numseries(2,3,4) == 7
assert numseries(3,3,4) == 11

assert luc(0) == 2
assert luc(1) == 1
assert luc(2) == 3
assert luc(3) == 4

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3