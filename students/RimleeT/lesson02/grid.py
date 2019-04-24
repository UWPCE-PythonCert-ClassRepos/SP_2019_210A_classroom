"""
Part 1 : Write a function that draws a grid(fixed grid)
"""
plus = '+'
minus = '-'*4
line = '|'
space = ' '*4
horizontal = (plus + minus)*2 + plus
vertical = (line + space)*2 + line
print (horizontal)
print (vertical)
print (vertical)
print (vertical)
print (vertical)
print (horizontal)
print (vertical)
print (vertical)
print (vertical)
print (vertical)
print (horizontal)


"""
Part 2 : Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.
"""
def print_grid(n):
	size_unit = (n-1)//2
	plus = '+'
	minus = '-'*size_unit
	line = '|'
	space = ' '*size_unit
	print ((plus + minus)*2 + plus)
	for i in range(0,size_unit):
		print ((line + space)*2 + line)
	print ((plus + minus)*2 + plus)
	for i in range(0,size_unit):
		print ((line + space)*2 + line)
	print ((plus + minus)*2 + plus)


print_grid(3)
print_grid(15)


"""
Part 3 : Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.
"""
def print_grid2(number_of_rows_column, size_unit):
	plus = '+'
	minus = '-'*size_unit
	line = '|'
	space = ' '*size_unit
	for i in range(0,number_of_rows_column):
		print((plus + minus)*(number_of_rows_column) + plus)
		for j in range(0,size_unit):
			print ((line + space)*(number_of_rows_column) + line)
	print((plus + minus)*(number_of_rows_column) + plus)

print_grid2(1,2)
print_grid2(5,2)	
print_grid2(10,10)




	
	
	