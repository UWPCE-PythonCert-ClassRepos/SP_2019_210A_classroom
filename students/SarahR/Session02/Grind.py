
"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""   


def grind(n):
    plus = "+"
    minus = "-" + " "
    vert = "|"
    spaces = "  "

    grinds_row = (plus + minus*n + plus + minus*n + plus)
    #grinds_column = ("\n" + (vert + "\n")*4 + plus)
    grinds_bottom_row = (minus*4 + plus + " " + minus*4 + plus)
    grinds_column_right = ((vert + "\n")*4)
    grinds_column = (vert + spaces*(n) + vert + spaces*(n) + vert)
    #grinds_test2= (vert, spaces*9, vert,  end=' +')
    #print(grinds_row, grinds_column_right, grinds_column, grinds_bottom_row)

    print(grinds_row)
    for i in range(n):
        print(grinds_column)
    print(grinds_row)
    for i in range(n):
        print(grinds_column)
        #print(grinds_test)
        #print(grinds_test)
        #print(grinds_test)
    print(grinds_row)
 
grind(2)


	

