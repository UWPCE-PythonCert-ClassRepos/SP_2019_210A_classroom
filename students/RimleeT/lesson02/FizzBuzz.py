"""
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""

def GetFizzBuzz(n):
	if (n%3==0 and n%5==0):
		return "FizzBuzz"
	elif n%5==0:
		return "Buzz"
	elif n%3==0:
		return "Fizz"
	else:
		return n

def FizzBuzz():
	for i in range(1,101):
		print(GetFizzBuzz(i))
	
FizzBuzz()

print("-------------------")
if __name__ == "__main__":
    # run some tests
    assert GetFizzBuzz(1) == 1
    assert GetFizzBuzz(30) == "FizzBuzz"
    assert GetFizzBuzz(15) == "FizzBuzz"
    assert GetFizzBuzz(3) == "Fizz"
    assert GetFizzBuzz(5) == "Buzz"
    assert GetFizzBuzz(4) == 4
    assert GetFizzBuzz(100) == "Buzz"
    print("tests passed")
print("------END--------")
	
    