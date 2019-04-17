def pri_grid(num_rows=2, num_columns=2):
    for x in range(num_rows*2+1):
        if x % 2 == 0:
            for nc in range(num_columns*2+1):
                if nc % 2 == 0:
                    print("+ ", end="")
                else:
                    print("- "*4, end="")
                if nc == num_columns*2:
                    print("")
        else:
            for _ in range(3):
                for nc in range(num_columns*2+1):
                    if nc % 2 == 0:
                        print("|", end="")
                    else:
                        print(" "*9, end="")
                    if nc == num_columns*2:
                        print("")


pri_grid(3, 3)
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
