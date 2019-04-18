

def print_row(c): 
    """
    function to print + and - using a 
    for loop 
    """
    print("+", end = " ")  
    for _ in range(c - 1):
        print("- - - - +", end = " ")
    print("- - - - +")

def print_column(c):
    print("|", end = " ")
    for _ in range(c - 1):
        print("        |", end = " ")
    print("        |")

def my_grid(c,r):
    print_row(c)
    for _ in range(r):
        for _ in range(4):
            print_column(c)
        print_row(c)


# c = int(input("Column: "))
# r = int(input("Row: "))

# my_grid(4,4)

print_column(4)