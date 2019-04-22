# SarahR.
# 04.21.2019. Original version of Fizz Buzz program.

#Goal:

#Write a program that prints the numbers from 1 to 100 inclusive.
#But for multiples of three print “Fizz” instead of the number.
#For the multiples of five print “Buzz” instead of the number.
#For numbers which are multiples of both three and five print “FizzBuzz” instead.

for e in range(1, 101):
    if e % 3 == 0  and e % 5 == 0:
        print(e, "FizzBuzz")
    elif e % 3 == 0:
        print(e, "Fizz")
    elif e % 5 == 0:
        print(e, "Buzz")
    else:
        print(e)

