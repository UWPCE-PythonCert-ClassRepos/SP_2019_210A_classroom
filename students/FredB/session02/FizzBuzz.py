#FizzBuzz
#FredBallyns
#Session02


def fizzBuzz():
    index=1
    while index < 101:
        if index % 15 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print (index)
        index = index +1