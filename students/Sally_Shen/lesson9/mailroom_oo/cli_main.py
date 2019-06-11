import sys
from donor_models import DonorCollection
'''mailroom oo version'''

# store all the donors
donors = DonorCollection()


def send_thank_you():
    response = input("Type your donor name, if don't know, type list to pick")
    '''If the user types list show them a list of the donor names and re-prompt'''
    if response == "list":
        print(donors.list_donors())
        person = input("Please type your donor name.")
    else:
        person = response

    new_donation = input("how much to donate?")
    valid_input = False
    amount = 0.0
    while not valid_input:
        try:
            amount = float(new_donation)
            valid_input = True
        except ValueError:
            new_donation = input("Please input numbers!")

    donor = donors.add_donation(person, [amount])
    print(donor.create_thank_you_letter(amount))


def create_report():
    print(donors.generate_report())


def send_thank_you_to_all():
    print(donors.generate_thank_you_letters("thank_you_letters"))


def quit_menu():
    sys.exit(1)


def main_menu():

    switcher = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_thank_you_to_all,
        "4": quit_menu,
    }

    while True:
        answer = input("""What would you like to do?
        Pick one:
        1. Send a Thank You to a single donor
        2. Create a Report
        3. Send Thankyou letters to all donors
        4. Quit
        >>>""")
        print("You picked:", answer)
        answer = str(answer).strip()
        try:
            func = switcher.get(answer)
            func()
        except TypeError:
            print("Invalid option, please enter 1 - 4")


if __name__ == '__main__':
    print('Welcome to the OO Mailroom!')
    main_menu()
