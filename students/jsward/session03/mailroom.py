#!/usr/bin/env python

from operator import itemgetter


def add_donation():
    while True:
        user_input = str(input("Provide the name of the donor for which you'd like to add a donation.  "))
        for donor in donors:
            if donor['Name'] == user_input:
                donation_input = float(input("Found donor with name {}.  Input their donation amount in dollars".format(donor['Name'])))
                donor['Donations'].append(donation_input)
                print_thank_you(donor['Name'])
                return
        print("Donor {} not found.\n".format(user_input))


def add_donor():
    donor_valid = False
    while not donor_valid:
        user_input = str(input("Provide the name to add to the donor list  "))
        donor_valid = True
        for donor in donors:
            if donor['Name'] == user_input:
                print("Donor {} already exists.  Please provide a different donor name to add".format(user_input))
                donor_valid = False
                break
    donors.append({'Name': user_input, 'Donations': []})
    pass


def generate_stats(donor):
    num_donations = len(donor['Donations'])
    total_donation = float(sum(donor['Donations']))
    average_donation = (float(total_donation / num_donations))
    return [donor['Name'], total_donation, num_donations, average_donation]


def list_donors():
    for donor in donors:
        print(donor['Name'])


def menu_donor():
    while True:
        user_input = input("l to list donors\na to add donor\n$ to add donation\nt to print thank you message\n \n").lower()
        if user_input == 'l' or user_input == 'a' or user_input == '$' or user_input == 't':
            return user_input


def menu_main():
    """
    Prompts for user input.  Returns valid input
    :return: string with one of the following values: q, r, t
    """
    while True:
        user_input = input("q to quit\nr to generate a report\nd to manage donors (print thank you)\n \n").lower()
        if user_input == 'q' or user_input == 'r' or user_input == 'd':
            return user_input


def main():
    user_input = ''
    while 'q' not in user_input:
        user_input = menu_main()
        if 'r' in user_input:
            report()
        elif 'd' in user_input:
            donor_management()


def print_thank_you(donor_name=''):
    while True:
        if donor_name:
            for donor in donors:
                if donor['Name'] == donor_name:
                    last_donation = donor['Donations'][-1]
                    print(
                        "Thank you message:\n\n Dear {}, thank you for the very generous donation of ${}.  Rest assured it will be put to good use helping those in need*\n\n *After deducting 98% for management overhead, of course ;).".format(
                            donor_name, last_donation))
                    return
        donor_name = str(input("Provide the name of the donor for which you'd like to print a thank you message.  "))


def report():
    donor_data = []
    for donor in donors:
        donor_data.append(generate_stats(donor))
    sorted_donor_data = sorted(donor_data, key=itemgetter(1), reverse=True)
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


def donor_management():
    user_input = menu_donor()
    if 'l' in user_input:
        list_donors()
    elif 'a' in user_input:
        add_donor()
    elif '$' in user_input:
        add_donation()
    elif 't' in user_input:
        print_thank_you()


# Hard coded data, ewwww...
donors = [
    {'Name': 'Alice', 'Donations': [50.25, 50.00, 50]},
    {'Name': 'Bob', 'Donations': [200, 1000.00]},
    {'Name': 'Christine', 'Donations': [20, 10.73]},
    {'Name': 'Dave', 'Donations': [200, 500]},
    {'Name': 'Kim', 'Donations': [10000]}
]

if __name__ == '__main__':
    main()
