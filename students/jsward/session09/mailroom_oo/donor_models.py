#!/usr/bin/env python


class Donor:
    def __init__(self, name, donations=()):
        """
        Initializes an instance of the Donor class

        :param name: Donor's name as a string, or value that can be converted to a string
        :param donations: Optional tuple of donations.  Donation values must be convertible to floats.
        """
        self.name = str(name)
        self.donations = []
        try:
            for donation in list(donations):
                self.add_donation(donation)
        except TypeError:
            self.add_donation(donations)

    def __str__(self):
        """
        String representation of the donor object

        :return: string
        """
        return self.name

    @property
    def stats(self):
        """
        Calculates donor statistics

        :return: A list containing donor's name, total donation amount, number of donations and average donation amount
        """
        num_donations = len(self.donations)
        total_donation = float(sum(self.donations))
        if total_donation > 0:
            average_donation = (float(total_donation / num_donations))
        else:
            average_donation = 0.00
        return [self.name, total_donation, num_donations, average_donation]

    @property
    def thank_you_letter(self):
        """
        A thank you letter to the donor for their most recent donation.
        If no donations have been made letter instead encourages making a first time donation.

        :return: string
        """
        if len(self.donations) == 0:
            letter_contents = "Dear {}, we look forward to your first donation!".format(self.name)
        else:
            letter_contents = "Dear {}, thank you for the very generous donation of ${:.2f}.  " \
                              "Rest assured it will be put to good use helping those in need*\n" \
                              "    *After deducting 98% for management overhead, of course ;).".format(self.name,
                                                                                                   self.donations[-1])
        return letter_contents

    def add_donation(self, amount):
        """
        Add a donation from the donor

        :param amount: The monetary value of the donation in USD.  Must be convertible to a float.
        :return: None
        """
        if type(amount) is str:
            amount = amount.strip('$ ').replace(',', '')
        amount = float(amount)
        if amount < 0:
            raise ValueError
        self.donations.append(amount)


class DonorCollection:
    def __init__(self):
        """
        Initializes an instance of the DonorCollection class
        """
        self.donors = []

    @property
    def donor_list(self):
        """
        Generate a list of donor names

        :return: List
        """
        return [donor.name for donor in self.donors]

    @property
    def letters_to_all_donors(self):
        """
        Generate a list of thank you letters to donors

        :return: list
        """
        return [donor.thank_you_letter for donor in self.donors]

    @property
    def donor_report(self):
        """
        Generate a donor report.
        Contains name, total donation amount, number of donations and average donation amount for each donor.

        :return: list
        """
        return [donor.stats for donor in self.donors]

    def add_donor(self, name, donations=()):
        """
        Formats the provided donor name.  Adds a donor to the DonorCollection.

        :param name: Donor's name as a string, or value that can be converted to a string
        :param donations: Optional tuple of donations.  Donation values must be convertible to floats.
        :return: None
        """
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
