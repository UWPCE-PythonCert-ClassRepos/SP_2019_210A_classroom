"""
GridPrinter.py

Prints ascii grid based on desired box size and grid size.
"""


def grid(box_size=2, grid_size=2):
    """
    Return grid pattern as a string

    :param box_size: integer
    :param grid_size: integer
    :return: string
    """

    plus = '+'
    space = ' '
    dash = '-'
    pipe = '|'
    row_divider = (plus + ((space + dash) * box_size) + space) * grid_size + plus
    column_middle = ((pipe + (space * (box_size * 2) + space)) * grid_size) + pipe
    output = ''

    # Outer loop adds lines to distinguish between rows
    # Inner loop adds lines to distinguish between columns
    for _ in range(grid_size):
        output += row_divider + '\n'
        for _ in range(box_size):
            output += column_middle + '\n'
    output += row_divider
    return output


def main():
    print('box_size=5 (single argument, default 2x2 grid):', grid(5), sep='\n')
    print('box_size=1, grid_size=2:', grid(box_size=1, grid_size=2), sep='\n')
    print()
    print('box_size=2, grid_size=4:', grid(box_size=2, grid_size=4), sep='\n')


if __name__ == '__main__':
    main()

