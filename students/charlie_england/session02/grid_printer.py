def pri_grid():
    for x in range(5):
        if x % 2 == 0:
            print("+", "-"*4, "+", "-"*4, "+")  
        else:
            for _ in range(3):
                print("|", " "*4, "|", " "*4, "|")

pri_grid()
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
# for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
# print("+","-"*4,"+","-"*4,"+")
