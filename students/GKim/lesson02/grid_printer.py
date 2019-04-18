

def print_row(c): 
    """
    function to print + and - using a 
    for loop .  Using input from user the range is -1 because
    from the first intial print the  section of the column is already created
    this all prints accross
    """
    print("+", end = " ")  
    for _ in range(c - 1):
        print("- - - - +", end = " ")
    print("- - - - +")

def print_column(c):
    """
    prints the "columns" " | " in the grid. just like the row first section is 
    already created by the input given from user.  The colums print across and 
    down
    """
    print("|", end = " ")
    for _ in range(c - 1):
        print("        |", end = " ")
    print("        |")

def my_grid(c,r):
    """
    function that puts print_row. print_column all together for the grid.  All determined
    by the user input

    """
    print_row(c)
    for _ in range(r): # the number of rows in the grid.  
        for _ in range(4): # range of 4 for how many | that connect each +
            print_column(c)
        print_row(c)


# input command from the user
c = int(input("Column: "))
r = int(input("Row: "))

my_grid(c,r)

