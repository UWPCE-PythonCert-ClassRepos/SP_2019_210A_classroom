# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)