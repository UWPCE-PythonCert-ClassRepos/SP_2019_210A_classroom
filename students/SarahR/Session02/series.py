def fibonacci(n):
    """ (int) -> int

    Parameters:
    	n: n'th number of the Fibonacci sequence

    Compute the nth Fibonacci number

    """
    # first two terms
    n1 = 0
    n2 = 1
    nth = int
    count = 2

    # check validity of n
    if n < 0:
        print("Please enter a positive integer")
	# No calculations for the first 2 elements of the sequence
    elif n <2:
        if n == 0:
            return 0
        if n == 1:
            return 1
    else:
        #calculate the nth number
        while count <= n:
            nth = n1 + n2

            # update values
            n1 = n2
            n2 = nth
            count += 1

        return nth


def lucas(n):
	""" (int) -> int

	Parameters:
		n: n'th number of the Lucas sequence

	Compute the nth Lucas number


    """
    n1 = 2
    n2 = 1
    nth = int
    count = 2

    if n < 0:
        print("Please enter a positive integer")
    elif n <2:

        if n == 0:
            return 2

        if n == 1:
            return 1

    else:
        while count <= n:
            nth = n1 + n2

            # update values
            n1 = n2
            n2 = nth
            count += 1

        return nth


def sum_series(n, seq0=0, seq1=1):
	""" (int, int, int) -> int

    Parameters:
        n: n'th number of the Lucas sequence
        seq0: seed used for the first number of the sequence
        seq1: seed used for the second number of the sequence

    compute the nth value of a summation series. Default to 0 and 1 for the seeds (fibonnaci sequence)

    """

	# variables
	n1 = seq0
	n2 = seq1
	nth = int
	count = 2

	if n < 0:
		print("Please enter a positive integer")
	elif n < 2:

		if n == 0:
			return seq0

		if n == 1:
			return seq1

	else:
		# calculate the nth number of the sequence
		while count <= n:
			nth = n1 + n2

			# update values
			n1 = n2
			n2 = nth
			count += 1

		return nth

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

    # test that sum_series matches fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
