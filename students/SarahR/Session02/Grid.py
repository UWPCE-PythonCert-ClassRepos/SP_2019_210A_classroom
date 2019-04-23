# SarahR.
# 04.16.2019. Original version of Grid program.
# 04.22.2019. The function for grid() was improved. Grid2() was written.

def grid(n):
    """
	Take one integer argument and print a grid cell size is given by the argument.

	Parameter
	    n: cell size

	"""
    plus = "+"
    minus = "-" + " "
    vert = "|"
    spaces = "  "

    grids_row = (plus + minus*n + plus + minus*n + plus)
    grids_column = (vert + spaces*(n) + vert + spaces*(n) + vert)

    # print the grid
    print(grids_row)
    for i in range(n):
        print(grids_column)
    print(grids_row)
    for i in range(n):
        print(grids_column)
    print(grids_row)



def grid2(n=3,a=2):
    """
	 Print a grid with a specified number of rows and columns, also with each cell a given size.

	Parameters
	    n: cell size
	    a: number os rows and columns

	"""
	#constants and variables
    plus = "+"
    minus = "-" + " "
    vert = "|"
    spaces = "  "

    grids_row = plus + ((minus*n) + plus)*a
    grids_column = (vert + ((spaces*n) + vert)*a)
    count = 1

    # print grid with a specified number of rows and columns
    print(grids_row)
    while count <= a:
        for i in range(n):
            print(grids_column)
        print(grids_row)
        count += 1


#grid()

#grid2()



