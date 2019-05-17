#!/usr/bin/env python3
import sys
import math
from textwrap import dedent


def get_donor_db():
    return {"Alpha Beta": ("Alpha Beta", [1000, 250]),
            "Tucker Jones": ("Tucker Jones", [800]),
            "Vladmir Putin": ("Vladmir Putin", [500000, 250000, 750000]),
            "Kim Jong Il":  ("Kim Jong Il", [200]),
            "Tony Robinson": ("Tony Robinson", [500000, 1000000, 750000])}


donor_db = get_donor_db()

def list_donors():
    '''
    Create a list of donors as a string so they can be printed
    Not calling print from here makes it more flexible to test
    '''
    listing = ["Donor list:"]
    for donor in donor_db:
        listing.append(donor)
    return "\n".join(listing)


def print_donor_list():
    '''
    prints each separate
    '''
    print(list_donors(), '\n')


def find_donor(name):
    '''
    Find a donor in donor_db
    :param: the name of the donor
    :returns: the donation (value) data, None if not in donor_db
    '''

    key = name.strip()
    return donor_db.get(key)


def add_donor(name):
    '''
    Add a donor to the donor_db
    :param name of the donor
    :return: the new donor data
    '''

    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor


def gen_letter(donor):
    '''
    generate a thank you letter for the donors
    :param donor: it's a tuple
    :return: string with letter

    This function doesn't actually write to a file -- that's another function.
    '''

    return dedent('''Dear {0:s},
          Thank you for your very kind donation of ${1:.2f}.
          It will be put to very good use.
                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def take_donation():
    ''''
    Ask User for donation amount and add it to donor.db'''
    # prompt the user for a donation amount. Since this is also an
    # exit point to the main menu, we want to make sure this is
    # also done before mutating the database.

    name = input("Enter a donor name (new or existing): \n >")
    while True:
        amount_str = input("Enter a donation amount (Or  <enter> to exit)> ").strip()
        if not amount_str:
            # that is, if no input in provided (<enter>)
            return
        else:
            # make sure amount is valid before leaving the loop
            amount = float(amount_str)
            break

    donor = find_donor(name)
    # if a donor is not found, it's a new donor
    if donor is None:
        # add the new donor to the database
        donor = add_donor(name)

    # record the donation
    donor[1].append(amount)
    # print the thank you letter
    print(gen_letter(donor))


def sort_key(item):
    # used t sort on name in donor_db
    return item[1]


def gen_donor_report():
    '''
    Generate the report of the donors and their donations
    :return: the donor report as a string
    '''
    # Reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gifts = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gifts))

    # sort the report data
    report_rows.sort(key=sort_key)
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
    '''
    make a letter for each donor, save to disk
    '''

    for donor in donor_db.values():
        letter = gen_letter(donor)
        filename = donor[0].replace('','_')+ '.txt'
        print("writing letter to", donor[0])
        open(filename, 'w').write(letter)


def print_donor_report():
    print(gen_donor_report())


def return_to_menu():
    ''' return True to trigger exit out of subloop'''
    return True

def quit():
    """
    quit the program
    Note: you could put the sys.exit call directly in the dict
          but this lets you put extra code in there if you want.
    """
    sys.exit(0)


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
    prompt = dedent('''
                    Choose an action:
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
        action = selection_dict.get(selection, None)
        if action is None:
            print("error: menu selection is invalid!")
        else:
            if action():
                # break out of the loop if action returns True
                break


if __name__ == "__main__":
    main_menu()

