"""You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0"""


from caught_speeding import caught_speeding

def test_1():
    assert caught_speeding(60, False) == 0


def test_2():
    caught_speeding(65, False) == 1


def test_3():
    caught_speeding(65, True) == 0

def test_4():
    caught_speeding(90, True) == 0

def test_5():
    caught_speeding(90, False) == 0