#!/usr/bin/env python3.7
#Mailroom Part2
#FredBallyns
#Session04

import sys
import os

donors = {"Fred Flintstone": [100, 200, 50],
        "James Bond": [0,0,7],
        "Lex Luthor": [5000,],
        "Harambe": [3, 2, 1],
        "Herman Cain": [9, 9, 9]
		}

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
        for i in donors.keys():
            print(i)
        print('\n')
    else:
        # Add new donation
        donation = int(input("Enter donation amount: "))
        # Search if repeat donor
        onlist = False
        for i in donors.keys():
            if i.lower() == donor.lower():
                donors[i].append(donation)
                onlist = True
        # Add first time donor
        if onlist == False:
            donors[donor] = [donation]
        print("donors",'\n','------------\n',donors)
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
    for donor in donors.keys():
        donations = donors[donor]
        total = sum(donations)
        num = len(donations)
        stats.append((donor, total, num, total / num))
    return stats


def send_letters():
    print(os.getcwd())
    letter_template = "Dear {},\n \n Thank you for your very kind donation of ${:.2f}. It will be put to very good use.\n \n Sincerely,\n  -The Team"
    for donor in donors.keys():
        with open((os.getcwd() + "/" + "{}.txt").format(donor), 'w') as new_letter:
            new_letter.write(letter_template.format(donor, sum(donors[donor])))
            new_letter.close()


def quit_program():
    print("quitting")
    sys.exit()


def main_menu():
    while True:
        answer = input("""What would you like to do?
Pick one:
1: Send a Thank You
2: Create a Report
3: Send letters to all donors
4: Quit
>>>""")
        #print(answer)
        clear_screen()
        if answer == "1" or answer.lower() == "send a thank you":
            thank_you()
        elif answer == "2" or answer.lower() == "create a report":
            report()
        elif answer == "3" or answer.lower() == "send letters to all donors":
            send_letters()
        elif answer == "4" or answer.lower() == "quit":
            quit_program()
        else:
            print("Please follow instructions dummy :)","\n")             








if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()