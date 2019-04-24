def fib(n):
    '''compute the nth fibonacci number'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return n + fib(n-1)


print(fib(int(input())))
