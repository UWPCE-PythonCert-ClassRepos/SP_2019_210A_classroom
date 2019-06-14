#Computing the Fibonacci and Lucas Series

def fibonacci(n):
	if n<2:
		return n
	return (fibonacci(n-2)+fibonacci(n-1))


def lucas(n):
	if n==0:
		return 2
	elif n==1:
		return 1
	else:
		return (lucas(n-2)+lucas(n-1))

"""
sum_series: 
It should have one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
Calling this function with no optional parameters will produce numbers from the fibonacci series (because 0 and 1 are the defaults).
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
"""
def sum_series(n, n0=0, n1=1):
	if n == 0:
		return n0
	elif n == 1:
		return n1
	else:
		return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)

print(fibonacci(5))
print(sum_series(5))
print(sum_series(5,2,1))

if __name__ == "__main__":
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")	
	