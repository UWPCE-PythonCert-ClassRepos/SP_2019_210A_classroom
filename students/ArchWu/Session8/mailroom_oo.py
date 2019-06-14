#!/usr/bin/env python3
import sys, os, math
from textwrap import dedent

def init_donor_db():
    db = DonorCollection()
    db.add_donor(Donor("William Gates III", [653772.32, 12.17]))
    db.add_donor(Donor("Jeff Bezos", [877.33]))
    db.add_donor(Donor("Paul Allen", [663.23, 43.87, 1.32]))
    db.add_donor(Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]))
    return db

class Donor:
    def __init__(self, name, donations = None):
        self.norm_name = normalize_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except:
                self.donations = [donations]
    
    @property
    def total(self):
        if self.donations:
            return sum(self.donations)
        else:
            return 0
    
    @property
    def average(self):
        if self.donations:
            return self.total / len(self.donations)
        else:
            return 0
    
    def gen_stats(self):
        return self.name, self.total, len(self.donations), self.average

class DonorCollection():

    def __init__(self):
        self.donors = {}
            
    
    def add_donor(self, donor):
        self.donors[donor.norm_name] = donor
    
    def get_donor(self, name):
        return self.donors[normalize_name(name)]
    
    def add_donation(self, name, amount):
        self.get_donor(name).donations.append(amount)

    def list_donor(self):
        listing = ["Donor list:"]
        for donor in self.donors:
            print(self.donors[donor].name)
            listing.append(self.get_donor(donor.strip()).name)
        result = "\n".join(listing)
        return result

    def report(self):
        """ Make a report on donations received by a style as specified """
        sorted_donors = sorted(self.donors.items(), reverse = True, key = lambda item: item[1].total)
        report_rows = ["{0:25s}   {1:10.2f}   {2:9d}   {3:11.2f}".format(*donor[1].gen_stats()) for donor in sorted_donors]
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)

        for row in report_rows:
            report.append(row)
        result = "\n".join(report)
        print(result)
        return result
    
    @staticmethod
    def send_letter():
        pass
    
def main():
    
    prompt = dedent('''
                Choose an action:

                (1) - Send a Thank You
                (2) - Create a Report
                (3) - Send letters to everyone
                (4) - Quit

                > ''')
    switch = {
        "1": submenu,
        "2": db.report,
        "3": save_letters_to_disk,
        "4": goodbye
    }
    
    menu(switch, prompt)


def menu(switch, prompt):
    while True:
        try:
            choice = str(input(prompt)).strip().lower()          
            if choice not in switch.keys():
                print("choose again")
            else:
                if switch[choice]():
                    break
        except KeyError:
            print("Error, choice invalid")
        

def submenu():
    prompt = ("To send a thank you, select one:\n\n"
                "(1) Update donor and send thank-you\n"
                "(2) List all existing DONORS\n"
                "(3) Return to main menu\n > ")
    switch = {
        "1": thank_you,
        "2": db.list_donor,
        "3": return_menu,
    }
    menu(switch, prompt)

def goodbye():
    sys.exit()

def return_menu():
    return True


def thank_you():
    """
    Ask user for donation amount, and then add it  to the DB
    """
    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    print("in take_donation")
    name = input("Enter a donor name (new or existing): \n >")
    if name == 'quit': return
    while True:
        amount_str = input("Enter a donation amount (or <enter> to exit)> ").strip()
        if not amount_str:
            # if they provide no input, go back to previous menu
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("error: donation amount is invalid\n")
            continue
        else:
            break

    if normalize_name(name) not in db.donors.keys():
        new_donor = Donor(name)
        db.add_donor(new_donor)
    db.donors[normalize_name(name)].donations.append(amount)

    """Generate Letter Here"""
    return

def save_letters_to_disk():
    temp_path = os.getcwd()

    for donor in db.donors.items():
        with open('{}/{}.txt'.format(temp_path, donor[1].name), 'w') as f:
            num_donation = donor[1].total
            greetings = 'Dear {},\n'.format(donor[1].name)
            body = '\nThank you for your generous gift ${} to us!\n'.format(num_donation)
            ending = '\nSincerely,\n  ABC foundations'
            f.write(greetings + body + ending)
    return

def normalize_name(name):
    return name.lower().strip().replace(" ", "")

if __name__ == "__main__":
    print("Welcome")
    db = init_donor_db()
    main()