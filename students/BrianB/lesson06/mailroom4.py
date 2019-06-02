#!/usr/bin/env python3

# -----------------------------------------------------------------
# What: Lesson05: mailroom3.py
# Who: Brian Brumleve
# Date: May 17, 2019
# Change Description:
#       Updated mailroom by adding functions to break up
#       add_to_donations() loop (formerly thank_you()). Also
#       incorporating exception loop in amend_donor_data().
#       A comprehension is added in gen_donor_data().
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
    return [donor for donor in donor_data]


def add_to_donations():
    """
    provides user new options to add donations to existing donors,
    create new donors or view all donors
    :return: nothing
    """
    # while True:
    sub_menu = int(input("\n""Select from these menu options:\n"
                         "1 - Print a list of all current donors\n"
                         "2 - Add to a current donor's donations\n"
                         "3 - Enter a new donor and donation.\n"
                         "4 - Return to the Main Menu.\n"
                         ">>>"))
    print("You replied: ", sub_menu)
    # sub_menu = sub_menu.strip()
    # if sub_menu == "1":
    #    print(gen_donor())
    # elif sub_menu == "2":
    #    amend_donor_data()
    # elif sub_menu == "3":
    #    new_donor_data()
    # elif sub_menu == "4":
    #    main_menu()
    # else:
    #    print("Please answer 1, 2, 3 or 4")
    sub_menu_dict = {1: print(gen_donor()),
                     2: amend_donor_data(),
                     3: new_donor_data(),
                     4: main_menu()}
    sub_menu_dict.get(sub_menu, "Please answer 1, 2, 3 or 4")()
    return sub_menu, sub_menu_dict


def amend_donor_data():
    """
    adds donations to existing donors
    :return: new donation amounts to donor_data{}
    """
    try:
        donor = input("Which donor would like to add a donation?\n"
                      ">>>")
        if donor in donor_data:
            print(donor, "is found in our database.")
        amount = int(input("Please enter a new donation amount:\n"
                           ">>>"))
        donor_data[donor].append(amount)
        # print updated donor data
        print("a peak into the donor database...", donor_data, "\n")
        print(gen_letter(donor, amount))
    # throws an exception when the donor cannot be added to the donor list
    except KeyError:
        print("key error: please enter an existing donor")
    return


def new_donor_data():
    """
    creates new donor account with donations
    :return: adds new {donor: [donations]} to donor_data{}
    """
    new_donor = input("Give our new donor a name.\n"
                      ">>>")
    print(new_donor, "has been added to our database!")
    new_amount = int(input("Please enter a donation amount:\n"
                           ">>>"))
    # add new donor and new donations to teh donor_data dictionary
    donor_data[new_donor] = [new_amount]
    # print updated donor data
    print("a peak into the donor database...", donor_data, "\n")
    print(gen_letter(new_donor, new_amount))


def gen_letter(donor, amount):
    """
    generates a thank you letter a donor

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


def gen_donation_stats(**donors_data):
    # opportunity for a function to pull for loop,
    # generating 'total', 'num' and 'average' from
    # gen_stats_report() & send_letter_to_all()
    for donors, donations in donor_data.items():
        donors = donors
        total = sum(donations)
        num = len(donations)
        average = total / num
    return


def send_letter_to_all(total, *donor, **num):
    """
    generates a letter and saves it to file

    :return: a letter for each donor in donor_data
    """
    #for donor, donations in donor_data.items():
    #    total = sum(donations)
    #    num = len(donations)
    total = gen_donation_stats(total)
    letter = gen_letter(donor, sum(donor_data[donor]))
    filename = donor.replace(" ", "_").replace(".", "") + ".txt"
    with open(filename, "w") as postal:
        print("created a thank you letter for",
              gen_donation_stats(donor), ":", gen_donation_stats(num),

              "donations totalling", "${:,.2f}"
              .format(total), "!")
        postal.write(letter)
    return total


def sort_stats(donations):
    return sum(donations[1])


def gen_stats_report(donors, total, num, average):
    """
    generates a report of donor stats

    :return: a formatted matrix of donor stats
    """
    donor_stats = []
    #donor_stats = [(donors, total, num, average)]
    #for donors, donations in donor_data.items():
    #    total = sum(donations)
    #    num = len(donations)
    #    average = total / num
    donor_stats.append((donors, total, num, average))

    donor_stats.sort(key=itemgetter(1), reverse=True)
    header = [
        f"{'Donor':<10}|{'($) Total Donated':>21}|{'Total Donations':>19}"
        f"|{'($) Average Donation':>22}|", "-" * 76
    ]
    for line in donor_stats:
        header.append("{:<10}|{:>21,.2f}|{:>19}|{:>22,.2f}|".format(*line))
        # I want to [header.append] with f-string formatting but I'm
        #   not getting it to work
        # header.append(
        #              f"{donors:<10}|{total:>21,.2f}|{num:>19}|"
        #              f"{average:>22,.2f}|"
        #              )
    return donors, total, num, average, "\n".join(header)


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
    answer_dict = {
                   1: add_to_donations,
                   2: print_donor_report,
                   3: send_letter_to_all,
                   4: quit
                   }
    ##########################################################
    # QUESTION FOR RON: Why does parenthesis after .get work?
    answer_dict.get(answer, "Please input 1, 2, 3 or 4")()
    return answer, answer_dict


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    donor_data = donor_database

    # main_menu()
    # print(gen_donor())
    # thank_you()
    # amend_donor_data()
    # new_donor_data()
    # gen_letter()
    send_letter_to_all()
    # print(gen_stats())
    # sort_stats()
    # gen_report()
