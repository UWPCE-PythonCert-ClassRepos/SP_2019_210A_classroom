plus = '+'
minus = '- '
bar = '|'
space = ' '

# print_grid2(3,4)Width = 4

def print_row(length):
    print(plus + space + minus * length + plus+space + minus * length + plus+space + minus * length+ plus)

def print_column(length):
    print(bar + space+space*length *2 + bar + space+space*length*2 + bar+ space+space*length*2 + bar)


def grid_print (length):
    for _ in range(2):
        print_row(length)
        for _ in range(length):
            print_column(length)
    print_row(length)

# grid_print(3)

def grid_print2(cells, length):
    for _ in range(cells):
        print_row(length)
        for _ in range(length):
            print_column(length)
    print_row(length)

grid_print2(3,4)

