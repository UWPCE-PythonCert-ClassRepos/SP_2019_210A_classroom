#Mailroom Part1
#FredBallyns
#Session03

import sys
import os

donors = [("Fred Flintstone", [100, 200, 50]),
        ("James Bond", [0,0,7]),
        ("Lex Luthor", [5000,]),
        ("Harambe", [3, 2, 1]),
        ("Herman Cain", [9, 9, 9])
        ]

def clear_screen():
    #Windows 'nt'
    if os.name == 'nt':
        clearText="cls"
    #Linux 'posix'   
    else:
        clearText="clear"
    os.system(clearText)


def thank_you():
    #print("in thank you")
    donor = input("Enter full name of donor else type 'list' to see donor list: ")
    if donor.lower() == 'list':
        print('\n','Donor List','\n', "------")
        for i in donors:
            print(i[0])
        print('\n')
    else:
        # Add new donation
        donation = int(input("Enter donation amount: "))
        # Search if repeat donor
        onlist = False
        for i in donors:
            if i[0].lower() == donor.lower():
                donor = i[0] #reuse existing format
                i[1].append(donation)
                onlist = True
        # Add first time donor
        if onlist == False:
            donors.append((donor,[donation]))
        print("donors",'\n','------------',donors)
        print (f"Thank you {donor} for your generous donation of ${donation} from a charity")


def report():
    print('Donor Name      | Total Given | Num Gifts   |  Average Gift')
    print("-"*60)
    stats = gen_stats()
    stats = sorted(stats, key=lambda x: x[1], reverse=True)
    for j in stats:
        print('{:15}   ${:10.2f}{:8}         ${:10.2f}'.format(*j))


def gen_stats():
    stats=[]
    for donor in donors:
        donations = donor[1]
        total = sum(donations)
        num = len(donations)
        stats.append((donor[0], total, num, total / num))
    return stats

def quit():
    print("quitting")
    sys.exit()


def main_menu():
    while True:
        answer = input("""What would you like to do?
Pick one:
1: Send a Thank You
2: Create a Report
3: Quit
>>>""")
        #print(answer)
        clear_screen()
        if answer == "1" or answer.lower() == "send a thank you":
            thank_you()
        elif answer == "2" or answer.lower() == "create a report":
            report()
        elif answer == "3" or answer.lower() == "quit":
            quit()
        else:
            print("Please follow instructions dummy :)","\n")             








if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()