

# def fib(n):
#     """
#     compute the nth Fibonacci number
#     """
#     #print("fib called with:", n)
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


# def fib(n):
#     nums = [0, 1]
#     while len(nums) < n:
#         nums.append(sum(nums[-2:]))
#         print(nums)
#     return nums[-1]

def fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a = b
        b = a + b
#        a, b = b, a + b
    return b


# assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13

print(fib(6))
