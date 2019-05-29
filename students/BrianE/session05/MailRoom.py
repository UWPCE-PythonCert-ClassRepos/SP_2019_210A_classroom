#!/usr/bin/env python3

import sys
import tempfile

'''
Manage donation information and generate thank-you emails for donors
'''


def send_thankyou(donors):
    """
    Capture new donation info and generate thank-you email
    :param donors: dictionary containing donor info
    :return: updated donors dictionary
    """
    while True:
        name = input("Enter donor's full name\n(Enter 'List' to display current donors):\n >>>")
        if name.lower() == 'list':
            print([donor for donor in donors])
            continue
        else:
            try:
                amount = float(input("Enter donation amount: "))
            except ValueError:
                print("Value entered is not valid. Only integers or floating points are supported.")
                break
            if name.strip() in donors:
                donors[name].append(amount)
            else:
                donors[name] = [amount]
            email_message = f"Dear {name.strip()},\n" \
                            f"    Thank you for your recent donation of ${amount}!\n\n" \
                            f"    Sincerely,\n\n" \
                            f"    FakeCorp, Inc"
            print(email_message)
            break
    return donors


def generate_all_thankyou_emails(donors):
    """
    Generate thank-you emails to all donors in database
    :param donors: dictionary of donors
    :return: write email text to file for each donor
    """

    for donor in donors:
        total_donated = round(sum(donors[donor]), 2)
        most_recent_donation = donors[donor][-1]
        email_message = f"Dear {donor},\nThank you for your recent donation of ${most_recent_donation}! In total, " \
                        f"you've donated {total_donated}!\n\n"

        with tempfile.TemporaryFile(mode='w+') as email_file:
            email_file.writelines(email_message)
            email_file.seek(0)
            print(email_file.read())


def generate_report(donors):
    """
    Generate donation report
    :param donors: dictionary containing donor info
    :return: None
    """

    header = f'| {"Donor Name":19} | {"Total Donated":9} | {"Num Gifts":5} | {"Average Gift":8}'
    print(header)
    print("-" * 64)

    for donor in donors:
        total_donated = round(sum(donors[donor]), 2)
        num_gifts = len(donors[donor])
        average = round((total_donated / num_gifts), 2)
        print("| {0:20}".format(donor), end='')
        print("| {0:13} | {1:10}| {2:10} |".format(total_donated, num_gifts, average))


def menu_quit(donors):
    """
    Quit main menu upon user request
    :param donors:
    :return: 0
    """
    sys.exit(0)


def main_menu(donors):
    switch_main_menu = {
        1: send_thankyou,
        2: generate_report,
        3: generate_all_thankyou_emails,
        9: menu_quit}

    while True:
        try:
            choice = int(input("""\n\n
            What would you like to do?
            1) Send a Thank You
            2) Create a Report
            3) Generate thank-you emails for all donors
            9) QUIT\n
            >>>:"""))
        except ValueError:
            print("Please enter a valid option. (1, 2, 3 or 9)")
            continue

        try:
            switch_main_menu.get(choice)(donors)
        except TypeError:
            print("Please enter a valid option. (1, 2, 3 or 9)")



def main():
    donors = {'Brian Ervin': [100.57, 200.63, 350.47],
              'Steve Walline': [300.55, 500.14, 443.80],
              'Mike Tomson': [100.25, 300.12, 543.45],
              'Michelle Anderson': [700.67, 1300.56, 1543.22],
              'Matt Anderson': [224.34, 600.50, 5000.12]}

    main_menu(donors)


if __name__ == '__main__':
    main()
