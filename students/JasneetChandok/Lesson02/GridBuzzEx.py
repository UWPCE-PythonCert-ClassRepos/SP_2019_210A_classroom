'''
Lesson: 02
Excercise: Grid Printer
Student Name: Jasneet Chandok
Last Update Date: 04/17/19
'''
#!/usr/bin/env python3.6


#Part 3
def print_grid(gridsize, boxsize):
    line1 = '+' + ((('-'*boxsize) + '+')*gridsize)
    line2 = '|' + (((' '*boxsize) + '|')*gridsize)
    box = (line1 + '\n') + ((((line2 + '\n')*boxsize) + (line1 + '\n'))*gridsize)
    print(box)
    return gridsize, boxsize

#print_grid(4,8)


'''
# Part 2
def print_grid(boxsize):
    line1 = '+' + ('-'*boxsize) + '+' + ('-'*boxsize) + '+'
    line2 = '|' + (' '*boxsize) + '|' + (' '*boxsize) + '|'
    box = (line1 + '\n') + ((line2 + '\n')*boxsize) + (line1 + '\n') + ((line2 + '\n')*boxsize) + (line1 + '\n')
    print(box)
    return boxsize


# Part 1
plus = '+'
minus = '-'
bar = '|'
space = '    '

print(plus, minus*4, plus, minus*4, plus)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(plus, minus*4, plus, minus*4, plus)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(bar, space, bar, space, bar)
print(plus, minus*4, plus, minus*4, plus)
'''


