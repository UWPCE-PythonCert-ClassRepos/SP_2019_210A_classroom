#!/usr/bin/env python

from donor_models import Donor, DonorCollection
from operator import itemgetter


def add_donation(): 
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


def add_donor():
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


def list_donors():
    print(donor_collection.donor_list)


def print_thank_you():
    print(find_donor().thank_you_letter)


def write_letters_to_disk():
    for donor in donor_collection.donors:
        with open('thank_you_letter_{}'.format(donor.name), 'w') as thank_you_file:
            thank_you_file.write(donor.thank_you_letter)


######################
# NAVIGATION FUNCTIONS
######################


def donor_management():
    donor_menu_options = {'l': list_donors, 'a': add_donor, '$': add_donation, 't': print_thank_you,
                          'g': write_letters_to_disk}
    user_input = menu_donor()
    donor_menu_options.get(user_input)()


def find_donor():
    while True:
        user_input = str(input("Provide the name of the donor.\n"))
        for donor in donor_collection.donors:
            if donor.name == user_input:
                return donor
        print("Donor {} not found.".format(user_input))


def menu_donor():
    while True:
        user_input = input("l to list donors\na to add donor\n$ to add donation\nt to print thank you message\n"
                           "g to generate thank you letters for all donors\n \n").lower()
        if user_input == 'l' or user_input == 'a' or user_input == '$' or user_input == 't' or user_input == 'g':
            return user_input


def menu_main():
    while True:
        user_input = input("\nq to quit\nr to generate a report\nd to manage donors\n \n").lower()
        if user_input == 'q' or user_input == 'r' or user_input == 'd' or user_input == 'p':
            return user_input


#####################
# MAIN MENU FUNCTIONS
#####################


def main():
    main_menu_options = {'r': report, 'd': donor_management, 'p': populate_default_data, 'q': exit}
    user_input = ''
    while 'q' not in user_input:
        user_input = menu_main()
        main_menu_options.get(user_input)()


def populate_default_data():
    donors = [
        {'Name': 'Alice', 'Donations': ('$10000.00',)},
        {'Name': 'Bob', 'Donations': (200, 1000.00)},
        {'Name': 'Christine', 'Donations': (0,)},
        {'Name': 'Dave', 'Donations': ()},
        {'Name': 'Kim', 'Donations': (50.25, 50.00, 50)}
    ]
    for donor in donors:
        donor_collection.add_donor(donor['Name'], donor['Donations'])


def report():
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