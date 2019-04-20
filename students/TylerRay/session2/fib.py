#number = int(input("Number: "))

#def fib(number):
#    if number < 2:
#        return number
#    return fib(number-1) + fib(number-2)

#def fib(n):
#    nums = [0,1]
#    while len(nums) <= n:
#        nums.append(sum(nums[-2:]))
#        print(nums)
#    return nums[-1]

def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a,b = b, a + b
    return b

print(fib(1000))
