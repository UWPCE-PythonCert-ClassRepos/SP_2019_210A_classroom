#FizzBuzz
#FredBallyns
#Session02


def fizzBuzz():
    """Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead."""
    index=1
    while index < 101:
        if index % 15 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print (index)
        index = index +1




if __name__ == "__main__":
    # run a test
    fizzBuzz()
