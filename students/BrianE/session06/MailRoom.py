#!/usr/bin/env python3

import sys
from textwrap import dedent

'''
Manage donation information and generate thank-you emails for donors
'''


def initalize_donor_db():
    """
    Initialize donor DB as dictionary

    :return: donors as dictionary
    """

    donors = {
        'Brian Ervin': [100.57, 200.63, 350.47],
        'Steve Walline': [300.55, 500.14, 443.80],
        'Mike Tomson': [100.25, 300.12, 543.45],
        'Michelle Anderson': [700.67, 1300.56, 154],
        'Matt Anderson': [224.34, 600.50, 5000.12]}
    return donors


def list_donors(donors):
    """
    Display a list of donors currently in donors DB

    :return: string containing donors separated by newline
    """

    return "\n".join([donor for donor in donors])


def generate_email(donor, recent_donation_amount):
    """
    Generate thank-you email message to donor

    :param donor: donor name
    :param recent_donation_amount: most recent donation amount
    :return: email_message string
    """

    email_message = dedent('''Dear {},
          Thank you for your recent donation of ${}.

                         Sincerely,
                            -FakeCorp, Inc.
          '''.format(donor, recent_donation_amount))
    return email_message


def send_thankyou(donors):
    """
    Capture new donation info and generate thank-you email
    :param donors: dictionary containing donor info
    :return: updated donors dictionary
    """
    while True:
        name = input("Enter donor's full name\n(Enter 'List' to display current donors):\n >>>")
        if name.lower() == 'list':
            print(list_donors(donors))
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
            print(generate_email(name, amount))
            break
    return donors


def generate_all_thankyou_emails(donors):
    """
    Generate thank-you emails to all donors in database
    :param donors: dictionary of donors
    :return: write email text to file for each donor
    """

    for donor in donors:
        most_recent_donation = donors[donor][-1]
        email_message = generate_email(donor, most_recent_donation)

        filename = f"{donor}.txt"
        with open(file=filename, mode='w') as email_file:
            email_file.writelines(email_message)


def generate_report(donors):
    """
    Generate donation report
    :param donors: dictionary containing donor info
    :return: None
    """

    header = f'| {"Donor Name":19} | {"Total Donated":9} | {"Num Gifts":5} | {"Average Gift":8}'
    separator = "-" *64
    report = []
    report.append(header)
    report.append(separator)

    for donor in donors:
        total_donated = round(sum(donors[donor]), 2)
        num_gifts = len(donors[donor])
        average = round((total_donated / num_gifts), 2)
        report.append("| {0:20}| {1:13} | {2:10}| {3:10} |".format(donor, total_donated, num_gifts, average))
    return '\n'.join(report)


def display_report(donors):
    """
    Display donors report to user
    :param donors: donors DB
    :return:
    """
    print(generate_report(donors))


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
        2: display_report,
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
    donors = initalize_donor_db()
    main_menu(donors)


if __name__ == '__main__':
    main()
