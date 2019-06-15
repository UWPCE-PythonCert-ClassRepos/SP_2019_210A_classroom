""" Notes from class 10 """

# Function Programming
from operator import add, sub, mul, truediv, floordiv, mod

# Expect the same result everytime
print(add(5, 9))
print(sub(5, 2))
print(mul(10, 5))
print(truediv(20, 3))
print(floordiv(20, 3))

def f(x):
    return x ** 2


def g(y):
    return y / (10 ** 10)

x = 11
y = f(x)
print(y)
z = g(y)
print(z)

print(g(f(x)))

# Build in functions


# Lambda
# form a function in place without creating a function memeory
# annonymous function
from random import randint

x = [randint(0, 20) for _ in range(20)]
print(x)

sorted(x, key=lambda x: x)

# Map
print("Map")
map(lambda y: y * 2, x)
print([i for i in map(lambda y: y * 2, x)])


# Filter
# If it evaluates to True it does its operation,
# if false it does not
f = filter(lambda x: mod(x) == 2, range(100))
print("Filter")
print(f)


# Reduce
# Reudces down to a single value
from functools import reduce
r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r)


# Generators
print("Generators?")
r = range(100)
print([i for i in r]) # list comprehension

def demo_generator(n):
    for i in range(n):
        yield i