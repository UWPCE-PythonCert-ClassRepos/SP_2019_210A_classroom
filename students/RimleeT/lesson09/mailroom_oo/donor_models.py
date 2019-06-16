import os
import tempfile

class Donor():
    def __init__(self, name, donation=None):

        if type(name) != str:
            raise Exception("Donor name should be a string type")
        else:
            self.name = name 
        
        self.donations = list()
        
        if donation != None:
            self.donate(donation)

    def donate(self, donation):
        if type(donation) == list:
            for item in donation:
                self.donate(item)
        else:
            try:
                donation_amount = float(donation) # Throws exection for invalid exception
            except Exception:
                raise Exception("Invalid type for donation amount")
            self.donations.append(donation_amount)
        
    def get_stat(self):
        total_donation = float(format(sum(self.donations),'.2f'))
        num_donation = len(self.donations)
        avg_donation = float(format(total_donation/num_donation,'.2f'))
        
        return {
                    "Total": total_donation,
                    "Count": num_donation,
                    "Avg": avg_donation
               }
    
    def send_letter(self, dir_name):
        stat = self.get_stat()
        letter = f"Dear {self.name}\n\n\tThank you for your very kind donation of ${stat['Total']} It will be put to very good use.\n\nSincerely,\nThe Team"
        
        f = tempfile.NamedTemporaryFile(prefix = self.name + '-', dir = dir_name, delete = False)
        f.write(letter.encode())
        
        return letter
        
class DonorCollection():
    def __init__(self):
        self._donor_list = list()
        
        # Initializing some donors
        self._donor_list.append(Donor("William Gates, III", [653772.32, 12.17]))
        self._donor_list.append(Donor("Jeff Bezos", 877.33))
        self._donor_list.append(Donor("Paul Allen", [663.23, 43.87, 1.32]))
        self._donor_list.append(Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]))
    
    
    def add_donation(self, name, donation):
        donor = self.find_donor(name)
        
        if not donor:
            donor = Donor(name, donation)
            self._donor_list.append(donor)
        else:
            donor.donate(donation)
            
        return donor
        
    def find_donor(self, name):
        for donor in self._donor_list:
            if donor.name == name:
                return donor
        return None
    
    def get_donors(self):
        return self._donor_list
    
    def send_letter(self):
        dir_name = tempfile.mkdtemp(prefix = 'Letters-', dir = os.getcwd())
        return [donor.send_letter(dir_name) for donor in self._donor_list]