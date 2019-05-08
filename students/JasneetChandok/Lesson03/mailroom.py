#!/usr/bin/env python3.6

'''Lesson 3 - Mailroom Part 1'''


# Importing Systems Module
import sys

# Starter list of existing donors
donors = [("jasneet paramjit", [50, 200, 500]), 
("simran kaur", [100, 200, 500]), 
("manikaran chandok", [100, 200, 500, 680]),
("manveen chandok", [10, 200, 65]), 
("sanjam patwalia", [200, 50])] 


# Function for storing and thanking a new donor
def new_donor():
    new_donor_name = input("Enter new donors 'Full Name'>>>")
    new_donor_donation = int(input("\nEnter the 'Amount' donated>>>"))
    donors.append((new_donor_name.lower(), [new_donor_donation]))
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
    fmt_donor = "\n".join(["{}"] * len(donors)).format(*(donor[0] for donor in donors))
    print("List of Existing Donors:\n", fmt_donor, "\n")
    donor_selection = input("Enter donor full name to store the new donation value>>>")
    donor_donation = int(input("\nEnter the 'Amount' donated>>>"))
    if donor_selection.strip().lower() == donors[0][0]:
        donors[0][1].append(donor_donation)
        print("\n****Donation amount has been recorded****\n")
        print(
            '''
              Dear {}

              Thank you for your very kind donation of ${:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(donor_selection, donor_donation))
    else:
        print("Enter correct name")


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
    for (name, gifts) in donors:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=sort_key)
    # print it out in with a nice format.
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)
    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))


# Function for quitting the propram
def quit_program():
    print("Program Quit!!")
    sys.exit(0)


def main_menu():
    while True:
        answer = input("""\nWhich option from the menu below would you like to do?
    Option 1: Send a thank you email
    Option 2: Create a report of donors
    Option 3: Quit the program
    >>>""")
        answer = answer.strip().lower()
        print("\nYou choose option:", answer, "\n")
        if answer == "1":
            thankyou_email()
        elif answer == "2":
            generate_report()
        elif answer == "3":
            quit_program()
        else:
            print("Please select either 1,2 or 3")


if __name__ == "__main__":
    print("*****Welcome to the Mailroom Program!!*****\n")

main_menu()
