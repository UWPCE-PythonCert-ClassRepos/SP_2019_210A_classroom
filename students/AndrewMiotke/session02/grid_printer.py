#!/usr/bin/env python3

# Long hand way of creating a grid
# def verbose_grid():
#     print("+",  " - " * 4, "+", " - " * 4, "+")

#     print("|              |              |")
#     print("|              |              |")
#     print("|              |              |")
#     print("|              |              |")

#     print("+",  " - " * 4, "+", " - " * 4, "+")

#     print("|              |              |")
#     print("|              |              |")
#     print("|              |              |")
#     print("|              |              |")

#     print("+",  " - " * 4, "+", " - " * 4, "+")

# verbose_grid()

# More general grid generator
def create_beam(beams):
    beam = '+ - - - - '
    plus = "+"
    end_line = end=' '

    print(beam * beams + plus + end_line)

def create_post(posts):
    post = '|         '

    print(post * (posts + 1))

def create_grid(cells, beams=0, posts=0):
    """
    Returns a grid based on the parameters of this function
    :param arg 1: define the number of cells
    :param arg 2: define the number of beams required to complete a cell
    :param arg 3: define the number of posts required to complete a cell

    Example: create_grid(10, 10, 10) would create a 10x10 grid using 10 cells
    """
    for _ in range(cells):
        create_beam(beams)
        create_post(posts)
        create_post(posts)
        create_post(posts)
    create_beam(beams)

create_grid(5, 5, 5)