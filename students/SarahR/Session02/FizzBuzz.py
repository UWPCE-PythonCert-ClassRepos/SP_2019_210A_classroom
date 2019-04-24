# SarahR.
# 04.21.2019. Original version of Fizz Buzz program.
# 04.22.2019. Documentation was made.


for e in range(1, 101):
    # for multiples of 3 and 5, prints "FizzBuzz"
    if e % 3 == 0 and e % 5 == 0:
        print("FizzBuzz")
    #for multiples of 3, prints "Fizz"
    elif e % 3 == 0:
        print("Fizz")
    # for multiples of 5, prints "Buzz"
    elif e % 5 == 0:
        print("Buzz")
    # any others, prints the number itself
    else:
        print(e)

