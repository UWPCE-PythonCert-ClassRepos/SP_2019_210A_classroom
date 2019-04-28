#!/usr/bin/env python3

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
            print([donor for donor in donors.keys()])
            continue
        else:
            amount = float(input("Enter donation amount: "))
            if name.strip() in donors.keys():
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


def generate_report(donors):
    """
    Generate donation report
    :param donors: dictionary containing donor info
    :return: None
    """

    header = f'| {"Donor Name":19} | {"Total Donated":9} | {"Num Gifts":5} | {"Average Gift":8}'
    print(header)
    print("-" * 64)

    for donor in donors.keys():
        total_donated = round(sum(donors[donor]), 2)
        num_gifts = len(donors[donor])
        average = round((total_donated / num_gifts), 2)
        print("| {0:20}".format(donor), end='')
        print("| {0:13} | {1:10}| {2:10} |".format(total_donated, num_gifts, average))

def main():

    donors = {'Brian Ervin': [100.57, 200.63, 350.47],
              'Steve Walline': [300.55, 500.14, 443.80],
              'Mike Tomson': [100.25, 300.12, 543.45],
              'Michelle Anderson': [700.67, 1300.56, 1543.22],
              'Matt Anderson': [224.34, 600.50, 5000.12]}

    while True:
        choice = input("""\n\n
        What would you like to do?
        1) Send a Thank You
        2) Create a Report
        9) QUIT\n
        >>>:""")
        if choice == "1":
            donors = send_thankyou(donors)
        elif choice == "2":
            generate_report(donors)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please choose between options 1 or 2")


if __name__ == '__main__':
    main()

