"""Test for mailroom"""
import pytest
import mailroom


def test_donor_list():
    database = mailroom.donors_list

    assert "Rufio" in database
    assert "Gus" in database
    assert "Spike" not in database


def test_get_donor_not():
    donor = mailroom.get_donor("Lemon")

    assert donor is None


def test_send_thank_you_letter():
    donor = ("Rufio", [897, 200 , 200])
    letter = mailroom.thank_you_letter(donor)

    assert "Rufio" in letter
    assert "$200" in letter


def test_add_donor():
    donor_name = "Lemon    "
    donor_to_add = mailroom.add_donor(donor_name)
    # database = mailroom.donors_list

    assert donor_to_add == ("Lemon", [])