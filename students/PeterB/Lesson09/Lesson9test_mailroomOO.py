import os
from mailroom import Donor


def test_donor_name():
    donor = Donor("Road Runner")

    assert donor.name == "Road Runner"

def test_find_donor_not():
    "test one that's not there"
    donor = mailroom.find_donor("Shawn Michs")

    assert donor is None

def test_add_donor():
    """
    adds a new donor

    then tests that the donor is added, and that a donation is properly recorded.
    """
    name = "Shawn Michaels  "

    donor = mailroom.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Shawn Michaels"
    assert donor[1] == [300]
    assert mailroom.find_donor(name) == donor


def test_add_donation():
    donor = Donor("Road Runner")

    donor.add_donation(4839283.32)

    assert donor.num_donations == 1


def test_send_thanks():
    pass


def test_donorDB():
    db = DonorDB()

    db.add_donation(Donation("Road"))

    db.avg_by_donor()

    db.total_donations()


if __name__ == "__main__":
    test_find_donor()
    test_find_donor_not()
    test_add_donor()
    test_donorDB()
    test_add_donation()
    test_send_thanks()