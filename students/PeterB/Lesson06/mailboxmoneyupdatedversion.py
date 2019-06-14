#!/usr/bin/env python

import sys
import math
from operator import itemgetter

# handy utility to make pretty printing easier
from textwrap import dedent

# questions in-line


def get_donor_db():
    return {'road runner': ("Road Runner", [4839283.32, 17842102.94]),
            'shawn michaels': ("Shawn Michaels", [55303.04, 5000.08, 300.03]),
            'sasuke uchiha': ("Sasuke Uchiha", [80040033.32]),
            'frieza': ("Frieza", [0.50, 1.75, 2000.25]),
            }

# how do you know to name the value ["Donor List:"]
def list_donors():
    listing = ["Donor List:"]
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)

def print_donor_list():
    print(list_donors())
    print()


def find_donor(name):
    key = name.strip().lower()
    return donor_db.get(key)


def add_donor(name):
    """
    Add a new donor to the donor db

    :param: the name of the donor
    :returns: the new Donor data structure
    """
    #  why does donor redefine?
    #  first donor is donor = (name, [])
    #  then donor is redefined as donor_db[name.lower()] = donor

    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor


def gen_letter(donor):
    # explain donor[1][-1]
    return dedent('''Dear {0:s},

          Thank you for your very kind donation of ${1:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def take_donation():
    """
    Ask user for donation amount, and then add it  to the DB
    """
    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.


    # why is print statement first call?
    print("in take_donation")
    name = input("Enter a donor name (new or existing): \n >")
    while True:
        amount_str = input("Enter a donation amount (or <enter> to exit)> ").strip()
        if not amount_str:
            # if they provide no input, go back to previous menu
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("error: donation amount is invalid\n")
            continue
        else:
            break

    donor = find_donor(name)
    # If the donor is not found, it's a new donor
    if donor is None:
        # add the new donor to the database
        donor = add_donor(name)

    # Record the donation
    donor[1].append(amount)
    # print the thank you letter
    print(gen_letter(donor))


def sort_key(item):
    # used to sort on name in donor_db
    return item[1]


def generate_donor_report():
    """
    Generate the report of the donors and amounts donated.

    :returns: the donor report as a string.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data

    # need help understanding the report.append() call
    report_rows.sort(key=itemgetter(1), reverse=True)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)


def save_letters_to_disk():
    """
    make a letter for each donor, and save it to disk.
    """
    # how does this find the txt file in your local?
    for donor in donor_db.values():
        letter = gen_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing letter to:", donor[0])
        open(filename, 'w').write(letter)


def print_donor_report():
    print(generate_donor_report())


def return_to_menu():
    ''' Return True to trigger exit out of sub-loop'''
    return True


def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    prompt = ("To send a thank you, select one:\n\n"
              "(1) Update donor and send thank-you\n"
              "(2) List all existing DONORS\n"
              "(3) Return to main menu\n > ")
    selection_dict = {"1": take_donation,
                      "2": print_donor_list,
                      "3": return_to_menu,
                      }
    run_menu(prompt, selection_dict)

def main_menu():
    """
    Run the main menu for mailroom
    """
    # what does dedent mean ?
    prompt = dedent('''
                    Choose ,an action:

                    (1) - Send a Thank You
                    (2) - Create a Report
                    (3) - Send letters to everyone
                    (4) - Quit

                    > ''')

    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": save_letters_to_disk,
                      "4": quit}

    run_menu(prompt, selection_dict)


def run_menu(prompt, selection_dict):
    """
    run an interactive menu

    :param prompt: What you want to ask the user

    :param selection_dict: Dict of possible user impots mapped to
                           the actions to take.
    """
    while True:
        selection = input(prompt).strip().lower()
        try:
            if selection_dict[selection]():
                # break out of the loop if action returns True
                break
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    donor_db = get_donor_db()
    main_menu()
