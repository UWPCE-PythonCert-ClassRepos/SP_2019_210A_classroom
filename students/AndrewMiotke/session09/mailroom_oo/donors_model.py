
class Donor:
    def __init__(self, name, donations=None):
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except TypeError:
                self.donations = [donations]

    @staticmethod
    def normalize_name(name):
        return name.lower().replace(" ", "")


class DonorList:
    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}


    def get_donor(self, donor_name):
        key = donor_name.strip().lower()

        return self.donor_data.get(key)


    def add_donor(self, donor_name):
        donor_name = donor_name.strip()
        donor = (donor_name, [])
        self.donor_data[donor_name.lower()] = donor

        return donor