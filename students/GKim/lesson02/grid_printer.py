def print_row(r):
    print("+", end = " ")
    for x in range(r -1):
        print("- - - - +", end = " ")
    print("- - - - +")
    return 
    
def print_column(c):
    for x in range(c):
        print("|      ", end = "")
        

print(print_row(4))
# print(print_column(4))