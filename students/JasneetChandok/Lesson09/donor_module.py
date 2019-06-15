#!/usr/bin/env python


class Donor:
    def __init__(self, name, donations=()):
        self.name = str(name)
        self.donations = []
        try:
            for donation in list(donations):
                self.add_donation(donation)
        except TypeError:
            self.add_donation(donations)

    def __str__(self):
        return self.name

    @property
    def stats(self):
        num_donations = len(self.donations)
        total_donation = float(sum(self.donations))
        if total_donation > 0:
            average_donation = (float(total_donation / num_donations))
        else:
            average_donation = 0.00
        return [self.name, total_donation, num_donations, average_donation]

    @property
    def thank_you_letter(self):
        if len(self.donations) == 0:
            letter_contents = "Dear {}, we look forward to your first donation!".format(self.name)
        else:
            letter_contents = "Dear {}, thank you for the very generous donation of ${:.2f}.  " \
                              "Rest assured it will be put to good use helping those in need*\n" \
                              "    *After deducting 98% for management overhead, of course ;).".format(self.name,
                                                                                                   self.donations[-1])
        return letter_contents

    def add_donation(self, amount):
        if type(amount) is str:
            amount = amount.strip('$ ').replace(',', '')
        amount = float(amount)
        if amount < 0:
            raise ValueError
        self.donations.append(amount)


class DonorCollection:
    def __init__(self):
        self.donors = []

    @property
    def donor_list(self):
        return [donor.name for donor in self.donors]

    @property
    def letters_to_all_donors(self):
        return [donor.thank_you_letter for donor in self.donors]

    @property
    def donor_report(self):
        return [donor.stats for donor in self.donors]

    def add_donor(self, name, donations=()):
        name_string = str(name)
        name_list = [name.capitalize() + ' ' for name in name_string.split(' ')]
        formatted_name = ''.join(name_list).strip()

        donor_exists = False
        for donor in self.donors:
            if donor.name == formatted_name:
                donor_exists = True
        if not donor_exists:
            new_donor = Donor(formatted_name, donations)
            self.donors.append(new_donor)
        else:
            raise ValueError