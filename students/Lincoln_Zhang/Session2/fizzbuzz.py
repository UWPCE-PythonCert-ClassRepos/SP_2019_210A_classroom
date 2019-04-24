#!#!/usr/bin/env python3
# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.


def return_Fizz(n):
    if (not n % 3):
        return "Fizz"
    return ""


def return_Buzz(n):
    if (not n % 5):
        return "Buzz"
    return ""


def return_FizzBuzz(n):
    if not n % 15:
        return "FizzBuzz"
    # else:
    #     return n


def Fizz_Buzz_filter(n):
    #l = [return_Fizz(n), return_Buzz(n), return_FizzBuzz(n)]
    #result = ""
    result = return_Fizz(n) + return_Buzz(n)
    if not result:
        result = str(n)
    return result


    # if "Fizz" in l:
    #     return "Fizz"
    # elif "Buzz" in l:
    #     return "Buzz"
    # elif "FizzBuzz" in l:
    #     return "FizzBuzz"
    # else:
    #     return n


def printer(m):
    for n in range (1,m+1):
        a = Fizz_Buzz_filter(n)
        print (a)

assert return_Fizz(45) == "Fizz"
assert return_Fizz(9) == "Fizz"
assert return_Buzz(15) == "Buzz"
assert return_Buzz(10) == "Buzz"
# assert return_FizzBuzz(10) == None
# assert return_FizzBuzz(21) == 21
# assert return_FizzBuzz(30) == "FizzBuzz"

printer(100)