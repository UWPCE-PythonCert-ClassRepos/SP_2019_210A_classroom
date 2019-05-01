
"""
Shortened version
"""

def print_symbol(c , a=2 , s1="", s2=""): 
    """
    function to print + and - using a 
    for loop .  Using input from user the range is -1 because
    from the first intial print the  section of the column is already created
    this all prints accross
    """
    x = c // 2
    for _ in range(a):
        print("{}".format(s1), end = "")
        print(" {} ".format(s2) * int(x), end = "")
    print("{}".format(s1))


def my_grid(c, a = 2):
    """
    function that puts print_row. print_column all together for the grid.  All determined
    by the user input

    """
    x = c // 2
    print_symbol(c, a, s1 = "+", s2 = "-")
    for _ in range(a): # the number of rows in the grid.  
        for _ in range(int(x)): # range of 4 for how many | that connect each +
            print_symbol(c, a, s1 ="|", s2 =" ") # moving down
        print_symbol(c, a, s1="+", s2="-")

def my_grid2(c, a = 2):

    c *= 2
    my_grid(c,a)









# def print_row(c, a =2): 
#     """
#     function to print + and - using a 
#     for loop .  Using input from user the range is -1 because
#     from the first intial print the  section of the column is already created
#     this all prints accross
#     """
#     if c % 2 == 0:
#         x = int(c)/2
#     elif c % 2 == 1:
#         x = int(c-1)/2
#     for _ in range(a):
#         print("+", end = "")
#         print(" - " * int(x), end = "")
#     print("+")

# def print_column(c, a =2):
#     """
#     prints the "columns" " | " in the grid. just like the row first section is 
#     already created by the input given from user.  The colums print across 
#     """
#     if c % 2 == 0:
#         x = int(c)/2
#     elif c % 2 == 1:
#         x = int(c-1)/2
#     for _ in range(a):
#         print("|", end = "")
#         print("   " * int(x), end = "")
#     print("|")
    

# def my_grid(c,a=2):
#     """
#     function that puts print_row. print_column all together for the grid.  All determined
#     by the user input

#     """
#     if c % 2 == 0:
#         x = int(c)/2
#     elif c % 2 == 1:
#         x = int(c-1)/2
#     print_row(c,a)
#     for _ in range(a): # the number of rows in the grid.  
#         for _ in range(int(x)): # range of 4 for how many | that connect each +
#             print_column(c,a) # moving down
#         print_row(c,a)

# def my_grid2(c, a=2):

#     c *= 2
#     if c % 2 == 0:
#         x = int(c)/2
#     elif c % 2 == 1:
#         x = int(c-1)/2
#     print_row(c,a)
#     for _ in range(a): # the number of rows in the grid.  
#         for _ in range(int(x)): # range of 4 for how many | that connect each +
#             print_column(c,a) # moving down
#         print_row(c,a)

# print(print_row(4))
# print(print_column(4))
my_grid(11)
my_grid2(3,5)



