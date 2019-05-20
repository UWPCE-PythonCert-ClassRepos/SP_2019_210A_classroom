#!/usr/bin/env python3.6

'''Lesson 3 - Mailroom Part 1'''


# Importing Systems Module
import sys

# Starter list of existing donors
donors = {'jasneet paramjit': ("jasneet paramjit", [50, 200, 500]), 
'simran kaur': ("simran kaur", [100, 200, 500]), 
'manikaran chandok':("manikaran chandok", [100, 200, 500, 680]),
'manikaran chandok': ("manveen chandok", [10, 200, 65]), 
'sanjam patwalia': ("sanjam patwalia", [200, 50])} 


def find_donor(name):
    key = name.strip().lower()
    return donors.get(key)


def add_donor(name):
    name = name.strip()
    donor = (name, [])
    donors[name.lower()] = donor
    return donor


# Function for storing and thanking a new donor
def new_donor():
    new_donor_name = input("Enter new donors 'Full Name'>>>")
    new_donor_donation = int(input("\nEnter the 'Amount' donated>>>"))
    donor = find_donor(new_donor_name)
    if donor is None:
        donor = add_donor(new_donor_name)
    donor[1].append(new_donor_donation)
    print("\n****New donor information added to list****\n")
    print(
        '''
          Dear {}

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(new_donor_name, new_donor_donation))


# Function for updating record and thanking existing donor
def existing_donor():
    print("List of Existing Donors:\n")
    print(donors.keys(), '\n')
    donor_selection = input("Enter donor full name to store the new donation value>>>")
    donor_donation = int(input("\nEnter the 'Amount' donated>>>"))
    donor = find_donor(donor_selection)
    donor[1].append(donor_donation)
    print("\n****Donation amount has been recorded****\n")
    print(
        '''
              Dear {}

              Thank you for your very kind donation of ${:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
        '''.format(donor_selection, donor_donation))


# Function for sending a thanking you note
def thankyou_email():
    donor_category = input("""Specify if new or pick existing donor from the list
        New Donor: Enter 'new'
        Existing Donor: Enter 'list'
        >>>""")
    donor_category = donor_category.strip().lower()
    print("\nYou selected:", donor_category, "\n")
    if donor_category == "new":
        new_donor()
    elif donor_category == "list":
        existing_donor()
    else:
        print("Select one of the two category!!")


# Function for sorting report by amount
def sort_key(item):
    return item[1]


# Function for generating reporting
def generate_report():
    report_rows = []
    for (name, gifts) in donors.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

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


def gen_letter(donor):
    return ('''Dear {0:s},

          Thank you for your very kind donation of ${1:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def save_letters_to_disk():
    for donor in donors.values():
        letter = gen_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing letter to:", donor[0])
        open(filename, 'w').write(letter)


# Function for quitting the propram
def quit_program():
    print("Program Quit!!")
    sys.exit(0)


def main_menu():
    prompt = ('''
                        Choose an action:

                        (1) - Send a Thank You
                        (2) - Create a Report
                        (3) - Send letters to everyone
                        (4) - Quit

                        > ''')

    selection_dict = {"1": thankyou_email,
                      "2": generate_report,
                      "3": save_letters_to_disk,
                      "4": quit_program}

    run_menu(prompt, selection_dict)


def run_menu(prompt, selection_dict):
    while True:
        selection = input(prompt).strip().lower()
        action = selection_dict.get(selection, None)
        if action is None:
            print("error: menu selection is invalid!")
        else:
            if action():
                break


if __name__ == "__main__":
    print("*****Welcome to the Mailroom Program!!*****\n")

main_menu()
