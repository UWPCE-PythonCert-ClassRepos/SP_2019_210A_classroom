#donor class
#collection class (donor database)
import math

def get_sample_data():
    '''
    returns a list of the instances of donor classes
    '''
    return [
        Donor("Jeff Bezos",[1000,500,20]),
        Donor('blue berry',[1233,513])
    ]

class Donor:
    def __init__(self,name,donations=None):
        self.norm_name = self.normalize_name(name) #standarize name for searching
        self.name = name.strip()
        if not donations:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except:
                self.donations=[donations]

    def normalize_name(self,name):
        return name.lower().strip().replace(" ","")

    @property
    def average(self):
        average = 0
        for donation in self.donations:
            average+=donation
        return (average/self.num_donations)

    @property
    def num_donations(self):
        return len(self.donations)
    
    @property
    def total(self):
        return sum(self.donations)

    def add_donation(self,donation):
        self.donations.append(donation)

    def send_thank_you(self):
        return (
            """Dear {},\n\n 
            On behalf of Local Charity we would like to extend our sincerest thanks for your ${:,.2f} donation.\n
            Without people like you we could not continue blah blah blah.\n
            You have given us a total of {:,.2f} over {} donation(s) with an average of {:,.2f} per donation!
            Again thank you\n
        Sincerely,\n
            Local Charity """.format(self.name, self.donations[-1],self.total,self.num_donations,self.average)
            )
        

class Donor_Collection:
    def __init__(self,donors=None):
        if not donors:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name:d for d in donors} #create a key for the using the normalized name
    
    def add_donor(self,donor_info):
        self.donor_data.update({donor_info.norm_name:donor_info})

    def search_donor(self,donor):
        #search for a given donor
        pass

    def gen_report(self):
        #generate a report of all the donors
        pass