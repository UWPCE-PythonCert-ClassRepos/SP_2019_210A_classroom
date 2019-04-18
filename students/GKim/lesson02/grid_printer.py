

def print_row(c): 
    """
    function to print + and - using a 
    for loop .  Using input from user the range is -1 because
    from the first intial print the  section of the column is already created
    """
    print("+", end = " ")  
    for _ in range(c - 1):
        print("- - - - +", end = " ")
    print("- - - - +")

def print_column(c):
    """
    prints the "columns" " | " in the grid. just like the row first section is 
    already created by the input given from user
    """
    print("|", end = " ")
    for _ in range(c - 1):
        print("        |", end = " ")
    print("        |")

def my_grid(c,r):
    """
    function that puts print_row. print_column all together

    """
    print_row(c)
    for _ in range(r):
        for _ in range(4): # range of 4 for how many | that connect each +
            print_column(c)
        print_row(c)


# c = int(input("Column: "))
# r = int(input("Row: "))

# my_grid(4,4)

print_column(4)