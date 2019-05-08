donors = [("Fred Mann",[100, 200, 50]),
          ("Niles Crane",[200]),
          ("Bob Harris",[4356, 3332]),
          ("Eric the Red",[34563,6788, 34534, 345]),]

def donorFinder(): #finds donor item within donors list by first index (the name)
    i = 0
    # listlen = len(donors)
    # for donor in donors:
    #     print("{}:".format(donors.index(donor)+1), donor)

    donorChoice = (input("Input: "))
    for donor in donors:

        if donorChoice == donor[0]:
            print(donors[i])
        else:
            i += 1
    donationAdd = input('Would you like to add a donation? (y/n)\n>>>')
    if donationAdd.strip().lower() == 'y' or 'yes':
        donAdd = int(input("How much? "))
        donor = donors[i]
        donor[1].append(donAdd)
        print(donors[i-1])



donorFinder()