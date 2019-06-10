import datetime

"""The Mailroom Class Definitions"""
class Donor:
    """The Donor Class that contains donation information"""
    def __init__(self, name, _donations=None):
        self.donations = _donations
        self.key = self.standardize_name(name).strip()
        self.name =  name

    def standardize_name(self, name):
        return name.lower().strip().replace(' ', '')

    def to_str(self):
        return "{}\n------\n".format(self.__name)

    @property
    def donations(self):
        return self.__donations

    @donations.setter
    def donations(self, val=None):
        self.__donations = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    def add_donation(self, val):
        self.donations.append(Donation(val))

    def donations_to_str(self):
        return ", ".join(str(donation) for donation in self.__donations)


class DonorCollection:
    """The DonorCollection class which contains a set of donors"""
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
    """The Donation class which holds donation details"""
    def __init__(self, _amount=0, date=None):
        self.amount = _amount
        self.date = date or datetime.datetime.now()

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, val):
        self.__amount = val

    def to_str(self):
        return "{0:,.2f}".format(self.__amount)