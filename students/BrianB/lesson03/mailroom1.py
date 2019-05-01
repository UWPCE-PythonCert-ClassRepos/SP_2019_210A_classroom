#!/usr/bin/env python3
from textwrap import dedent

#----------------------------------------------
# What: Lesson03: mailroom.py
# Who: Brian Brumleve
# Date: April 23, 2019
# Program Description:
#
# To take something off the list in iPython:
#  donor[1].pop(1)  Takes the 1 position
#                       from donor 1
#  donor[1].pop()  Leaving pop() blank, deletes
#                       the value in the last
#                       position
#----------------------------------------------

import sys
import math
from textwrap import dedent

print("In the Mailroom")

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


def thank_you():
    while True:
        name = input("Which Donor would you like to see?\n\
    Please enter the full name only.\n\
    >>> ")
        if name == "list":
            for donor in donor_data:
                print(donor[0])
            continue
        for donor in donor_data:
            if name == donor[0]:
                print("There's a match!\n", donor[0])
                new_amt = input("Please enter a donation amount:")
                donor[1].append(float(new_amt))
                # print(donor_data)
                print(dedent('''

                            Dear {}!
                             Thank for your donation of ${:,.2f}! We appreciate
                             your contribution and without you nothing would
                             be possible!

                                                     Sincerely,
                                                        Street Fighter, LLC
                                                            an equal opportunity
                                                            employer
                                '''.format(donor[0], donor[1][-1])))
                break  # this does not break out of [thank =_you()]
        else:
            print(name, ": There's a new donor!")
            amt = input("New donor found! Please enter a donation amount:")
            donor_data.append((name, [float(amt)]))
            print(donor_data)
            # print(gen_letter(donor))
            print(dedent('''

                            Dear {}!
                            Thank for your donation of ${:,.2f}! We appreciate
                            your contribution and without you nothing would
                            be possible!

                                                     Sincerely,
                                                        Street Fighter, LLC
                                                            an equal opportunity
                                                            employer
                                '''.format(name, float(amt))))
            break


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total/num)
    return stats


def gen_letter():
    return dedent('''

                Dear {}!
                     Thank for your donation of {:,.2f}! We appreciate
                     your contribution and without you nothing would
                     be possible!

                                             Sincerely,
                                                Street Fighter, LLC
                                                    an equal opportunity
                                                    employer
                    '''.format(name, float(amt)))
    pass


def sort_key(donor):
    return donor[1][2]


print(sorted(donor_data, key=sort_key))


def report():
    print("in report")


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
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    main_menu()

    donor = ("Barney Rubble", [101, 201, 51])
    assert gen_stats(donor) == ("Barney Rubble", 353, 117.67)

