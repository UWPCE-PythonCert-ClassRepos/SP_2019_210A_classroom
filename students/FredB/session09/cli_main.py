
from donors_models import Donor, DonorCollection, standardize_name, valid_donation
import sys, os

""" Initialize data"""
db = DonorCollection([Donor("Fred Flintstone", [100, 200, 50]),
                    Donor("James Bond", [0,0,7]),
                    Donor("Lex Luthor", [5000,]),
                    Donor("Harambe", [3, 2, 1]),
                    Donor("Herman Cain", [9, 9, 9]),
                    Donor("Placeholder Guy")])

def requested_list(userEntry):
    return (userEntry.lower() == 'list') or (userEntry.lower() == 'l')

def print_donor_list():
    print("Donor List\n")
    print("----------\n")
    for donor in db.donors:
        print(str(donor.name), "\n")

def print_thank_you(user_donor, user_donation):
    print ("Thank you {} for your generous donation of ${} from a charity".format(user_donor, user_donation))


def thank_you():
    #print("in thank you")
    user_donor = input("Enter full name of donor else type 'list' to see donor list: ")
    if requested_list(user_donor):
        print_donor_list()
        return
    elif not db.donor_present(user_donor):
        new_donor = input("Donor not found. Is this a new donor? (y/n): ")
        if new_donor[0].lower() == "y":
            db.add_donor(Donor(user_donor))
        else:
            return
    else:
        print("Donation again :)")
    user_donation = -1
    while not valid_donation(user_donation):
        print("Must be a positive integer")
        try:
            user_donation = int(input("Enter donation amount: "))
        except ValueError:
            user_donation = -1
    db.donors[standardize_name(user_donor)].add_donation(user_donation)
    print_thank_you(user_donor, user_donation)



def quit_program():
    print("quitting")
    sys.exit()


def main_menu():
    while True:
        choice = input("""What would you like to do?
Please enter a number 1-4:
1: Send a Thank You
2: Create a Report
3: Send letters to all donors
4: Quit
>>>""")
        switcher={
                "1":thank_you,
                "4":quit_program
             }
        switcher[choice]()
        """
                "2":print_report,
                "3":send_letters,"""

if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()