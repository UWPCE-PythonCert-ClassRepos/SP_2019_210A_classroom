def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib (n - 2)

def fib2(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
