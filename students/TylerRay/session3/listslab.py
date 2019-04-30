strChoice = True
list = ['apples', 'pears', 'oranges', 'peaches']
while strChoice != False:

    print("""
    Menu of Options
    1) Show current list of fruit

    2) Add a fruit to the end of the list.

    3) Find fruit by number

    4) Add fruit to the beginning of the list

    5) Delete the first fruit

    6) Delete fruit by number

    7) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()
    if (strChoice.strip() == '1'):
        print(list)

    elif (strChoice.strip() == '2'):

        endfruit = input("What fruit do you want to add? ")
        if endfruit not in list:
            list.append(endfruit)

        else:
            print("That fruit is already in the list.")
    elif (strChoice == '3'):
        print('There are', len(list), "fruits in the list.")
        print("Which one do you want to view? ")
        fc = int(input())
        extent = len(list)
        if fc-1 in range(extent):
            print(list[fc-1])
        else:
            print("That wasn't a valid choice.")


    elif (strChoice == '4'):

        endfruit = input("What fruit do you wantto add? ")
        if endfruit not in list:
            list.insert(0, endfruit)

        else:
            print("That fruit is already in the list.")

    elif (strChoice == '5'):
        pop = list.pop(0)
        print(pop, "deleted")

    elif (strChoice == '6'):
        print("There are", len(list), "fruits in the list.")
        print("Which fruit number do you want to delete?")
        fdel = int(input())
        extent = len(list)
        if fdel in range(0, extent):
            list.pop(fdel-1)

    else:
        strChoice = False

print("Goodbye")