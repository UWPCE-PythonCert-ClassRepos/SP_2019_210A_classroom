#! /usr/bin/env python3
"""
Lesson 02 : FizzBuzz
Author : Joe Nunnelley
"""
def fizzbuzz(start=1, stop=100):
    """
    A function detecting specific modulus conditions
    and printing some fun text
    """
    for _ in range(start, stop):
        fizz = (_ % 3 == 0)
        buzz = (_ % 5 == 0)

        if fizz and buzz:
            print('FizzBuzz ({})'.format(_))
        elif fizz and not buzz:
            print('Fizz ({})'.format(_))
        elif not fizz and buzz:
            print('Buzz ({})'.format(_))
        else:
            print('{}'.format(_))


fizzbuzz()