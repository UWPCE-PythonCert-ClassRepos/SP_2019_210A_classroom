#! /usr/bin/env python3
"""
The Mailroom Program : Part 2
Author : Joe Nunnelley
Description:
    Write a small command-line script called mailroom.py. This script should be executable.
    The script should accomplish the following goals:
    - It should have a data structure that holds a list of your donors and a history of
      the amounts they have donated. This structure should be populated at first with
      at least five donors, with between 1 and 3 donations each. You can store that
      data structure in the global namespace.
    - The script should prompt the user (you) to choose from a menu of 3 actions:
      “Send a Thank You”, “Create a Report” or “quit”.

      Update your mailroom program to:

        Use dicts where appropriate.
        See if you can use a dict to switch between the user’s selections.
        See if you can use a dict to switch between the users selections.
        see Using a Dictionary to switch for what this means.
        Convert your main donor data structure to be a dict.
        Try to use a dict and the .format() method to produce the letter as one big
        template, rather than building up a big string that produces the letter in parts.
"""
import datetime
import os
import sys
import tempfile


DONOR_SET = {"George Jetson": [100.00, 50.00, 200.00],
             "Bugs Bunny": [400.00, 55.00, 5000.00],
             "Daffy Duck": [0.00, 3.00, 5.00, 6.00, 76.00, 8.00],
             "Elmer Fudd": [66.00, 666.00, 6666.00, 6666.00, 66666.00],
             "Porky Pig": [0.50, 56.45, 67.89]}

BOUNDARY = '#####'

UI_MENU = {'Main':  """
        What would you like to do?
        Pick one:
            1.) Send a Thank You to a single donor.
            2.) Create a Report
            3.) Send letters to all donors.
            4.) Quit
        >
        """,
           'Directory Select': "Directory? ",}

def send_thankyou():
    """
    Send a Thank You

        If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
            - If the user types list show them a list of the donor names and re-prompt.
            - If the user types a name not in the list, add that name to the data
              structure and use it.
            - If the user types a name in the list, use it.
        Once a name has been selected, prompt for a donation amount.
            - Convert the amount into a number; it is OK at this point for the program
              to crash if someone types a bogus amount.
            - Add that amount to the donation history of the selected user.
        Finally, use string formatting to compose an email thanking the donor for
        their generous donation.

        Print the email to the terminal and return to the original prompt.

    It is fine (for now) for the program not to store the names of the new
    donors that had been added, in other words, to forget new donors once
    the script quits running.
    """
    donor = select_donor()

    if donor:
        added_donations = add_donations()

        for donor_name, donations in DONOR_SET.items():
            if donor_name == donor[0]:
                donations.extend(added_donations)

        print(f'\nSending a Thank You to {donor[0]}...\n')
        formulate_mail(donor)
        print()
    print()


def sort_by_donation_total(item):
    """
    This function is used to sort a list based on a specific key
    """
    return item[1]


def print_report():
    """
    Create a Report

        If the user (you) selected “Create a Report,” print a list of your donors,
        sorted by total historical donation amount.
            - Include Donor Name, total donated, number of donations, and average
              donation amount as values in each row. You do not need to print out
              all of each donor’s donations, just the summary info.
            - Using string formatting, format the output rows as nicely as possible.
              The end result should be tabular (values in each column should align
              with those above and below).
            - After printing this report, return to the original prompt.
        At any point, the user should be able to quit their current task and return
        to the original prompt.

        From the original prompt, the user should be able to quit the script cleanly.

        Your report should look something like this:

        Donor Name                | Total Given | Num Gifts | Average Gift
        ------------------------------------------------------------------
        William Gates, III         $  653784.49           2  $   326892.24
        Mark Zuckerberg            $   16396.10           3  $     5465.37
        Jeff Bezos                 $     877.33           1  $      877.33
        Paul Allen                 $     708.42           3  $      236.14
    """
    print('\nPrinting Report...\n')
    header_format = '{:<24}|{:^14}|{:^12}|{:>13}'
    row_format = '{:<24} ${:>13.2f} {:>12} ${:>13.2f}'
    print(header_format.format('Donor Name',
                               'Total Given',
                               'Num Gifts',
                               'Average Gift'))
    print('-' * 68)
    row_list = []
    for donor, donations in DONOR_SET.items():
        donation_count = len(donations)
        summed_donations = 0

        if donation_count:
            for donation in donations:
                summed_donations += donation

            average_donations = summed_donations / donation_count
            row = [donor,
                   summed_donations,
                   donation_count,
                   average_donations]
            row_list.append(row)

    row_list.sort(key=sort_by_donation_total, reverse=True)

    for row in row_list:
        print(row_format.format(row[0],
                                row[1],
                                row[2],
                                row[3]))

    print('-' * 68)
    print()
    print()


