#!/usr/bin/env python

from donor_models import Donor, DonorCollection
from operator import itemgetter

############################
# DONOR MANAGEMENT FUNCTIONS
############################


def add_donation():  # Tested
    """
    Adds a donation to the specified donor.  Prints a thank you letter to stdout.
    :return: None
    """
    donor = find_donor()
    while True:
        donation_input = input("Input {}'s donation amount in dollars\n".format(donor.name))
        try:
            donor.add_donation(donation_input)
            print(donor.thank_you_letter)
            return
        except ValueError:
            print("{} is not a valid donation amount.".format(donation_input))
            continue


def add_donor():  # Tested
    """
    Adds a donor to the donor collection
    :return: None
    """
    donor_valid = False
    while not donor_valid:
        try:
            user_input = str(input("Provide the name to add to the donor list\n"))
        except TypeError:
            continue
        try:
            donor_collection.add_donor(user_input)
            donor_valid = True
        except ValueError:
            print("Donor {} already exists.  Please provide a different donor name to add".format(user_input))
            continue


def list_donors():  # Tested
    """
    Prints a list of donor names to stdout.
    :return: None
    """
    print(donor_collection.donor_list)


def print_thank_you():  # Tested
    """
    Prompts for the name of a donor.  Prints a thank you letter for the donor's mmost recent donation.
    :return: None
    """
    print(find_donor().thank_you_letter)


def write_letters_to_disk():  # Tested
    """
    Writes a text file to disk for each donor in the donor collection.
    Each file contains a thank you letter for the donor's most recent donation.
    :return: None
    """
    for donor in donor_collection.donors:
        with open('thank_you_letter_{}'.format(donor.name), 'w') as thank_you_file:
            thank_you_file.write(donor.thank_you_letter)


######################
# NAVIGATION FUNCTIONS
######################


def donor_management():  # Tested
    """
    Calls a function based on the user's input in the program's donor menu.
    :return: None
    """
    donor_menu_options = {'l': list_donors, 'a': add_donor, '$': add_donation, 't': print_thank_you,
                          'g': write_letters_to_disk}
    user_input = menu_donor()
    donor_menu_options.get(user_input)()


def find_donor():  # Tested
    """
    Prompts user for a donor name.  Locates the corresponding Donor object in the DonorCollection
    :return: Donor object
    """
    while True:
        user_input = str(input("Provide the name of the donor.\n"))
        for donor in donor_collection.donors:
            if donor.name == user_input:
                return donor
        print("Donor {} not found.".format(user_input))


def menu_donor():  # Tested
    """
    Presents user with the donor sub-menu's options.  Validates user input.
    :return: str with one of the following values: l, a, $, t, g
    """
    while True:
        user_input = input("l to list donors\na to add donor\n$ to add donation\nt to print thank you message\n"
                           "g to generate thank you letters for all donors\n \n").lower()
        if user_input == 'l' or user_input == 'a' or user_input == '$' or user_input == 't' or user_input == 'g':
            return user_input


def menu_main():  # Tested
    """
    Prompts user with the program's main menu options.  Validates user input.
    :return: str with one of the following values: q, r, d, p
    """
    while True:
        user_input = input("\nq to quit\nr to generate a report\nd to manage donors\n \n").lower()
        if user_input == 'q' or user_input == 'r' or user_input == 'd' or user_input == 'p':
            return user_input


#####################
# MAIN MENU FUNCTIONS
#####################


def main():  # Tested
    """
    Calls a function based on the user's input in the program's main menu.
    :return: None
    """
    main_menu_options = {'r': report, 'd': donor_management, 'p': populate_default_data, 'q': exit}
    user_input = ''
    while 'q' not in user_input:
        user_input = menu_main()
        main_menu_options.get(user_input)()


def populate_default_data():  # Tested
    """
    Populates donor_collection with various donor objects.  Not listed in menu options.
    :return: None
    """
    # Hard coded data, ewwww...
    donors = [
        {'Name': 'Alice', 'Donations': ('$10000.00',)},
        {'Name': 'Bob', 'Donations': (200, 1000.00)},
        {'Name': 'Christine', 'Donations': (0,)},
        {'Name': 'Dave', 'Donations': ()},
        {'Name': 'Kim', 'Donations': (50.25, 50.00, 50)}
    ]
    for donor in donors:
        donor_collection.add_donor(donor['Name'], donor['Donations'])


def report():  # Tested
    """
    Prints a table to stdout containing donor statistics.
    :return: None
    """
    sorted_donor_data = sorted(donor_collection.donor_report, key=itemgetter(1), reverse=True)
    print("Donor Name{}| Total Given | Num Gifts | Average Gift".format(' ' * 20))
    print('-' * 70)
    for donor in sorted_donor_data:
        total_str = '{:,.2f}'.format(donor[1])
        average_str = '{:,.2f}'.format(donor[3])
        print("{name}{w1}${w2}{t}{w3}{num}  ${w4}{a}".format(
            name=donor[0],
            w1=' ' * (31 - len(str(donor[0]))),
            w2=' ' * (12 - len(total_str)),
            t=total_str,
            w3=' ' * (12 - len(str(donor[2]))),
            num=donor[2],
            w4=' ' * (11 - len(average_str)),
            a=average_str
        ))


donor_collection = DonorCollection()
if __name__ == '__main__':
    main()
