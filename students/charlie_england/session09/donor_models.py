
class Donor:
    """
    holds donor information including the name of the donor, and a list of donations
    properties:
        average: the average donations contained in the instance list
        num_donations: the length of the donations list = number of donations
        total = the sum of the donations list
    has a send_thank_you function which will return a string thanking the donor for their most recent donation, it also gives information about previous donations
    """
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
        if self.num_donations == 0:
            return 0
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
            You have given us a total of ${:,.2f} over {} donation(s) with an average of ${:,.2f} per donation!
            Again thank you\n
        Sincerely,\n
            Local Charity """.format(self.name, self.donations[-1],self.total,self.num_donations,self.average)
            )
        

class Donor_Collection:
    """
    This donor collection class stores the donors with the normalized name as the key for each instance of the donor object.
    add donor will add a new donor to the list (it takes a Donor instance of the class)
    search donor will return true of the normalized name is in the keys of the current donor
    generate report will generate a list (which can be printed) that will display each donor in the donor_data and their relevate donor information
    send letters will write out letters for each donor and append a 2 length list to an output list for each donor. the first index is the string to be emailed/printed, the second is the donor name for ease of use
    """
    def __init__(self,donors=None):
        if not donors:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name:d for d in donors} #create a key for the using the normalized name
    
    def add_donor(self,donor_info):
        self.donor_data.update({donor_info.norm_name:donor_info})

    def search_donor(self,donor):
        #search for a given donor
        if donor.lower().strip().replace(" ","") in self.donor_data.keys():
            return True

    def gen_report(self):
        #generate a report of all the donors
        rep_list = []
        rep_list.append("Donor Name" + " "*11 + "|" + " "*3 + " Total Given " + " "*3 +
                   "| Num Gifts " + "| Average Gift\n" + "-"*60)
        for donor in self.donor_data.values():
            rep_list.append(f"{donor.name:<20} $  {donor.total:>16,.2f} {donor.num_donations:^12} $ {donor.average:>10,.2f}")
        return rep_list

    def send_letters(self):
        send_letter_lst = []
        for donor in self.donor_data.values():
            send_letter_lst.append(["""Dear {},\n\n 
            On behalf of Local Charity we would like to extend our sincerest thanks for your most recent ${:,.2f} donation.\n
            Without people like you we could not continue blah blah blah\n
            Over time you have given us a total of ${:,.2f} over {} donation(s) which averages out to ${:,.2f} per donation! \n
            Again thank you\n
            Sincerely,\n
            Local Charity """.format(donor.name, donor.donations[-1], donor.total, donor.num_donations, donor.average),donor.name])
        return send_letter_lst

