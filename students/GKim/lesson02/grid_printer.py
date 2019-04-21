"""
FYI not my code , got help from you tube... but I understand and like this method.
"""

def print_row(c, a =3): 
    """
    function to print + and - using a 
    for loop .  Using input from user the range is -1 because
    from the first intial print the  section of the column is already created
    this all prints accross
    """
    for _ in range(a-1):
        print("+", end = "")
        print(" - " * ((c-1)//2), end = "")
    print("+")

def print_column(c, a =3):
    """
    prints the "columns" " | " in the grid. just like the row first section is 
    already created by the input given from user.  The colums print across 
    """
    for _ in range(a-1):
        print("|", end = "")
        print("   " * ((c-1)//2), end = "")
    print("|")
    

def my_grid(c,a =3):
    """
    function that puts print_row. print_column all together for the grid.  All determined
    by the user input

    """
    print_row(c,a)
    for _ in range(3-1): # the number of rows in the grid.  
        for _ in range((c-1)//2): # range of 4 for how many | that connect each +
            print_column(c,a) # moving down
        print_row(c,a)

# print(print_row(4))
# print(print_column(4))





my_grid(3)

