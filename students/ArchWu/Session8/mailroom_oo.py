#!/usr/bin/env python3
import sys, os
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
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except:
                self.donations = [donations]
    
    @staticmethod
    def normalize_name(name):
        return name.lower().strip().replace(" ", "")
    
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

    # Singleton setup
    __instance = None

    @staticmethod
    def getDonorCollection():
        if DonorCollection.__instance == None:
            DonorCollection()
        return DonorCollection.__instance
    
    def __init__(self):
        if DonorCollection.__instance != None:
            raise Exception("This is a singleton")
        else:
            DonorCollection.__instance = self
            self.donors = {}
            
    
    def add_donor(self, donor):
        self.donors[Donor.normalize_name(donor.name)] = donor
    
    def get_donor(self, name):
        return self.donors[Donor.normalize_name(name)]
    
    def list_donor(self):
        listing = ["Donor list:"]
        for donor in self.donors:
            print(self.donors)
            listing.append(self.get_donor(donor.strip()).name)
        return "\n".join(listing)

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
        return "\n".join(report)
    
    @staticmethod
    def send_letter():
        pass
    
    @staticmethod
    def thank(parameter_list):
        pass

def main():
    print("Welcome")
    prompt = dedent('''
                Choose an action:

                (1) - Send a Thank You
                (2) - Create a Report
                (3) - Send letters to everyone
                (4) - Quit

                > ''')
    switch = {
        "1": DonorCollection.thank,
        "2": DonorCollection.report,
        "3": DonorCollection.send_letter,
        "4": goodbye
    }
    
    submenu(switch)


def submenu(switch):
    while True:
        try:
            choice = input("Select 1-4 > ")
            if choice not in switch.keys():
                print("choose again")
            else:
                switch[choice]()
        except KeyError:
            print("Error, choice invalid") 


def goodbye():
    sys.exit()


if __name__ == "__main__":
    init_donor_db()
    main()