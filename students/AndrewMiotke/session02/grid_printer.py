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

def create_grid(beams, posts):
    """
    Returns a grid based on the parameters of this function
    :param arg 2: define the number of beams(x axis) required to complete a cell
    :param arg 3: define the number of posts(y axis) required to complete a cell

    Example: create_grid(10, 10) would create a 10x10 grid
    """
    for _ in range(posts):
        create_beam(beams)
        create_post(posts)
        create_post(posts)
        create_post(posts)
    create_beam(beams)

create_grid(10, 10)