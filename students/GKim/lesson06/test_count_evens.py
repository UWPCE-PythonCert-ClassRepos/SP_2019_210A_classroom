


"""
test code from count evens on coding bat

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0

"""
from count_evens import count_evens

def test_1():
    assert count_evens([2, 1, 2, 3, 4]) == 3

def test_2():
    assert count_evens([2, 2, 0]) == 3

def test_3():
    assert count_evens([2, 6, 8, 10]) == 4

def test_4():
    assert count_evens([1, 3, 5]) == 0

def test_5():
    assert count_evens([11, 9, 0, 1]) == 1

def test_6():
    assert count_evens([2, 11, 9, 0]) == 2

def test_7():
    assert count_evens([2, 5, 12]) == 2

def test_8():
    assert count_evens([2]) == 1