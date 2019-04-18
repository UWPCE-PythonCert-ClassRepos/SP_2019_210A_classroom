#!/usr/bin/env python3

# Long hand way of creating a grid
def verbose_grid():
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

# More general grid generator
def create_beam():
    beam = '+ - - - - '
    plus = "+"
    end_line = end=' '

    print(beam * 2 + plus + end_line)

def create_post():
    post = '|         '

    print(post * 3)

def create_grid(cells):
    for _ in range(cells):
        create_beam()
        create_post()
        create_post()
        create_post()
    create_beam()

create_grid(5)