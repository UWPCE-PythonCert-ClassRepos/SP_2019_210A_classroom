#!/usr/bin/env python3

# -----------------------------------------------------------------
# What: Lesson06: test_mailroom4.py
# Who: Brian Brumleve
# Date: June 08, 2019
# Change Description:
#      Adding some test to Mailroom4 code.
#
# -----------------------------------------------------------------

import mailroom4 as test_mailroom
import os


def test_donation_stats():
    result = test_mailroom.gen_donation_stats()
    assert "Guile", [1000, 589, 25000] in result
    assert "Blanca", [23, 1, 17] in result
    assert "Ken", [26592.00, 3, 8864] in result
    assert "M. Bison", [15000, 8000, 1200000] in result
    assert "Chun-Li", [61000000, 500000, 1200000] in result


def test_print_donor_list():
    result = test_mailroom.print_donor_list()
    assert "Guile" in result


# Add tests:
#  Adding a new donor
def test_new_donor_data():
    user = 'BrianB'
    # this function needs to be implemented
    new_donor = test_mailroom.select_donor(user)
    assert new_donor[0] == user
    assert new_donor[1] == []


#  Updating an existing donor
def test_amend_donor_data():
    user = "Guile"
    # this function needs to be implemented
    existing_donor = test_mailroom.select_donor(user)
    assert existing_donor[0] == user
    assert existing_donor[1] is not None


def validate_donor_in_stats(donor, list_of_lists):
    for sublist in list_of_lists:
        if donor in sublist:
            # if the item shows up in any of the sublists, it will return True
            return True
    # if the item is not in any of the sublists, it will return False
    return False


#  Print all thank you letters
def test_send_letter_to_all():
    # no parameter stats_list[0] necessary
    result = test_mailroom.gen_donation_stats()
    assert validate_donor_in_stats("Guile", result)
    assert validate_donor_in_stats("Blanca", result)
    assert validate_donor_in_stats("Ken", result)
    assert validate_donor_in_stats("M. Bison", result)
    assert validate_donor_in_stats("Chun-Li", result)

