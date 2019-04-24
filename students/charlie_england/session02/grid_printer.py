
def pri_grid(size = 2, cols = 2, rows = 2): #instead of just 2 parameters, allows you to change the # of rows and cols independently
    '''
    prints a grid that has a size, number of columns and number of rows
    default is size 2, 2 columns and 2 rows
    '''
    for _ in range(rows): # for ever row: print the +...- line and a number of the |...| lines
        print((" +" + " -"*size)*cols+" +") #prints the +, - line. Changes number of '-' with the size and the number of + with the number of columns
        for _ in range(size): #prints the |    | line that varies the " " and number of lines by size, also prints the repeats for the number of columns
            print((" |" + "  "*size)*cols+" |")
    print((" +" + " -"*size)*cols+" +") 

pri_grid(5,5,10)
pri_grid(3, 3, 5)
