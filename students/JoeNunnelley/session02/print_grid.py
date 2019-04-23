#! /usr/bin/env python3

"""
Lesson 02 : Print Grid Dual Inputs
Author : Joe Nunnelley
This module prints grids of various sizes depending on inputs
"""
import sys
import getopt

def print_inner(scale, dimension):
    """This function prints the inner row pattern"""
    open_row_start = "|" + ("   " * scale)
    middle_row = (open_row_start * dimension) + "|"

    for _ in range(scale):
        print(middle_row)

def print_grid(dimension, scale):
    """This function prints the vertical edge pattern"""
    side = "+" + (" - " * scale)
    vertical_side = (side * dimension)  + "+"

    for _ in range(dimension):
        print(vertical_side)
        print_inner(scale, dimension)

    print(vertical_side)

def usage():
    print('ERROR : Inputs must be positive numbers')
    print('Syntax: <script> -d <dimension> -s <scale>')


# Decided to make this a little more fun and work with inputs
def main(argv):
    """The main function of the program"""

    dimension = 0
    scale = 0

    try:
        opts, _ = getopt.getopt(argv, "hd:s:", ["dimension", "scale"])
    except getopt.GetoptError as err:
        print(err)
        print("Invalid options. Run <script> -h for help")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit(1)
        elif opt in ("-d", "--dimension"):
            dimension = int(arg)
        elif opt in ("-s", "--scale"):
            scale = int(arg)
    if dimension and scale:
        print("Dimesion : ", dimension)
        print("Scale    : ", scale)
    else:
        usage()
    print()

    # make that grid
    # you may specify unique values for dimension and scale
    # or you may simply specify dimension and it will be used
    # for the scale value
    # dimension = # of columms/rows
    # scale = the segments count between column/row lines
    print_grid(dimension, scale)

if __name__ == "__main__":
    main(sys.argv[1:])
