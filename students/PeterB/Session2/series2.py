# fibonacci

a, b = 0,1
while b < 56:
    print(b)
    a, b = b, a+b

# lucas

a, b = 2,1
while b < 56:
    print(b)
    a, b = b, a+b

# sum_series
# one required user , two optional parameters

# n, b, c = ,0,1
# while n < 56:
#     print(n)


def sum_series(n, b=0, c=1):
    if n < 0:
        return None
    elif n == 0:
        return b
    elif n == 1:
        return c
    else:
        return sum_series(n - 1, b, c) + sum_series(n - 2, b, c)
