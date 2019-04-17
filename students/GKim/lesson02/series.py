# def fib(n):
#     """
#     compute the nth fibonacci number
#     """
#     # print("fib called with:", n)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     return fib(n-1) + fib(n-2)


# assert fib(0) == 0
# assert fib(1) == 1
# assert fib(2) == 1
# assert fib(3) == 2

# def fib(n):
#     nums = [0,1]
#     while len(nums) < n:
#         # new_num = nums[-1] + nums[-2]
#         nums.append(sum(nums[-2:]))
#     print(nums)
#     return nums[-1]

# print(fib(15))

def fib(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

print(fib(0))