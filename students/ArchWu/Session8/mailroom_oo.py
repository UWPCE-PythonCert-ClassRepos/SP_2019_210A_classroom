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

    @staticmethod
    def report():
        
    @staticmethod
    def send_letter()
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
            choice = input("Select 1-3 > ")
            if choice not in switch.keys():
                print("choose again")
            else:
                switch[choice]()
        except KeyError:
            print("Error, choice invalid") 


def goodbye():
    sys.exit()

def gen_letter():
    pass

if __name__ == "__main__":
    main()