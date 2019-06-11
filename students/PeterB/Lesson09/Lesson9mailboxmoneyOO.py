#!/usr/bin/python3

class Donor:
    def __init__(self, name, donations=None):
        self.name = self.norm_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations - []
        else:
            try:
                self.donations = list(donations)
            except:
                self.donations = [donations]

    def norm_name(self, name):
        return name.lower().strip().replace(" ","")

    def add_donation(self, donation):
        self._donations.append(donation)

    def remove_donation(self, donation):
        if donation in self.donations:
            self.donations.remove(donation)
            return f'Your donation {donation} has been removed. Thank you'

    def send_thanks(self, name, donation):
        return f'Composing Thank You email:\n'
        f'Thank you {name} for your donation of ${donation:%10.2f}!'

class DonorDB:

    @staticmethod
    def get_sample_data():
        return DonorDB([
            Donor("Road Runner", [4839283.32, 17842102.94]),
            Donor("Shawn Michaels", [55303.04, 5000.08, 300.03]),
            Donor("Sasuke Uchiha", [80040033.32]),
            Donor("Frieza", [0.50, 1.75, 2000.25]),
        ])

    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}


    def total_donations(self):
        return sum([sum(donor.donations) for donor in self.donor_data])

    def avg_by_donor(self):
        return ([sum(donor.donations)/len(donor.donations) for donor in self.donor_data])

        if self.donations == {}:
            return sum(self.donations) / len(self.donations)

    def find_donor(self):
        key = name.strip().lower()
        return donorDB.get(key)



db = DonorDB.get_sample_data()
print(db)
