def print_grid(x):
    """
    print grid with user defined dimensions

    :param x: The parameter that decides the length of grid

    """
    plus = '+'
    minus = '-'
    space = ' '
    column = '|'

    if x % 2:
        side = space + (minus + space) * (x // 2)
    else:
        side = (minus + space) * (x // 2)

    len = (column + space * x) * 2 + column
    border = (plus + side) * 2 + plus

    for i in range(0, x + 2):
        if i % (x // 2 + 1) == 0:
            print(border)
        else:
            print(len)

    if not x % 2:
        # This line is supposed to deal with n as an even integer
        print(border)


def print_grid2(x, length):
    """
    another grid printer that can define more details for a grid

    :param x: the number of rows and columns of grid
    :param length: the length of each cell in grid

    """
    plus = '+'
    minus = '-'
    space = ' '
    column = '|'
    line = (plus + (space + minus) * length + space) * x + plus
    wall = (column + space * (2 * length + 1)) * x + column

    for i in range(0, x + x * length + 1):
        if i % (length + 1) == 0:
            print(line)
        else:
            print(wall)
