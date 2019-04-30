#!/usr/bin/env python

print("in mailroom")

# list of donors
donors = [("Fred Flinstone", [100, 200, 300]),
          ("Joy Grey", [50, 200]),
          ("Susan May", [20, 100, 75]),
          ("Joshua Carter", [500, 200]),
          ("Jim Starson ", [60, 60, 60])
          ]

def is_name_in_list(name):
    ''' Check if name given is in donors list'''

    for donor in donors:
        if name in donor[0]:
            return True

    return False

def thank_you():
    ''' Take a donor name and its donations send a thank you message to them '''

    name = input("What donor would you like to thank?")
    # show donors list
    if name == "list":
        print("All donors in the list are: ")
        for donor in donors:
            print(donor[0])
        name = input("What donor would you like to thank?")
    # check if name give is already in the list, if not it is added
    if not is_name_in_list(name):
        newDonor = (name, [])
        donors.append(newDonor)
        print("new donor added")

    #take the donation amount
    donation = int(input("What is the donation amount?"))
    for donor in donors:
        if name in donor[0]:
            donor[1].append(donation)

    # send an email thanking for the donation
    email = "Dear {}, thank you for your generous donation!".format(name)

    print(email)

def gen_stats(donor):
    '''Genarate donations stats: Donor name, total given, num donations and average donation'''
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total/num)

    return stats

def report():
    '''Generate a graphic report of users donation'''

    print('{:20}|{:^10}|{:^10}|{:^10}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-"*55)
    for donor in donors:
        stats = gen_stats(donor)
        print('{:20} ${:10} {:10} ${:10}'.format(stats[0], stats[1], stats[2], stats[3]))


def quit():
    '''Quit program'''

    print("Quitting")
    exit()



def main_menu():
    '''Show menu of options to the user'''

    while True:
        answer = input("What would you like to do? '\n' Pick one: '\n'"
                       "1: Send a Tkank You note '\n'"
                       "2: Create a report '\n'"
                       "3: Quit")
        print("You replied:", answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2 or 3.")

if __name__ == '__main__':
    print("Welcome to the mailroom")

    main_menu()
