"""
The Various Mailroom Classes
- Donor
- Donation
- DonorCollection
"""

import datetime

class Donor:
    """The Donor Class that contains donation information"""
    def __init__(self, name, _donations=None):
        self.__donations = _donations
        self.key = self.standardize_name(name).strip()
        self.__name = name


    @classmethod
    def standardize_name(cls, name):
        """Generate a standardized name key"""
        return name.lower().strip().replace(' ', '')


    @property
    def donations(self):
        """Getter for the donations list"""
        return self.__donations


    @donations.setter
    def donations(self, val=None):
        """Setter for the donations list"""
        self.__donations = val


    @property
    def name(self):
        """Getter for the donor name"""
        return self.__name


    @name.setter
    def name(self, val):
        """Setter for the donor name"""
        self.__name = val


    def add_donation(self, val):
        """Function to add a donation to the donor"""
        self.donations.append(Donation(val))


    def donations_to_str(self):
        """Function to return the donations of this donor as a string"""
        return ", ".join(str(donation) for donation in self.__donations)


class DonorCollection:
    """The DonorCollection class which contains a set of donors"""
    def __init__(self, donors=None):
        self.__donors = []
        if donors is not None:
            # creates key to donor and inserts the donor object
            self.__donors = {d.standardize_name: d for d in donors}


    def add(self, donor=None):
        """Add a donor to the donors list"""
        if donor is not None:
            self.__donors.append(donor)

        return self.__donors


    def delete(self, donor_name=None):
        """Delete a user from the donors list"""
        for index, donor in enumerate(self.__donors):
            if donor_name.lower() == donor.name.lower():
                del self.__donors[index]

        return len(self.__donors)


    def get_donor(self, donor_name=None):
        """Return the queried user or a None"""
        for donor in self.__donors:
            if donor_name.lower() == donor.name.lower():
                return donor

        return None


    @property
    def donors(self):
        """Getter for returning the donor set"""
        return self.__donors



class Donation:
    """The Donation class which holds donation details"""
    def __init__(self, _amount=0, date=None):
        self.__amount = _amount
        self.date = date or datetime.datetime.now()


    @property
    def amount(self):
        """Setter for the donation amount"""
        return self.__amount


    @amount.setter
    def amount(self, val):
        """Setter for the donation amount"""
        self.__amount = val


    def to_str(self):
        """Function to return the donation amount formatted"""
        return "{0:,.2f}".format(self.__amount)
