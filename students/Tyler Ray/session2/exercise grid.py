plus = "+ "
minus = "- "
space = " "
vert = "| "
boxsize = int(input("Box Size: "))
gridsize = int(input("Grid Size: "))
line1 = str(minus * boxsize + plus)
line2 = (vert+(space * boxsize * 2 + vert) * gridsize + '\n') * boxsize
line3 = minus * boxsize + plus

'''
def box(boxsize):
  line1 = str(plus+minus*boxsize+plus+'\n')
  line2 = (vert+space*boxsize*2+vert+'\n')*boxsize
  line3 = plus+minus*boxsize+plus
  return str(line1+line2+line3)
'''

def grid(line1, line2, line3, gridsize):
    row1 = '+ '+ line1 * gridsize
    row2 = '\n' + line2
    row3 = '+ '+line3 * gridsize + '\n'
    grid = (row1 + row2) * gridsize + row3
    return grid

print(grid(line1, line2, line3, gridsize))
