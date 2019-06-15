

import statistics as stats



def standardize_name(donor_name):
    return donor_name.lower().replace(" ", "")

def valid_donation(donation):
    #donation must be a positive integer
    return (type(donation) == int) and (donation>0)


class Donor(object):

    def add_donation(self,donation):
        self.donations.append(donation)

    def __init__(self,name,donations=None):
        self.name = name.strip()
        self.donations = []
        self.load_error = []
        if donations:
            for d in donations:
                if valid_donation(d):
                    self.add_donation(d)
                else:
                    self.load_error.append(d)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def ave_donation(self):
        if self.num_donations == 0:
            return 0
        else:
            return stats.mean(self.donations)

    @property
    def tot_donation(self):
        return sum(self.donations)

class DonorCollection(object):

    def add_donor(self, donor):
        self.donors[standardize_name(donor.name)] = donor

    def __init__(self, data=None):
        self.donors = {}
        if data:
            for d in data:
                self.add_donor(d)

    def donor_present(self,donor_name):
        return standardize_name(donor_name) in self.donors