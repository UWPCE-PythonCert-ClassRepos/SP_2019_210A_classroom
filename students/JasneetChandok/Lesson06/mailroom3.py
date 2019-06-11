#!/usr/bin/env python3.6

'''
Lesson 6: Mailroom Part 3 Unit Test

Problem Statement: You work in the mail room at a local charity.\
Part of your job is to write incredibly boring, repetitive emails \
thanking your donors for their generous gifts. You are tired of \
doing this over and over again, so you’ve decided to let Python \
help you out of a jam and do your work for you.

Written By: Jasneet Chandok

Last Modified Date: 5/22/2019
'''

# Importing Systems Module
try:
    import sys
except ImportError:
    print("The sys module could nout be imported!")


def get_donors_db():
    # List of existing donors
    return {'jasneet paramjit': [50, 200, 500],
            'simran kaur': [100, 200, 500],
            'manikaran chandok': [100, 200, 500, 680],
            'manveen chandok': [10, 200, 65],
            'harjeev anand': [200, 50]}


# List of existing donor
def existingdonors_list():
    donor_list = ["\nList of Existing Donors:"]
    for donor in donors_db.keys():
        donor_list.append(donor.title())
    return "\n".join(donor_list)


def print_donor_list():
    print(existingdonors_list())


# Add donation to an existing donor
def add_donation():
    try:
        donor_selection = input("\nEnter 'Full Name' of the donor >")
        donor_donation = input("\nEnter the 'Amount' donated >")
        donor = donor_selection.strip().lower()
        try:
            if donor in donors_db:
                donor_amount = donors_db.get(donor)
                donor_amount.append(float(donor_donation))
                print(f'\nDonation amount of "{donor_donation}" has been recorded for {donor.title()}!!\n')
                print('''Thank you note to share out with the donor below:\n
                  Dear {}

                  Thank you for your very kind donation of ${:.2f}.
                  It will be put to very good use.

                                 Sincerely,
                                    -The Team
                    '''.format(donor.title(), float(donor_donation)))
            else:
                print('\nDonor name entered does not exist in the list!!')
        except ValueError:
            print("A value error occured")
    except (EOFError, KeyboardInterrupt):
        print("""\nA user induced error occured. Please check keys pressed!""")


# Create a record for a new donor
def new_donor():
    try:
        donor_name = input("\nEnter 'Full Name' of the donor >")
        new_donation = float(input("\nEnter the 'Amount' donated >"))
        donor_name = donor_name.strip().lower()
        try:
            if donor_name not in donors_db:
                donors_db[donor_name] = [new_donation]
                print(f'\nDonation amount of "{new_donation}" has been recorded for {donor_name.title()}!!\n')
                print('''Thank you note to share out with the donor below:\n
                  Dear {}

                  Thank you for your very kind donation of ${:.2f}.
                  It will be put to very good use.

                                 Sincerely,
                                    -The Team
                    '''.format(donor_name.title(), new_donation))
            else:
                print("\nDonor already exists in the list!!")
        except ValueError:
            print("A value error occured")
    except (EOFError, KeyboardInterrupt):
        print("""\nA user induced error occured. Please check keys pressed!""")


# Function for sending a thanking you note
def thankyou_email():
        prompt = ('''
                  Choose an action number:

                  (1) - List existing donors
                  (2) - Existing donor new donation amount
                  (3) - Add a new donor and donation amount
                  (4) - Return to main menu
                  (5) - Quit

                  > ''')

        selection_dict = {"1": print_donor_list,  # existingdonors_list
                          "2": add_donation,
                          "3": new_donor,
                          "4": main_menu,
                          "5": quit_program}

        run_menu(prompt, selection_dict)


# Function for sorting report by amount
def sort_key(item):
    return item[1]


# Function for generating reporting
def generate_report():
    report_rows = []
    for donor, donation in donors_db.items():
        total_donation = sum(donation)
        num_donation = len(donation)
        avg_donation = total_donation / num_donation
        report_rows.append((donor.title(), total_donation, num_donation, avg_donation))

    # sort the report data
    report_rows.sort(key=sort_key, reverse=True)
    report = []
    report.append("{:20s} | {:11s} | {:9s} | {:12s}".format("\nDonor Name",
                                                            "Total Donation",
                                                            "Num Donation",
                                                            "Avg Donation"))
    report.append("-" * 70)

# print the report
    for row in report_rows:
        report.append("{:20s}   {:10.2f}$   {:9d}   {:13.2f}$".format(*row))
    return"\n".join(report)


def display_report():
    print(generate_report())


def gen_letter(donor):  # letter needs to be fixed
    return ('''Dear {:s},

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor.title(), donors_db[donor][-1]))


def save_letters_to_disk():
    for donor in donors_db:
        letter = gen_letter(donor)
        filename = donor.replace(" ", "_") + ".txt"
        print("Generated letter for:", donor.title())
        open(filename, 'w').write(letter)


# Function for quitting the propram
def quit_program():
    print("Program Quit!!")
    sys.exit(0)


# Function with main menu options
def main_menu():
    prompt = ('''
                        Choose an action number:

                        (1) - Send a thank you note
                        (2) - Create a report
                        (3) - Send letters to everyone
                        (4) - Quit

                        > ''')

    selection_dict = {"1": thankyou_email,
                      "2": display_report,  # generate_report,
                      "3": save_letters_to_disk,
                      "4": quit_program}

    run_menu(prompt, selection_dict)


# Function to enabling the main menu option
def run_menu(prompt, selection_dict):
    while True:
        selection = input(prompt).strip().lower()
        action = selection_dict.get(selection, None)
        if action is None:
            print("Error: menu selection is invalid!")
        else:
            if action():
                break


# Runs the file as a main module
if __name__ == "__main__":
    print("\n*****Welcome to the Mailroom Program!!*****\n")
donors_db = get_donors_db()
main_menu()
