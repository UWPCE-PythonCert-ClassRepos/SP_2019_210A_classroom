#!/usr/bin/env python3

import csv, textwrap

class donor_db_collection:

    def __init__(self,donor_name,donation_amount):
        self.donor_name = donor_name
        self.donation_amount = donation_amount
        self.donor = {self.donor_name:self.donation_amount}
    
    @classmethod
    def from_csv(cls,csv_file):
        """
        this func is to take data from a csv file and create donation collection as a dictionary
        """
        donor_db = {}
        with open(csv_file,'r') as donor_file:
            csv_reader = csv.reader(donor_file)

            for line in csv_reader:
                line_num = []
                for s in line[1:]:
                    line_num.append(float(s))
                self = cls(line[0],line_num)
                donor_db.update(self.donor)
                
        return donor_db

    @staticmethod
    def gen_stats(a_list):
        """
        a function to process donor data
        v is a list of numbers
        return total amount, times of donation and average amount
        """
        total = sum(a_list)
        num = len(a_list)
        avg = format(total / num, ".2f")
        return total, num, avg

    @staticmethod
    def gen_report(a_dict):
        """
        this func is to print a table of donors_db to screen
        """
        

        header = "{:<20}  |{:^13}|{:^13}|{:>13}".format("Donor Name","Total Given","Num Gifts","Average Gift")

        print(header)
        for k,v in a_dict.items():
            total, num, avg = donor_db_collection.gen_stats(v)
            row = "{:<20}  ${:^13} {:^13}${:>13}".format(k,total,num,avg)
            print(row)



class donor(donor_db_collection):
    def __init__(self,donor_name,donation_amount):
        super().__init__(donor_name,donation_amount)
        self.total_amount = super().gen_stats(self.donation_amount)[0]

    def __repr__(self):
        return "Donor {} instance.".format(self.donor_name)

    def thank_you(self):
        """
        this func is to generate thank you letter for a donor
        """

        letter = textwrap.dedent("""
        Dear {},

        Thank you! The amount you donated is ${:.2f}!

        Sincerely
        The Team

        """.format(self.donor_name, self.total_amount))
        
        return letter

# donors = donor_db_collection.from_csv('donors.csv')
# print(donors)
# donor_db_collection.gen_report(donors)

# a = []
# for i in donors:
#     # print(i)
#     a.append(donor(i,donors[i]))

# print(a)
# print(a[0].donor_name)
# print(a[0].donation_amount)
# print(a[0].total_amount)
# print(a[0].thank_you())
# print(a[1]().thank_you())