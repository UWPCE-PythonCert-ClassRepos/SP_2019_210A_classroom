

main_donors = [("Luke Skywalker", [100.25, 200.55, 50]),
          ("Han Solo", [100.80, 50.99, 600]),
          ("Yoda", [1000.01, 50, 600.55, 200.47]),
          ("Ben Kenobe", [101.32, 500, 60.34]),
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


