
'''choms'''

import sys
import os

print("in mailroom")
'''Writing first name is easier for testing.'''
donors ={"Fred Gates": [100.90, 200, 50], "Jeff Bezos": [100, 50, 600], "Mark Zuckerberg": [200, 50, 500],
          "Paul Allen": [300, 40, 200]}


# donors = {{"first_name": "Fred", "last_name": "Gates"}: [[100.90, 200, 50], 265.98]}


def addDonation(person, amount):
    if person not in donors.keys():
        donors[person] = []
    donors[person].append(amount)

def genThankYouLetter(person, amount):
    email = '''
    Dear {0},
    Thank you for donating {1}!\n'''.format(person, amount)
    return email

def thank_you():
    response = input("Type your donor name, if don't know, type list to pick")
    '''If the user types list show them a list of the donor names and re-prompt'''
    person = ""
    if response == "list":
        for key in donors.keys():
            print(key)
        person = input("Please type your donor name.")
    else:
        person = response

    newDonation = input("how much to donate?")
    validInput = False
    amount = 0.0
    while not validInput:
        try:
            amount = float(newDonation)
            validInput = True
        except ValueError:
            newDonation = input("Please input numbers!")

    addDonation(person, amount)
    email = genThankYouLetter(person, amount)
    print(email)
    return email



def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num)
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
    output = "{:<20}{:<20}{:<15}{:<20}\n".format("Donor Name", "|Total Given", "|Num Gifts", "|Average Gift")
    output += "-------------------------------------------------------------------\n"


    '''  
    for amount in sortedAmount:
        nameList = amountToNames[amount]
        for name in nameList:
            numGifts = len(donors[name])
            output += lineItem(name, amount, numGifts, amount / numGifts)
            
    '''
    '''Change the code by using comprehensions'''

    output += "".join(
        lineItem(name, amount, len(donors[name]), amount / len(donors[name])) for amount in sortedAmount for name in amountToNames[amount])

    print(output)
    return output



def lineItem(name, total, numGifts, avg):
    output = "{:<20}${:<20.2f}{:<15}${:<20.2f}\n".format(name, total, numGifts, avg)
    return output


def gen_thank_you_letters(a_dict):
    dir = "thankyouLetters"
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass
    os.cir(dir)
    for name, amount in donors.items():
        firstLastName = name.split()
        fileName = firstLastName[0] + "_" + firstLastName[1] + ".txt"
        with open(fileName, "w") as f:
            f.write('''
            Dear {0},
                    Thank you for your very kind donation of ${1:.2f}.

                    It will be put to very good use.

                                        Sincerely,
                                            - The Team'''.format(name, sum(amount)))

def quit():
    print("quitting")
    sys.exit()


def main_menu():
    while True:
        answer = input("""What would you like to do?
    Pick one:
    1. Send a Thank You to a single donor
    2. Create a Report
    3. Send Thankyou letters to all donors
    4. Quit
    >>>""")
        print("You picked:", answer)
        answer = str(answer).strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            gen_thank_you_letters(donors)
        elif answer == "4":
            quit()
        else:
            print("Please answer 1, 2, 3, 4")


if __name__ == '__main__':
    print('Welcome to the mailroom!')

    main_menu()


