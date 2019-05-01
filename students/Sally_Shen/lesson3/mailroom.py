

'''choms'''

import sys

print("in mailroom")
'''Writing first name is easier for testing.'''
donors ={"Fred Gates": [100.90, 200, 50], "Jeff Bazos": [100, 50, 600], "Mark Zuckerberg": [200, 50, 500],
         "Paul Allen": [300, 40, 200]}


def thank_you():
    response = input("Type your donor name, if don't know, type list to pick")
    '''If the user types list show them a list of the donor names and re-prompt'''
    if response == "list":
        for key in donors.keys():
            print(key)
        response = input("Please type your donor name.")

    if response not in donors.keys():
        donors[response] = []

    newDonation = input("how much to donate?")
    donors[response].append(float(newDonation))
    email = '''
    Dear {0},
    Thank you for donating {1}!\n'''.format(response, newDonation)
    print(email)


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num  =  len(donations)
    stats = (donor[0], total, num, total/num)
    return

def report():
    amountToNames = {}
    for name, amount in donors.items():
        total = sum(amount)
        if total in amountToNames.keys():
            amountToNames[total].append(name)
        else:
            amountToNames[total] = [name]

    sortedAmount = sorted(amountToNames, reverse=True)
    output = "{:<15}${:<15}{:<12}${:<12}\n".format("Donor Name", "|Total Given", "|Num Gifts", "|Average Gift")
    output += "-------------------------------------------------------------\n"


    for amount in sortedAmount:
        nameList = amountToNames[amount]
        for name in nameList:
            numGifts = len(donors[name])
            output += lineItem(name, amount, numGifts, amount/numGifts)
    print(output)

def lineItem(name, total, numGifts, avg):
    output = "{:<15}${:<15}{:<12}${:<12.2f}\n".format(name, total, numGifts, avg)
    return output

def quit():
    print("quitting")
    sys.exit()



def main_menu():

    while True:
        answer = input ("""What would you like to do?
    Pick one:
    1. Send a Thank You
    2. Create a Report
    3. Quit
    >>>""")
        print("You picked:", answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, 3")


if __name__ == '__main__':
    print('Welcome to the mailroom!')

    main_menu()


