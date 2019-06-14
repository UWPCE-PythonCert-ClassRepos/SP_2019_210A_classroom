#!/usr/bin/env python

"""
unit tests for the mailroom program
"""
import os

import mailroom3 as mailroom

# so that it's there for the tests
mailroom.donor_db = mailroom.get_donor_db()


def test_list_donors():
    listing = mailroom.list_donors()

    # hard to test this throughly -- better not to hard code the entire
    # thing. But check for a few aspects -- this will catch the likely
    # errors
    assert listing.startswith("Donor list:\n")
    assert "Shawn Michaels" in listing
    assert "Sasuke Uchiha" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """ checks a donor that is there, but with odd case and spaces"""
    donor = mailroom.find_donor("sHaWn MichAels ")

    assert donor[0] == "Shawn Michaels"


def test_find_donor_not():
    "test one that's not there"
    donor = mailroom.find_donor("Shawn Michs")

    assert donor is None


def test_gen_letter():
    """ test the donor letter """

    # create a sample donor
    donor = ("Frieza", [0.50, 1.75, 2000.25])
    letter = mailroom.gen_letter(donor)
    # what to test? tricky!
    assert letter.startswith("Dear Frieza")
    assert letter.endswith("-The Team\n")
    assert "donation of $1.75" in letter


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


def test_generate_donor_report():

    report = mailroom.generate_donor_report()

    print(report)  # printing so you can see it if it fails
    # this is pretty tough to test
    # these are not great, because they will fail if unimportant parts of the
    # report are changed.
    # but at least you know that codes working now.
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")

    assert "Shawn Michaels                  $    55303.04           1   $     55303.04" in report


def test_save_letters_to_disk():
    """
    This only tests that the files get created, but that's a start

    Note that the contents of the letter was already
    tested with test_gen_letter
    """

    mailroom.save_letters_to_disk()

    assert os.path.isfile('Shawn_Michaels.txt')
    assert os.path.isfile('Road_Runner.txt')
    # check that it'snot empty:
    with open('Road_Runner.txt') as f:
        size = len(f.read())
    assert size > 0


if __name__ == "__main__":
    test_list_donors()
    test_find_donor()
    test_find_donor_not()
    test_gen_letter()
    test_add_donor()
    test_generate_donor_report()
    test_save_letters_to_disk()
    print("All tests Passed")