#-----------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Desc: Grid Printer Homework, Week 2
# Date Created: Sunday 4/21
#-----------------------------------------------------------#
"""
Goal:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
plus = "+"
minus = "- "
vertical = "| "

def print_row(cell, length):
    for _ in range(cell):
        print(plus + " " + minus * length, end="")
    print(plus)

def print_column(cell, length):
    for _ in range(cell):
        print(vertical + "  " * length, end="")
    print(vertical)

def print_grid(cell, length):
    for _ in range(cell):
        print_row(cell, length)
        for _ in range(length):
            print_column(cell, length)
    print_row(cell, length)

print_grid(4,4)
