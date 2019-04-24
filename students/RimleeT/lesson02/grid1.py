def print_grid2(number_of_rows_column, size_unit):
	plus = '+'
	minus = '-'*size_unit
	line = '|'
	space = ' '*size_unit
	for i in range(0,number_of_rows_column):
		#print (plus + minus + plus + minus + plus)
		print((plus + minus)*(number_of_rows_column) + plus)
		for j in range(0,size_unit):
			print ((line + space)*(number_of_rows_column) + line)
	print((plus + minus)*(number_of_rows_column) + plus)
print_grid2(5,4)