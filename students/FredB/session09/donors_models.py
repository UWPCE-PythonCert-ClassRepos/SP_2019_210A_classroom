

import statistics as stats



def standardize_name(donor_name):
    return donor_name.lower().replace(" ", "")

def valid_donation(donation):
    #donation must be a positive integer
    return (type(donation) == int) and (donation>0)



class Donor(object):

    def __init__(self,name,donations=None):
        self.standard_name = standardize_name(name)
        self.name = name.strip()
        self.donations = []
        self.load_error = []
        if donations:
            for d in donations:
                if valid_donation(d):
                    self.donations.append(d)
                else:
                    self.load_error.append(d)

    def add_donation(self,donation):
        self.donations.append(donation)

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
