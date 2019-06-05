#! /usr/bin/env python3

class Donor:
  def __init__(self, fname, lname, **_donations):
    donations = []
    self.initialize_donations(_donations)
    self.fname = fname
    self.lname = lname

  def initialize_donations(self, donations):
    for date, donation in donations:
      self.donations.append(Donation(donation, date))

  def printme():
    print("{} {}\n------\n".format(self.fname, self.lname))
#    for donation in self.donations
#      donation.printme()


class Donation:
  def __init__(self, amount=0, date=0):
    self.amount = amount
    self.date = date

  def printme():
    print("{} : {}".format(self.date, self.amount))
  


dons = {} 
dons['2019-01-01'] = 20
a = Donor('Joe', 'Nunnelley', dons)
a.print()

