#!/usr/bin/env python3.6

'''
Lesson 6: Mailroom Part 3 Unit Test

'''

import os

import mailroom3 as mailroom

# so that object is there for the tests
mailroom.donors_db = mailroom.donors_db()


def test_existingdonors_list():
    listing = mailroom.existingdonors_list()
    assert listing.startswith("Donor list:\n")
    assert "manikaran chandok" in listing
    assert "simran kaur" in listing
    assert len(listing.split('\n')) == 5


def test_gen_letter():
    donor = ('manveen chandok', [10, 200, 65])
    letter = mailroom.gen_letter(donor)
    assert letter.startswith("Dear Manveen Chandok")
    assert letter.endswith("-The Team\n")
    assert "donation of $65.00" in letter


def test_generate_donor_report():
    report = mailroom.generate_donor_report()
    print(report)
    assert report.startswith("Donor Name          | Total Donation | Num Donation | Avg Donation")

    assert "Jasneet Paramjit           750.00$           3          250.00$" in report


def test_save_letters_to_disk():
    mailroom.save_letters_to_disk()
    assert os.path.isfile('simran_kaur.txt')
    assert os.path.isfile('manikaran_chandok.txt')
    with open('manikaran_chandok.txt') as f:
        size = len(f.read())
    assert size > 0


if __name__ == "__main__":
    test_existingdonors_list()
    test_gen_letter()
    test_generate_donor_report()
    test_save_letters_to_disk()
    print("All tests Passed")

