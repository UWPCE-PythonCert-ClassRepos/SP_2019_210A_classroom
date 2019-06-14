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
    
    def normalize_name(self, name):
        return name.lower().strip().replace(" ", "")

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

    def __init__(self):
        self.donors = {}
            
    
    def add_donor(self, donor):
        self.donors[donor.norm_name] = donor
    
    def get_donor(self, name):
        return self.donors[normalize_name(name)]
    
    def add_donation(self, name, amount):
        self.get_donor(name).donations.append(amount)

    def list_donor(self):
        listing = ["Donor list:"]
        for donor in self.donors:
            print(self.donors[donor].name)
            listing.append(self.get_donor(donor.strip()).name)
        result = "\n".join(listing)
        return result

    def report(self):
        """ Make a report on donations received by a style as specified """
        sorted_donors = sorted(self.donors.items(), reverse = True, key = lambda item: item[1].total)
        report_rows = ["{0:25s}   {1:10.2f}   {2:9d}   {3:11.2f}".format(*donor[1].gen_stats()) for donor in sorted_donors]
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)

        for row in report_rows:
            report.append(row)
        result = "\n".join(report)
        print(result)
        return result
    
    @staticmethod
    def send_letter():
        pass