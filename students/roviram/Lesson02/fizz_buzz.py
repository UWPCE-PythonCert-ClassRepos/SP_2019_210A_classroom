#-----------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Desc: Fizz Buzz Homework, Week 2
# Date Created: Sunday 4/21
#-----------------------------------------------------------#
"""
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
"""

# Range function creates a sequence of numbers with the first number being inclusive and the last number is not inclusive
for number in range(1, 101):
    # If the number in the range 1-100 is divisible by 3 with no remainders after the division, e.g. 27 / 3 = 9 (27 divided by 3, 9 times will result in 0 remainder)
    # Order of Operations with if logic matters, so testing for multiples of 3 and 5 needs to go first for numbers like 15 otherwise it won't get evaluated since it will be automatically True
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

