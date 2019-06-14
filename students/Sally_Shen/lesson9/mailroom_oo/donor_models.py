import os


class Donor:
    def __init__(self, name, donations=None):
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except ValueError:
                self.donations = [donations]

    @staticmethod
    def normalize_name(name):
        return name.lower().strip().replace(" ", "")

    def add_donation(self, amount):
        try:
            self.donations.append(float(amount))
            return self.create_thank_you_letter(float(amount))
        except ValueError:
            print("Donation amount should be in float string")

    def add_donations(self, amounts):
        for amount in amounts:
            self.add_donation(amount)

    @property
    def donor_name(self):
        return self.name

    @property
    def donation_sum(self):
        return sum(self.donations)

    @property
    def donation_avg(self):
        return sum(self.donations) / len(self.donations)

    def create_thank_you_letter(self, amount):
        letter = '''
        Dear {0},
        Thank you for donating {1}!\n'''.format(self.name, amount)
        return letter

    def gen_stats(self):
        return self.name, self.donation_sum, len(self.donations), self.donation_avg


class DonorCollection:
    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    def list_donors(self):
        return ", ".join(self.donor_data.keys())

    def add_donor(self, name):
        if name not in self.donor_data:
            self.donor_data[name] = Donor(name)

    def add_donation(self, donor_name, amounts=[]):
        if donor_name in self.donor_data:
            self.donor_data[donor_name].add_donations(amounts)
        else:
            self.donor_data[donor_name] = Donor(donor_name, amounts)
        return self.donor_data[donor_name]

    def find_donor(self, donorName):
        if donorName in self.donor_data:
            return self.donor_data[donorName]

    def generate_report(self):
        sorted_names = []
        if self.donor_data:
            sorted_names = sorted(list(self.donor_data.keys()))
        output = "{:<20}{:<20}{:<15}{:<20}\n".format("Donor Name", "|Total Given", "|Num Gifts", "|Average Gift")
        output += "-------------------------------------------------------------------\n"
        output += "".join(
            self.line_item(*(self.donor_data[name].gen_stats())) for name in sorted_names)

        return output

    @staticmethod
    def line_item(name, total, num, avg):
        output = "{:<20}${:<20.2f}{:<15}${:<20.2f}\n".format(name, total, num, avg)
        return output

    def generate_thank_you_letters(self, directory):
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        prev_dir = os.getcwd()
        os.chdir(directory)
        for donor in self.donor_data.values():
            fileName = donor.name + ".txt"
            with open(fileName, "w") as f:
                f.write('''
                Dear {0},
                        Thank you for your very kind donation of ${1:.2f}.

                        It will be put to very good use.

                                            Sincerely,
                                                - The Team'''.format(donor.name, donor.donation_sum))
        os.chdir(prev_dir)



