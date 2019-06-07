import datetime

class Donor:
    def __init__(self, name, donations=None):
        self.donations = []
        self.key = self.standardize_name(name).strip()
        self.initialize_donations(donations)
        self.name = name

    def standardize_name(self, name):
        return name.lower().strip().replace(' ', '')

    def initialize_donations(self, donations):
        if donations:
            for date, donation in enumerate(donations):
                self.donations.append(Donation(donation, date))

    def to_str(self):
        return "{}\n------\n".format(self.name)

    @property
    def get_donations(self):
        return self.donations

    def add_donation(self, val):
        self.donations.append(Donation(val))

    def donations_to_str(self):
        return ", ".join(donation.to_str() for donation in self.donations)


class DonorCollection:
    def __init__(self, donors=None):
        self.donors = []
        if donors is not None:
            # creates key to donor and inserts the donor object
            self.donors = { d.standardize_name: d for d in donors }

    def add(self, donor=None):
        """Add a donor to the donors list"""
        if donor is not None:
            self.donors.append(donor)

        return self.donors


    def delete(self, donor_name=None):
        """Delete a user from the donors list"""
        for index, donor in enumerate(self.donors):
            if donor_name.lower() == donor.name.lower():
                del(self.donors[index])

        return len(self.donors)


    def get_donor(self, donor_name=None):
        """Return the queried user or a None"""
        for donor in self.donors:
            if donor_name.lower() == donor.name.lower():
                return donor

        return None




class Donation:
    def __init__(self, amount=0, date=0):
        self.amount = amount
        self.date = date

    @property
    def get_amount(self):
        return self.amount

    def set_amount(self, val):
        self.amount = val

    def to_str(self):
        return "{0:,.2f}".format(self.amount)