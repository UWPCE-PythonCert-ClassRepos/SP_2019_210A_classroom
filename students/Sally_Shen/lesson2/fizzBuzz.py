''''Fizz Buzz
Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print “Fizz” instead of the number.
For the multiples of five print “Buzz” instead of the number.
For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''

def fizzBuzz(n):

    output = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')

        else:
            output.append(str(i))
    return output

print(fizzBuzz(20))
