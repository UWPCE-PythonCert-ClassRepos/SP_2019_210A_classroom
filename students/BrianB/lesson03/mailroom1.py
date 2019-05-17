#!/usr/bin/env python3

# ----------------------------------------------
# What: Lesson03: mailroom.py
# Who: Brian Brumleve
# Date: April 23, 2019
# Change Description:
#       Updated with Mailroom#1 requirements.
#
# ----------------------------------------------

import sys
import math
from textwrap import dedent

#print("In the Mailroom")

# convert lists to a dictionary - see Assignment 05, ToDo.py

# A tuple of donor and listing of past donations
# You want a tuple to keep a record of past donations. The original
# tuple stays in as assigned memory location.
donor_data = [("Guile", [1000, 589, 25000]),
              ("Blanca", [23, 1, 17]),
              ("Ken", [1001, 590, 25001]),
              ("M. Bison", [15000, 8000, 1200000]),
              ("Chun-Li", [61000000, 500000, 1200000]),
              ]


def gen_donor():
    # print("The Donors Are:")
    for donor in donor_data:
        print(donor[0])


def thank_you():
    while True:
        donor = input("Which Donor would you like to see?\n"
                      "Please enter the full name only.\n"
                      ">>> ")
        if donor == "list":
            gen_donor()
            continue
        if donor in donor_data:
            print(donor, "was found in our database!")
            amount = int(input("Please enter a new donation amount:"))
            donor[1].append(amount)
            print(donor_data)
            break
        if donor not in donor_data:
            print(donor, ": There's a new donor!")
            amount = int(input("Please enter a donation amount:"))
            donor_data.append((donor, ([amount])))
            print(donor_data)
            break

    print(gen_letter(donor, amount))


def gen_letter(donor, amount):
    return dedent('''
                Dear {},
                    Thank for your donation of {:,.2f}! We appreciate
                    your contribution and without you nothing would
                    be possible!

                                        Sincerely,
                                            Street Fighter, LLC
                                                an equal opportunity
                                                employer
                '''.format(donor, amount))


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    return "{:<10}|{:>26,.2f}|{:>19,}|{:>22,.2f}|".format(donor[0],
                                                       total,
                                                       num,
                                                       total/num
                                                       )


def sort_stats(items):
    return sum(items[1])


def gen_report():
    donor_data.sort(key=sort_stats, reverse=True)
    header = "{:<10}|{:>26}|{:>19}|{:>22}|".format("Donor",
                                                   "Total Donated ($)",
                                                   "Total Donations",
                                                   "Average Donation ($)"
                                                   )
    print(header),
    print("-"*83),
    for items in donor_data:
        print(gen_stats(items))


def quit():
    print("quitting")
    sys.exit()


def main_menu():

    while True:
        answer = input(("What would you like to do?\n"
                        "Pick One:\n"
                        "1 - Send a Thank You\n"
                        "2 - Create a Report\n"
                        "3 - Quit\n"
                        ">>> "))
        print("you replied:", answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            gen_report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    main_menu()
