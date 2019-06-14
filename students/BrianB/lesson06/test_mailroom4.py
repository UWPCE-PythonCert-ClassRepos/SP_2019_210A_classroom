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



