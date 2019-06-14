

import sys
import math
from textwrap import dedent


def example_donors():
   return [Donor("Luke Skywalker", [100.25, 200.55, 50]),
            Donor("Han Solo", [100.80, 50.99, 600]),
            Donor("Yoda", [1000.01, 50, 600.55, 200.47]),
            Donor("Ben Kenobe", [101.32, 500, 60.34]),
            ]



class Donor:
    def __init__(self, name, donations = None):
        self.name = name.strip()

        if donations is None:
            self.donations = []
        elif type(donations) == list:
            self.donations = donations
        elif type(donations) == float:    
            self.donations = [donations]
        
    @property
    def key(self):
        return self.name.lower().strip().replace(" ", "")

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donations(self):
        return self.total_donations / len(self.donations)

    @property
    def last_donations(self):
        return self.donations[-1]

    def __str__(self):
        return f"\n\nDonor: {self.name} \nDonations: {self.donations}"

    def __lt__(self, other_donor):
        return sum(self.donations) < sum(other_donor.donations)


    def add_donation(self, donation):
        self.donations.append(donation)
"""
george = Donor("George Kim", [50])
george.normalized_name

DonorCollection = {"georgekim" : george}
"""


class DonorDb:
    
    def __init__(self, donors=None):

        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {donor.key: donor for donor in donors}

    
    def add_donor(self, donor):
        self.donor_data[donor.key] = donor

    def print_donors(self):
        for donor_key in self.donor_data:
            print(self.donor_data[donor_key])

    def generate_stats(self):
        for donor in self.donor_data:
            print(self.donor_data[donor], self.donor_data[donor].total_donations,
            len(self.donor_data[donor].donations), self.donor_data[donor].average_donation)
            
    def has_key(self, key):
        return key in self.donor_data

    def add_donation(self, key, donation):
        self.donor_data[key].add_donation(donation)

    def find_donor(self, name):
        return self.donor_data.get(Donor.key(name))


    def find_or_create_donor(self, name, donation):
        
        try:
            donor = self.donor_data[Donor.key(name)]
        except KeyError:
            self.add_donor(name)
        donor.add_donation(donation)
        return donor

    def send_email(self, donor):
        """
        This functions sends a letter to an individual donor
        """
        return dedent("""\n
        Dear {n},
        Thank you for your generous donation of ${a}! This will help our cause
        immensely in our battle against the darkside.  You, {n} , have made a big 
        difference in our efforts and we greatly appreciate you!!!  Your ${a} will be 
        put to great use to our forces against evil!  

        Thank you,

        The FORCE
        
        \n""".format(n = donor.name, a = donor.last_donations))
    
    def create_report(self):
        """
        Generates the report of donors by donation amount from greatest to least
        """
        donor_stats = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gifts = donor.average_donations
            stats = [name, total_gifts, num_gifts, avg_gifts]
            donor_stats.append(stats)

        stats_list = donor_stats
        stats_list.sort(key=lambda stats_list: stats_list[1],reverse=True)
        report = []
        report.append("{:<20}|{:^15}|{:^15}|{:>15}".format("Donor Name", 
                                                "Total Given",
                                                "Num Gifts",
                                                "Average Gifts"))
        report.append("-" * 68)
        for row in stats_list:
            report.append("{:<20}${:>15.2f} {:>15} ${:>15.2f}".format(*row))
        report.append("\nEnd of Report\n")
        return "\n".join(report)  

    
    def save_letters(self):
        """
        Saves letters to disk of all donors in data base
        """

        for donor in self.donor_data.values():   
            file_name = donor.name.replace(" ", "_") + ".txt"
            letter =  self.send_email(donor)
            with open(file_name, "w") as text_file:
                text_file.write(letter)   
                print("\nSaving {} file to disk".format(donor.name))
        print("\nSAVING COMPLETE\n")