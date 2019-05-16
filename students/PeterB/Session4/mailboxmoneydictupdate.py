

#donorList = [("William Gates", [653772.32, 12.17]),
#            ("Jeff Bezos", [877.33]),
#            ("Paul Allen", [663.23, 43.87, 1.32]),
#            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
#            ]

# created dictionary from above tuple
donorDict = {"William Gates":[653772.32, 12.17],
              "Jeff Bezos":[877.33],
             "Paul Allen":[663.23, 43.87, 1.32],
             "Mark Zuckerberg":[1663.23, 4300.87, 10432.0]
             }
#donorDict = dict(donorList)
#print(donorList)

userPrompt = "\n".join(("Please choose from the options below:",
          "1 = To view a list of donors type 'list'",
          "2 - Send a Thank You",
          "3 - Create a Report",
          "4 - Exit the Program",
          ">>> "))
#print(userPrompt)

def showList():
    '''Show list of donors'''
    print("Current donors include:")
    for names in range(len(donorList)):
        print(donorList[names][0])

def sendThankYou():
    '''Ask user for donor name and donor amount'''

    userNameResponse = input("Please enter a donor name:").title()

    donorNames = []
    for names in range(len(donorList)):
        donorNames.append(donorList[names][0])


    if userNameResponse in donorNames:
        userDonationAmt = float(input("Donor exists in DB, enter in new donation amount:"))

        for index, donor in enumerate(donorList):
            if userNameResponse in donor:
                donor[1].append(userDonationAmt)

        print("Dear Mr./Ms./Mrs. {:s}, \n Thank you for your generous donation of ${:.2f} to our organization. \n Sincerely,".format(userNameResponse, userDonationAmt))
    # if donor is not present in donor list
    else:
        userDonationAmt = float(input("New donor, please enter a donation amount:"))
        donorList.append((userNameResponse, [userDonationAmt]))

        # Generate an email using string formatting:
        print("Dear Mr./Ms./Mrs. {:s}, \n Thank you for your generous donation of ${:.2f} to our organization. \n Sincerely, ".format(
                userNameResponse, userDonationAmt))

def createReport():
    '''create a new list with donor names, total donation, number of donations
    and average donations'''
    donorSummary = []
    for index, donor in enumerate(donorList):
        donorName = donor[0]
        donorSum = float(sum(donor[1]))
        donationNum = int(len(donor[1]))
        donorMean = float(donorSum / donationNum)
        donorSummary.append([donorName, donorSum, donationNum, donorMean])

    def sort_key(donorSummary):
        return donorSummary[1]
    sortedDonorSummary = (sorted(donorSummary, key=sort_key, reverse=True))
    tableHeader = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
    sortedDonorSummary.insert(0,tableHeader)

    dash = '-' * 70
    for i in range(len(sortedDonorSummary)):
        if i == 0:
            print(dash)
            print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(sortedDonorSummary[i][0], sortedDonorSummary[i][1], sortedDonorSummary[i][2], sortedDonorSummary[i][3]))
            print(dash)
        else:
            print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(sortedDonorSummary[i][0], sortedDonorSummary[i][1], sortedDonorSummary[i][2],  sortedDonorSummary[i][3]))




def exitProgram():
    print("Thank you, good bye!")
    sys.exit()


def main():
    while True:
        userResponse = input(userPrompt)
        if userResponse == '1':
            showList()
        elif userResponse == '2':
            sendThankYou()
        elif userResponse == '3':
            createReport()
        elif userResponse == '4':
            exitProgram()

        else:
            print("Option not available")

if __name__ == "__main__":

    main()