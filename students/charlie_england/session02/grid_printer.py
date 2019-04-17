def plus():
    print("+","-"*4,"+","-"*4,"+")

def bar():
    for num in range(4):
        print("|", " "*4,"|", " "*4, "|")


#print("+","-"*4,"+","-"*4,"+")
#for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
#print("+","-"*4,"+","-"*4,"+")
#for num in range(4):
#    print("|", " "*4,"|", " "*4, "|")
#print("+","-"*4,"+","-"*4,"+")

for x in range(6):
    if x %2 != 0:
        plus()
    else:
        bar()