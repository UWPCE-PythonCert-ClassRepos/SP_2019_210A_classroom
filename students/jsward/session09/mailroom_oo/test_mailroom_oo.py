#!/usr/bin/env python

from donor_models import Donor, DonorCollection
import pytest

##################
# Test Donor class
##################


def test_create_donor():
    donor = Donor('first last')
    assert isinstance(donor, Donor)


def test_str():
    donor = Donor('first last')
    assert str(donor) == 'first last'


def test_weird_name():
    donor = Donor(88)
    assert donor.name == '88'


def test_create_donor_w_int_dono():
    donor = Donor('first last', 10)
    assert donor.name == 'first last'
    assert donor.donations == [10]


def test_create_donor_w_tuple_donos():
    donor = Donor('first last', (10, 20.22))
    assert donor.name == 'first last'
    assert donor.donations == [10, 20.22]


def test_create_donor_w_list_donos():
    donor = Donor('first last', [10, 20.22])
    assert donor.name == 'first last'
    assert donor.donations == [10, 20.22]


def test_add_donation():
    donor = Donor('first last')
    donor.add_donation(50)
    assert donor.donations == [50]


def test_add_donation_with_dollar_sign():
    donor = Donor('first last')
    donor.add_donation('$50.00')
    assert donor.donations == [50]


def test_add_donation_with_comma():
    donor = Donor('first last')
    donor.add_donation('50,000.00')
    assert donor.donations == [50000]


def test_add_donation_with_space():
    donor = Donor('first last')
    donor.add_donation(' 50')
    assert donor.donations == [50]


def test_add_negative_donation():
    donor = Donor('first last')
    with pytest.raises(ValueError):
        donor.add_donation(-50)


def test_add_donation_err():
    donor = Donor('first last')
    with pytest.raises(ValueError):
        donor.add_donation('asdf')


def test_stats():
    donor = Donor('first last')
    donor.add_donation(50)
    donor.add_donation(16.73)
    donor.add_donation(33.22)
    donor.add_donation(.45)
    assert donor.stats == ['first last', 100.4, 4, 25.1]


def test_stats_no_donos():
    donor = Donor('first last')
    assert donor.stats == ['first last', 0, 0, 0]


def test_tyl_no_donos():
    donor = Donor('first last')
    assert donor.thank_you_letter == "Dear first last, we look forward to your first donation!"


def test_tyl_with_donos():
    donor = Donor('first last')
    donor.add_donation(1)
    donor.add_donation(2)
    assert donor.thank_you_letter == "Dear first last, thank you for the very generous donation of $2.00.  " \
                              "Rest assured it will be put to good use helping those in need*\n" \
                              "    *After deducting 98% for management overhead, of course ;)."


############################
# Test DonorCollection class
############################


def test_create_donor_collection():
    dc = DonorCollection()
    assert isinstance(dc, DonorCollection)


def test_add_donor():
    dc = DonorCollection()
    dc.add_donor('first last')
    assert len(dc.donors) == 1


def test_add_existing_donor():
    dc = DonorCollection()
    dc.add_donor('first last')
    with pytest.raises(ValueError):
        dc.add_donor('first last')
    assert len(dc.donors) == 1


def test_donor_list():
    dc = DonorCollection()
    dc.add_donor('first last')
    dc.add_donor('second name')
    assert dc.donor_list == ['First Last', 'Second Name']


def test_letters_to_all_donors():
    dc = DonorCollection()
    dc.add_donor('first last')
    dc.add_donor('second name')
    assert dc.letters_to_all_donors == ["Dear First Last, we look forward to your first donation!",
                                        "Dear Second Name, we look forward to your first donation!"]


def test_donor_report():
    dc = DonorCollection()
    dc.add_donor('first last', (1, 2, 3))
    dc.add_donor('second name', (4, 5, 6))
    assert dc.donor_report == [['First Last', 6, 3, 2], ['Second Name', 15, 3, 5]]
