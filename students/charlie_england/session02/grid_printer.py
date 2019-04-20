def pri_grid(num_rows=2, num_columns=2, size=4):
    for x in range(num_rows*2+1):
        if x %  2 == 0:  # print horizontal bars
            for nc in range(num_columns*2+1):
                if nc % 2 == 0:
                    print("+ ", end="")
                else:
                    print("- " * size, end="")
                if nc == num_columns*2:
                    print("")
        else:  # print open space
            for _ in range(size):
                for nc in range(num_columns*2+1):
                    if nc % 2 == 0:
                        print("|", end="")
                    else:
                        print(" " * (size * 2 + 1), end="")
                    if nc == num_columns*2:
                        print("")


pri_grid(3, 3, 5)
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
