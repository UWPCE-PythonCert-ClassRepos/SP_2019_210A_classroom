
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
    print()
    print("Donor List")
    print("----------")
    [print(name) for name in db.name_list]
    print()


def print_thank_you(donor, donation):
    print ("Thank you {} for your generous donation of ${} from a charity".format(donor, donation))


def thank_you():
    user_donor = input("Enter full name of donor else type 'list' to see donor list: ")
    if requested_list(user_donor):
        print_donor_list()
        return
    elif not db.donor_present(user_donor):
        user_answer = input("Donor not found. Is this a new donor? (y/n): ")
        if user_answer[0].lower() == "y":
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
    print_thank_you(db.donors[standardize_name(user_donor)].name, user_donation)


def print_report():
    print('Donor Name      | Total Given | Num Gifts   |  Average Gift')
    print('-----------------------------------------------------------')
    for j in db.stats_sorted:
        print('{:15}   ${:10.0f}{:8}         ${:10.0f}'.format(*j))


def send_letters():
    letter_template = """Dear {}, \n
    \n
    Thank you for your very kind donation of ${:.0f}. It will be put to very good use.\n
    \n
    Sincerely,\n
      -The Team"""
    for donor in db.donors:
        donor_name = db.donors[donor].name
        total_donation = db.donors[donor].tot_donation
        if total_donation: #only donors that have donated
            with open((os.getcwd() + "/" + "{}.txt").format(donor_name), 'w') as new_letter:
                new_letter.write(letter_template.format(donor_name, total_donation))
                new_letter.close()


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
                "2":print_report,
                "3":send_letters,
                "4":quit_program
             }
        try:
            switcher[choice]()
        except KeyError:
            print("Invalid selection\n")
            continue


if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()