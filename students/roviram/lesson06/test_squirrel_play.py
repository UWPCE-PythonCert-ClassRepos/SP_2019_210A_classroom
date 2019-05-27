#---------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Week 6 Homework
# Script Name: Test Squirrel Play
# Script Creation Date: Saturday 5/18/2019
#---------------------------------------------------#
"""
test code for the Squirrel Play example

The squirrels in Palo Alto spend most of the day playing. https://codingbat.com/prob/p135815
    In particular, they play if the temperature is between 60 and 90 (inclusive).
    Unless it is summer, then the upper limit is 100 instead of 90.
    Given an int temperature and a boolean is_summer,
    return True if the squirrels play and False otherwise.
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""
from squirrel_play import squirrel_play


def test_1():
    assert squirrel_play(70, False) is True


def test_2():
    assert squirrel_play(95, False) is False


def test_3():
    assert squirrel_play(95, True) is True


def test_4():
    assert squirrel_play(100, True) is True


def test_5():
    assert squirrel_play(60, False) is True


def test_6():
    assert squirrel_play(50, False) is False




