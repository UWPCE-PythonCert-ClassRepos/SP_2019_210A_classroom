plus = "+ "
minus = "- "
space = " "
vert = "| "

boxsize = int(input("Box Size: "))
gridsize = int(input("Grid Size: "))

def grid(gridsize, boxsize):
    row1 = plus + (minus * boxsize + plus) * gridsize
    row2 = '\n' + (vert + (space * boxsize * 2 + vert) * gridsize + '\n') * boxsize
    row3 = (plus + minus * boxsize) * gridsize + plus
    grid = (row1 + row2) * gridsize + row3
    return grid

print(grid(gridsize, boxsize))
