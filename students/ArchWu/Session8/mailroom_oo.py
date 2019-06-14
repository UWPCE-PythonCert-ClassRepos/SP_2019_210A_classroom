#!/usr/bin/env python3
import sys, os
from textwrap import dedent

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
        return name.lower().strip().replace("", " ")
    
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
            
    
    def add_donor(self, name):
        self.donors[Donor.normalize_name(name)] = Donor(name)
    
    def get_donor(self, name):
        return self.donors[Donor.normalize_name(name)]
    
    @staticmethod
    def list_donor(self):
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def report(self):
        """ Make a report on donations received by a style as specified """
        sorted_donors = sorted(self.donors.items(), reverse = True, key = lambda item: item.total())
        report_rows = ["{0:25s}   {1:10.2f}   {2:9d}   {3:11.2f}".format(*donor.gen_stats()) for donor in sorted_donors]
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
    db = DonorCollection()
    main()