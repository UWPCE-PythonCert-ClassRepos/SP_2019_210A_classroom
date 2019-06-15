#!/usr/bin/env python3

# -----------------------------------------------------------------
# What: Lesson06: mailroom4.py
# Who: Brian Brumleve
# Date: May 19, 2019
# Change Description:
#   Some functions refractored to accomodate
#   testing in test_mailroom4.py
#
# -----------------------------------------------------------------

import sys
from textwrap import dedent
from operator import itemgetter

donor_database = {"Guile": [1000, 589, 25000],
                  "Blanca": [23, 1, 17],
                  "Ken": [1001, 590, 25001],
                  "M. Bison": [15000, 8000, 1200000],
                  "Chun-Li": [61000000, 500000, 1200000]}


def gen_donor():
    """
    generate donors in the database
    :return: a list of donors found in donor_data
    """
    return [donor for donor in donor_database]


def print_donor_list():
    """
    print list of donors in the database
    :return: a printed list of donors found in donor_data
    """
    for donor in donor_database:
        print(str(donor))
    return donor_database.keys()


def add_to_donations():
    """
    provides user new options to add donations to existing donors,
    create new donors or view all donors
    :return: nothing
    """
    sub_menu = 1
    while sub_menu == 1:
        sub_menu = int(input("\n""Select from these menu options:\n"
                             "1 - Print a list of all current donors\n"
                             "2 - Add to a current donor's donations\n"
                             "3 - Enter a new donor and donation.\n"
                             "4 - Return to the Main Menu.\n"
                             ">>>"))
        print("You replied: ", sub_menu)
        sub_menu_dict = {1: print_donor_list,
                         2: prompt_for_donor,
                         3: prompt_for_donor,
                         4: main_menu}
        sub_menu_dict.get(sub_menu, "Please answer 1, 2, 3 or 4")()


#def amend_donor_data():
#    """
#    adds donations to existing donors
#    :return: new donation amounts to donor_data{}
#    """
#    try:
#        donor = input("Which donor would like to add a donation?\n"
#                      ">>>")
#        if donor in donor_database:
#            print(donor, "is found in our database.")
#        amount = int(input("Please enter a new donation amount:\n"
#                           ">>>"))
#        donor_database[donor].append(amount)
#        # print updated donor data
#        print("a peak into the donor database...", donor_database, "\n")
#        print(gen_letter(donor, amount))
#    # throws an exception when the donor cannot be added to the donor list
#    except KeyError:
#        print("key error: please enter an existing donor")
#    #return donor, amount


def prompt_for_donor():
    """Select a donor to update or use"""
    print('Type "list" to see donor list')
    donor_name = input("Which donor? ")
    return select_donor(donor_name)


def select_donor(donor_name):
    """Find or create a donor in the donor set"""
    if donor_name == 'list':
        donor_id = 1
        for donor, donations in donor_database.items():
            print('{:<4}: {:>20} | {:>50}'.format(donor_id, donor, str(donations)))
            donor_id += 1
        print()
        return ''

    for donor, donations in donor_database.items():
        if donor_name.lower() == donor.lower():
            print('Found {}'.format(donor_name))
            return donor, donations

    donor_database[donor_name] = []
    print('{} not found in donor list. Adding...'.format(donor_name))
    return donor_name, donor_database[donor_name]


#def new_donor_data():
#    """
#    creates new donor account with donations
#    :return: adds new {donor: [donations]} to donor_data{}
#    """
#    new_donor = input("Give our new donor a name.\n"
#                      ">>>")
#    print(new_donor, "has been added to our database!")
#    new_amount = int(input("Please enter a donation amount:\n"
#                           ">>>"))
#    # add new donor and new donations to teh donor_data dictionary
#    donor_database[new_donor] = [new_amount]
#    # print updated donor data
#    print("a peak into the donor database...", donor_database, "\n")
#    print(gen_letter(new_donor, new_amount))


def gen_letter(donor: object, amount: object) -> object:
    """
    generates a thank you letter a donor
    :type donor: object
    :param donor: person or entity that donated
    :param amount: the amount of the donation
    :return: a thank you letter to the donor, restating their donation
    """
    return dedent('''Dear {},
        Thank for your donation(s) of ${:,.2f}! We appreciate
        your contribution and without you nothing would
        be possible!

                            Sincerely,
                                Street Fighter, LLC
                                    an equal opportunity
                                    employer'''.format(donor, amount))


def gen_donation_stats():
    stats = []
    try:
        for donor, donations in donor_database.items():
            total = sum(donations)
            num = len(donations)
            average = total / num
            stats.append([donor, total, num, average])
    except ZeroDivisionError:
        print("Learn Math dummy, zero is non-divisible.")
    return stats


def send_letter_to_all():
    """
    generates a letter and saves it to file
    :return: a letter for each donor in donor_data
    """
    stats_list = gen_donation_stats()
    for stats in stats_list:
        letter = gen_letter(stats[0], stats[1])
        filename = stats[0].replace(" ", "_").replace(".", "_") + ".txt"
        with open(filename, "w") as postal:
            print("created a thank you letter for",
                  stats[0], ":", stats[2], "donations totalling",
                  "${:,.2f}".format(stats[1]), "!")
            postal.write(letter)


def sort_stats(donations):
    return sum(donations[1])


def gen_stats_report():
    """
    generates a report of donor stats
    :return: a formatted matrix of donor stats
    """
    stats = gen_donation_stats()
    stats.sort(key=itemgetter(1), reverse=True)
    header = [f"{'Donor':<10}|{'($) Total Donated':>21}|{'Total Donations':>19}"
              f"|{'($) Average Donation':>22}|", "-" * 76]
    for line in stats:
        header.append("{:<10}|{:>21,.2f}|{:>19}|{:>22,.2f}|".format(*line))
    return "\n".join(header)


def print_donor_report():
    print(gen_stats_report())


def quit():
    print("quitting")
    sys.exit()


def main_menu():
    """
    the main menu of the mailroom
    :return: sends the user everywhere to do everything
    """
    while True:
        answer = int(input("\n"
                           "What would you like to do?\n"
                           "Pick One:\n"
                           "1 - Give a donation\n"
                           "2 - Create a Report\n"
                           "3 - Send Thank You's to all donors\n"
                           "4 - Quit\n"
                           ">>> "
                           ))
        print("You replied: ", answer)
        answer_dict = {1: add_to_donations,
                       2: print_donor_report,
                       3: send_letter_to_all,
                       4: quit}
        answer_dict.get(answer, "Please input 1, 2, 3 or 4")()


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    donor_data = donor_database

    main_menu()

