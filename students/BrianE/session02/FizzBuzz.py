"""
FizzBuzz.py

Return Fizz, Buzz or FizzBuzz if number is divisible by 3, 5 or both.
"""


def fizz_buzz(n):
    """
    Return Fizz, Buzz or FizzBuzz if number is divisible by 3, 5 or both.

    :param n: input value
    :return: Fizz, Buzz or FizzBuzz
    """

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == '__main__':
    for number in range(1, 101):
        print(fizz_buzz(number))

