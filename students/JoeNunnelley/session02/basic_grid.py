#! /usr/bin/env python3

"""
Lesson 02 : Basic Grid
Author : Joe Nunnelley
"""
def print_basic_grid(n):
    """A function to build a grid based on a single dimension input"""
    horizontal_line = ('+' + (' - ' * n)) * n + '+'
    vertical_line   = ('|' + ('   ' * n)) * n + '|'

    print(horizontal_line)
    for i in range(n):
        for _ in range(n):
            print(vertical_line)
        print(horizontal_line)

print_basic_grid(1)
print_basic_grid(2)
print_basic_grid(3)
