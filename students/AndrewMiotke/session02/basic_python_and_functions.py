#!/usr/bin/env/python 3

# Function definition 
def fun(x, y):
    return x + y
# Function call
fun(3, 2)

# Creates a test that asserts that x + y will equal 5
def test_fun(x, y):
    assert x + y == 5

test_fun(3, 2)