def quit_program():
    """Quit the program and return success"""
    print('Mailroom Closing...')
    print()
    sys.exit(0)


def formulate_mail(donor_in, echo_terminal=True):
    """Send our donor a thank you mail"""
    message = {}
    message['Recipient'] = donor_in[0]
    message['Sender'] = 'Charitable Foundation'
    message['Date'] = "{}".format(datetime.datetime.now())
    message['Title'] = 'Thank you {Recipient} for your recent ' \
                       'donation to {Sender}'.format(**message)
    donations = ''
    for donation in donor_in[1]:
        donations += ('- {:>10.2f} USD\n'.format(donation))

    message['Donations'] = donations

    message['Body'] = "Dear {Recipient},\n\n" \
           "Thank you for your recent donations. " \
           "As you know, every donation helps our mission. We are very grateful.\n\n" \
           "Your donation history:\n\n{Donations}\n\nRegards,\n\n{Sender}".format(**message)

    final_message = "Attn: {Recipient}\nFrom: {Sender}\nDate: " \
                    "{Date}\nSubject: {Title}\n\n{Body}".format(**message)

    if echo_terminal:
        print(BOUNDARY)
        print(final_message)
        print(BOUNDARY)

    return final_message


def add_donations():
    """Add donations to a user's record"""
    done = False
    donations = []
    while not done:
        print('Type "done" to finish')
        response = input('Donation Amount (USD): ')

        if response == 'done':
            done = True
        else:
            if response.isdigit() and float(response) > 0:
                donations.append(float(response))
            else:
                print('Not a number. Please input positive ' \
                      'numbers or "done"')

    print(donations)
    return donations


def select_donor():
    """Select a donor to update or use"""
    print('Type "list" to see donor list')
    donor_name = input("Which donor? ")

    if donor_name == 'list':
        donor_id = 1
        for donor, donations in DONOR_SET.items():
            print('{:<4}: {:>20} | {:>50}'.format(donor_id, donor, str(donations)))
            donor_id += 1
        print()
    else:
        for donor, donations in DONOR_SET.items():
            if donor_name.upper() == donor.upper():
                print('Found {}'.format(donor_name))
                return (donor, donations)

        DONOR_SET[donor_name] = []
        print('{} not found in donor list. Adding...'.format(donor_name))
        return (donor_name, DONOR_SET[donor_name])

    return ''


def generate_thankyou_files(output_directory):
    """
    This function will output a set of thankyou files
    one for each donor which you can then send via email or
    snailmail"""

    if not output_directory or not os.path.isdir(output_directory):
        print('Output directory invalid.')
        output_directory = tempfile.gettempdir()

    print('Generating donor mails here {}'.format(output_directory))
    for donor, donations in DONOR_SET.items():
        mail_contents = formulate_mail((donor, donations), False)
        file_name = "{}/{}.txt".format(output_directory, donor)
        with open(file_name, "w") as outputfile:
            outputfile.write(mail_contents)


def main():
    """The main the program UI"""
    print('Starting Mailroom...')

    while True:
        print(BOUNDARY)
        menu_ui = UI_MENU['Main']
        response = input(menu_ui)

        print(BOUNDARY)
        print("You chose: {}".format(response))

        if response == "1":
            send_thankyou()
        elif response == "2":
            print_report()
        elif response == "3":
            menu_ui = UI_MENU['Directory Select']
            output_directory = input(menu_ui)
            generate_thankyou_files(output_directory)
        elif response == "4":
            quit_program()
        else:
            print("Invalid input. Please input a valid number")


if __name__ == "__main__":
    main()
