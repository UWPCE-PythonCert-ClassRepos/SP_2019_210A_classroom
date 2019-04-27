#!/usr/bin/env python

import sys
import os

main_donors = [("Luke Skywalker", [100, 200, 50]),
          ("Han Solo", [100, 50, 600]),
          ("Yoda", [1000, 50, 600, 200]),
          ("Ben Kenobe", [10, 5, 6]),
          ]

def clear_screen():
    """
    clears the command screen
    """
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    """
    Main menu options
    """
    prompt = input("\n".join(("\nWelcome to the Mailroom!",
"Please choose from one of the options below:\n",
"1: Send a Thank You",
"2: Create a Report",
"3: Quit",
">>>")))
    return prompt

def menu_thank_you():
    """
    Menu to user to enter options for thank you
    """
    print("""\nTo whom would you like to send a Thank You?
Please enter full name""")
    thanks_answer = input("""
Enter 'LIST' to see Donor list or 'MENU' to return to Main Menu.
>>> """)
    return thanks_answer

# def search_donor(thanks_answer):
#     donor = thanks_answer
#     show_donor = []
#     for x in range(len(donors)-1, -1, -1):
#         if donors[x][0].lower() == donor.lower():
#             show_donor.append(donors[x])
#             print("\n{}\n".format(show_donor[0]))
#         else:
#             add_doner = (donor,[])
#             donors.append(add_doner)
#             print("done adding_doner")
#             print(donors)

def send_thank_you():
    """
    Either adds to list or adds a new donor to the list and  a 
    new donation amount 
    """
    donation_amount = None
    while True:
        thanks_answer = menu_thank_you()
        thanks_answer = thanks_answer.strip()
        if thanks_answer.upper() == "LIST":
            clear_screen()
            show_list()
        elif thanks_answer.upper() == "MENU":
            clear_screen()
            break
        else:
            idx = len(main_donors)-1
            in_main_donors = False
            for x in range(len(main_donors)-1, -1, -1):
                if main_donors[x][0].lower() == thanks_answer.lower():
                    in_main_donors = True
                    print("\nYou have chosen {}".format(thanks_answer))
                    donation_amount = int(input("\nPlease enter the amount that {} kindly donated: ".format(thanks_answer)))
                    main_donors[idx][1].append(donation_amount)
                    print(main_donors)
                idx -= 1
            
            if in_main_donors == False:
                donation_amount = int(input("\nPlease enter {}'s donated amount: ".format(thanks_answer)))
                add_new_donors = (thanks_answer,[donation_amount])
                main_donors.append(add_new_donors)
                print(main_donors[-1][:])
            
            send_email(thanks_answer, donation_amount)

def send_email(name, amount):
    print("""\n
    Dear {n},
       Thank you for your generous donation of ${a}! This will help our cause
       immensely in our battle against the darkside.  You, {n} , have made a big 
       difference in our efforts and we greatly appreciate you!!!  Your ${a} will be 
       put to great use to our forces against evil!  

       Thank you,

       The FORCE
    
    \n""".format(n = name, a = amount))


def show_list():
    print()
    print("#" * 9, "The Current Donor List", "#" * 9)
    index = 1
    for donor in main_donors:
        print("{}:{}".format(index, donor[0]))
        index += 1
    print("#" * 43)
    print()
    return show_list

def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num)

    return stats

def report():
    print("in report")

def quit():
    print("You are leaving the Mailroom!")
    sys.exit()


    


def mailroom_main():

    while True:
        answer = main_menu()
        # print("you replied:", answer)
        answer = answer.strip()
        if answer == "1":
            clear_screen()
            send_thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please choose a number 1-3")


if __name__ == "__main__":
    

    # donor = ('Barney Rubble', [100, 50, 600])
    # assert gen_stats(donor) == ('Barney Rubble', 750, 3, 250.0), str(gen_stats(donor))

    mailroom_main()
