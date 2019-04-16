#!/usr/bin/env python3

# Long hand way of creating a grid
# def verbose_grid():
#     print("+",  "-" * 4, "+", "-" * 4, "+")

#     print("|      |      |")
#     print("|      |      |")
#     print("|      |      |")
#     print("|      |      |")

#     print("+",  "-" * 4, "+", "-" * 4, "+")

#     print("|      |      |")
#     print("|      |      |")
#     print("|      |      |")
#     print("|      |      |")

#     print("+",  "-" * 4, "+", "-" * 4, "+")

# verbose_grid()

# More general grid generator
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_six(f):
    do_twice(f)
    do_twice(f)
    do_twice(f)

def print_beam():
    print("+ - - - -", end=" ")

def print_post():
    print("|        ", end=" ")

def print_beams():
    do_twice(print_beam)
    print("+")

def print_posts():
    do_twice(print_post)
    print("|")

def print_row():
    print_beams()
    do_four(print_posts)


def print_grid(t):
    # do_twice(print_row)
    print_row()
    print_beams()

print_grid(5)





# def do_twice(f):
#     f()
#     f()

# def do_four(f):
#     do_twice(f)
#     do_twice(f)

# def print_beam():
#     print('+ - - - -', end=' ')

# def print_post():
#     print('|        ', end=' ')

# def print_beams():
#     do_twice(print_beam)
#     print('+')

# def print_posts():
#     do_twice(print_post)
#     print('|')

# def print_row():
#     print_beams()
#     do_four(print_posts)

# def print_grid():
#     do_twice(print_row)
#     print_beams()

# print_grid()