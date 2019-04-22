plus = "* "
minus = "- "
space = " "
vert = "| "


boxsize = int(input("Box Size: "))
gridsize = int(input("Grid Size: "))

# def box(boxsize):
#   line1 = str(plus+minus*boxsize+plus+'\n')
#   line2 = (vert+space*boxsize*2+vert+'\n')*boxsize
#   line3 = plus+minus*boxsize+plus
#   return str(line1+line2+line3)



def grid(boxsize, gridsize):
    line3 = minus * boxsize + plus
    row1 = plus + (((minus * boxsize) + plus) * gridsize)
    row2 = '\n' + (vert+(space * boxsize * 2 + vert) * gridsize + '\n') * boxsize
    row3 = plus+line3 * gridsize + '\n'
    grid = (row1 + row2) * gridsize + row3
    return grid

print(grid(boxsize, gridsize))
