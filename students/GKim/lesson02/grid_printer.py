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
    if c % 2 == 0:
        x = int(c)/2
    elif c % 2 == 1:
        x = int(c-1)/2
    for _ in range(a-1):
        print("+", end = "")
        print(" - " * int(x), end = "")
    print("+")

def print_column(c, a =3):
    """
    prints the "columns" " | " in the grid. just like the row first section is 
    already created by the input given from user.  The colums print across 
    """
    if c % 2 == 0:
        x = int(c)/2
    elif c % 2 == 1:
        x = int(c-1)/2
    for _ in range(a-1):
        print("|", end = "")
        print("   " * int(x), end = "")
    print("|")
    

def my_grid(c,a=3):
    """
    function that puts print_row. print_column all together for the grid.  All determined
    by the user input

    """
    c = c * 2

    if c % 2 == 0:
        x = int(c)/2
    elif c % 2 == 1:
        x = int(c-1)/2
    print_row(c,a)
    for _ in range(a-1): # the number of rows in the grid.  
        for _ in range(int(x)): # range of 4 for how many | that connect each +
            print_column(c,a) # moving down
        print_row(c,a)




# print(print_row(4))
# print(print_column(4))
my_grid(3,5)



