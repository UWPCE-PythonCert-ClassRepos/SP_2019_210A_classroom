#!/usr/bin/env python3
import sys
import os
import tempfile
from textwrap import dedent

import math
from operator import itemgetter

#donations[]
#donors {donor1:donations1, donor2:donations2}
donors = {}
# The data struction used in this program, a list of tuples
def get_donors():
    """ Initializer of the dictionary containing informations of donors """
    return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
            'jeff bezos': ("Jeff Bezos", [877.33]),
            'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
            'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            }

def find_donor(name):
    """ Find the donor regardless of upper/lower cases and ignores extra spaces """
    key = name.strip().lower()
    return donors.get(key)

def add_donor(name):
    """ Adds a new donor """
    name = name.strip()
    donor = (name, [])
    donors[name.lower()] = donor
    return donor

def list_donors():
    """
    Create a list of the donors as a string, so they can be printed

    Not calling print from here makes it more flexible and easier to
    test
    """
    listing = ["Donor list:"]
    for donor in donors.values():
        listing.append(donor[0])
    return "\n".join(listing)

def add_donation(name, donation):
    """ Adds a donation to an existing donor """
    donors[name.strip().lower()][1].append(donation)
    return

def generate_donor_report():
    """ Make a report on donations received by a style as specified """
    sorted_donors = sorted(donors.items(), reverse = True, key = lambda item: (sum(item[1][1])))
    report_rows = ["{0:25s}   {1:10.2f}   {2:9d}   {3:11.2f}".format(*gen_stats(donor)) for donor in sorted_donors]
    report = []

    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)

    for row in report_rows:
        report.append(row)
    return "\n".join(report)


def gen_stats(donor):
    """ A function calculates the total and average donation of a donor """
    name = donor[0]
    donations = donor[1]
    total = round(sum(donations[1]),2)
    num_gifts = len(donations)
    avg = round((total / num_gifts), 2)
    return (name, total, num_gifts, avg)


def gen_letter(donor):
    return dedent('''Dear {0:s},

          Thank you for your very kind donation of ${1:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))

def thank_you():
    """ Thank-you funcion that generates an email to thank new donations """
    while True:
        answer = input("Please type the Full Name, type quit to go back to previous menu> ")
        if answer == 'list':
            for donor in donors:
                print(donor)
        elif answer == 'quit':
            return
        elif answer.strip().lower() in donors:
            name = answer
            new_user = False
            break
        else:
            name = answer
            new_user = True
            break

    while True:
        amount = input("How much have you just donated? > ")
        if amount == 'quit': return
        try:
            num_donation = float(amount)
        except:
            print("Please type a float number")
        else:
            if new_user:
                add_donor(name)
                add_donation(name, num_donation)
            else:
                add_donation(name, num_donation)
            break
    gen_letter(donors[name])

    return

def save_letters_to_disk():
    temp_path = os.getcwd()

    for name, donations in donors.items():
        with open('{}/{}.txt'.format(temp_path, name), 'w') as f:
            num_donation = sum(donations[1])
            greetings = 'Dear {},\n'.format(name)
            body = '\nThank you for your generous gift ${} to us!\n'.format(num_donation)
            ending = '\nSincerely,\n  ABC foundations'
            f.write(greetings + body + ending)
    return

def main_menu():
    """ Main menu function """
    while True:
        answer = input("""What would you like to do?
Pick one:
1: Send a Thank you
2: Create a report
3: Send letters to all donors
4: Quit
""")
        print("You replied:", answer)
        answer = answer.strip()
        if answer == '1':
            thank_you()
        elif answer == '2':
            print(generate_donor_report())
        elif answer == '3':
            save_letters_to_disk()
        elif answer == '4':
            sys.exit(0)
        else:
            print("please answer 1, 2 or 3")

if __name__ == '__main__':
    donors = get_donors()
    print("Welcome to the mailroom!")
    main_menu()
