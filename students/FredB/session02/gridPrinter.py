#gridPrinter
#FredBallyns
#Session02


def print_grid(n):
    #makes a 2 by 2 grid where each box is contains n by n rows and columns
    Corner ="+"
    Horizontal = "-"
    Vertical = "|"
    Space = " "
    #Alternates between line types
    print(Corner + Horizontal*n + Corner + Horizontal*n + Corner)
    print((Vertical + Space*n + Vertical + Space*n + Vertical+ "\n")*n, end="")
    print(Corner + Horizontal*n + Corner + Horizontal*n + Corner)
    print((Vertical + Space*n + Vertical + Space*n + Vertical+ "\n")*n, end="")
    print(Corner + Horizontal*n + Corner + Horizontal*n + Corner)

def print_grid2(n, r=2,c=2):
    #makes a grid of r rows by c columns where each box is contains n by n rows and columns
    Corner ="+"
    Horizontal = "-"
    Vertical = "|"
    Space = " "
    #line1 top edge
    line1 = Corner + (Horizontal*n+ Corner)*c + "\n"
    line2 = Vertical + (Space*n + Vertical)*c + "\n"
    print(line1 + (line2*n + line1)*r,end=' ')


if __name__ == "__main__":
    # Run a couple tests
    print("Tiny")
    print_grid2(0)
    print ("small")
    print_grid2(3)
    print("large")
    print_grid2(4,7,14)