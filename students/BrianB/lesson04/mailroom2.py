#!/usr/bin/env python3

# ----------------------------------------------
# What: Lesson04: mailroom2.py
# Who: Brian Brumleve
# Date: May 10, 2019
# Change Description:
#       Updated with Mailroom#2 requirements,
#       dictionaries are added.
#
# ----------------------------------------------

import sys
import math
from textwrap import dedent

# print("In the Mailroom")


def gen_donor():
    return [donor for donor in donor_data.keys()]


def thank_you():
    while True:
        donor = input("Which Donor would you like to see?\n"
                      "Please enter the full name only.\n"
                      ">>> "
                      )
        # print list of existing donor data
        if donor == "list":
            print(gen_donor())
            continue
        # enter existing donor data
        if donor in donor_data:
            print(donor, "was found in our database!")
            amount = int(input("Please enter a new donation amount:"))
            donor_data[donor].append(amount)
            # print updated donor data
            print(donor_data)
            break
        # enter new donor data
        if donor not in donor_data:
            print(donor, ": There's a new donor!")
            amount = int(input("Please enter a donation amount:"))
            donor_data[donor] = [amount]
            # print updated donor data
            print(donor_data)
            break

    print(gen_letter(donor, amount))


def gen_letter(donor, amount):
    return dedent('''Dear {},
        Thank for your donation(s) of ${:,.2f}! We appreciate
        your contribution and without you nothing would
        be possible!
        
                            Sincerely,
                                Street Fighter, LLC
                                    an equal opportunity
                                    employer'''.format(donor, amount))


def send_letter_to_all():
    for donor in donor_data:
        letter = gen_letter(donor, sum(donor_data[donor]))
        filename = donor.replace(" ", "_").replace(".", "") + ".txt"
        with open(filename, 'w') as postal:
            print('created a thank you letter for ', donor, donor_data[donor])
            postal.write(letter)


def gen_stats(items):
    #donations = sum(donor_data.items[1])
    total = sum(items[1])
    num = len(items[1])
    average = total/num
    return "{:<10}|{:>26,.2f}|{:>19,}|{:>22,.2f}|".format(items[0],
                                                          total,
                                                          num,
                                                          average
                                                          )


def sort_stats(donations):
    return sum(donations)


def gen_report():
    # donor_data.sort(key=sort_stats, reverse=True)
    header = "{:<10}|{:>26}|{:>19}|{:>22}|".format("Donor",
                                                   "Total Donated ($)",
                                                   "Total Donations",
                                                   "Average Donation ($)"
                                                   )
    print(header),
    print("-"*81),
    for donor in donor_data.items():
        items = gen_stats(donor, donor_data[donor])
        total, num, average = gen_stats(donations=donations)
        print(gen_stats(items))


def quit():
    print("quitting")
    sys.exit()


def main_menu():

    while True:
        answer = input(("What would you like to do?\n"
                        "Pick One:\n"
                        "1 - Send a Thank You to a single donor\n"
                        "2 - Create a Report\n"
                        "3 - Send letters to all donors\n"
                        "4 - Quit\n"
                        ">>> "))
        print("you replied:", answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            gen_report()
        elif answer == "3":
            send_letter_to_all()
        elif answer == "4":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    donor_data = {"Guile": [1000, 589, 25000],
                  "Blanca": [23, 1, 17],
                  "Ken": [1001, 590, 25001],
                  "M. Bison": [15000, 8000, 1200000],
                  "Chun-Li": [61000000, 500000, 1200000],
                  }

    main_menu()
    #print(gen_donor())
    #thank_you()
    #gen_letter()
    #send_letter_to_all()
    #gen_stats()
    #sort_stats()
    #gen_report()

