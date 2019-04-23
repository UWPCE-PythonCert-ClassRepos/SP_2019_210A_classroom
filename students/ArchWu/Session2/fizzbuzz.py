def printer(n):
    """Do the FizzBuzz behavior"""
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

def fizzbuzz(n = 100):
    """Main function that print FizzBuzz results"""
    for i in range(1, n + 1):
        printer(i)
