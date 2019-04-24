#!/usr/bin/env python3

def verbose_grid():
    """
    Returns a 2x2 grid
    This is hard coded and not flexible at all
    """
    print("+",  " - " * 4, "+", " - " * 4, "+")

    print("|              |              |")
    print("|              |              |")
    print("|              |              |")
    print("|              |              |")

    print("+",  " - " * 4, "+", " - " * 4, "+")

    print("|              |              |")
    print("|              |              |")
    print("|              |              |")
    print("|              |              |")

    print("+",  " - " * 4, "+", " - " * 4, "+")

verbose_grid()

# Variables to make up grids below
plus = '+'
minus = '- '
post = '|'
space = ' '

def create_beam(size):
    print(plus + space + minus * size + plus + space + minus * size + plus)

def create_post(size):
    print(post + space + space * size * 2 + post + space + space * size * 2 + post + space + space * size * 2)
    
def create_grid(size):
    """
    Returns a 2x2 grid with flexible cell height and width
    :param arg 0: define the arguement in the function call to determine the height('|') and width('-') of each cell
    """
    for _ in range(2):
        create_beam(size)
        for _ in range(size):
            create_post(size)
    create_beam(size)

create_grid(5)

def print_grid(cells, size):
    """
    Returns a Xx2 grid with flexible cell height and width
    :param arg 0: defines the number of cells along the y axis
    :param arg 1: defines the height('|') and width('-') of each cell
   """
    for _ in range(cells):
        create_beam(size)
        for _ in range(size):
            create_post(size)
    create_beam(size)

print_grid(5, 5)

