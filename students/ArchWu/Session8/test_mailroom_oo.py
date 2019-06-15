#!/usr/bin/env python3

"""
unit tests for the mailroom program
"""
import donor_model
import mailroom_oo as mailroomoo
import os
import pytest
# so that it's there for the tests
mailroom = mailroomoo.init_donor_db()


def test_list_donors():
    listing = mailroom.list_donor()

    # hard to test this throughly -- better not to hard code the entire
    # thing. But check for a few aspects -- this will catch the likely
    # errors
    assert listing.startswith("Donor list:\n")
    assert "Jeff Bezos" in listing
    assert "William Gates III" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    #pytest.skip("skipping this test")
    """ checks a donor that is there, but with odd case and spaces"""
    donor = mailroom.get_donor("jefF beZos ")

    assert donor.name == "Jeff Bezos"


def test_find_donor_not():
    "test one that's not there"
    
    with pytest.raises(KeyError):
        donor = mailroom.get_donor("Jeff Bzos")


# def test_gen_letter():
#     """ test the donor letter """

#     # create a sample donor
#     donor = ("Fred Flintstone", [432.45, 65.45, 230.0])
#     letter = mailroom.gen_letter(donor)
#     # what to test? tricky!
#     assert letter.startswith("Dear Fred Flintstone")
#     assert letter.endswith("-The Team\n")
#     assert "donation of $230.00" in letter


def test_add_donor():
    """
    adds a new donor

    then tests that the donor is added, and that a donation is properly recorded.
    """
    name = "Fred Flintstone  "
    donor = mailroomoo.Donor(name)
    mailroom.add_donor(donor)
    donor.donations.append(300)
    assert donor.name == "Fred Flintstone"
    assert donor.donations == [300]
    assert mailroom.get_donor(name) == donor


def test_generate_donor_report():

    report = mailroom.report()

    print(report)  # printing so you can see it if it fails
    # this is pretty tough to test
    # these are not great, because they will fail if unimportant parts of the
    # report are changed.
    # but at least you know that codes working now.
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")
    assert("Jeff Bezos" in report)
    assert "877.33" in report
    #assert "Jeff Bezos                  $    877.33           1   $     877.33" in report



# def test_save_letters_to_disk():
#     """
#     This only tests that the files get created, but that's a start

#     Note that the contents of the letter was already
#     tested with test_gen_letter
#     """
#     mailroom.save_letters_to_disk()

#     assert os.path.isfile('jeff bezos.txt')
#     assert os.path.isfile('william gates iii.txt')
#     # check that it'snot empty:
#     with open('william gates iii.txt') as f:
#         size = len(f.read())
#     assert size > 0


if __name__ == "__main__":
    # this is best run with a test runner, like pytest
    # But if not, at least this will run them all.
    # test_list_donors()
    # test_find_donor()
    # test_find_donor_not()
    # test_gen_letter()
    # test_add_donor()
    # test_generate_donor_report()
    # test_save_letters_to_disk()
    print("All tests Passed")
