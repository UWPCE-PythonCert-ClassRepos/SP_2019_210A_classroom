#!/usr/bin/env python3

#--------------------------------------------------
# Who: Brian Brumleve
# What: Lesson02 - Fizz Buzz
# When: April 17, 2019
# Program Description:
#   Prints a list 0 to 100. For multiples of 3,
#   Fizz is printed, for multiples of 5, Buzz is
#   printed and for multiples of 3 adn 5,
#   "FizzBuzz" is printed.
#--------------------------------------------------

# Global variables set the
# range to be looped through
n = 100
i = 0

while i < n:
    i = i + 1
    #  The first IF statement you come across determines
    #  if 3 AND 5 are both divisible by the specific
    #  number the loop is processing. If this statement
    #  weren't first then the program would assign priority
    #  to numbers divisible by 3 OR 5, individually.  The
    #  program (which checks 3 OR 5 before checking 3 AND 5)
    #  will never get find a number that fits both 3 AND 5.
    #  The script passes the first and second tests, being
    #  divisible by 3, then 5 and stops.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        # if a value isn't divisible by 3 or 5
        # then its value ends up being printed
        # by this print statement
        print(i)
