import pytest
from donors_model import Donor, DonorList

def test_donor_list():
    donor_list = DonorList()

    # Checks for an empty dictionary
    assert donor_list.donor_data == {}


def test_normalize_name():
    donor = Donor("Gus")

    # Checks that the name is transformmed to lower case
    assert donor.normalize_name("Gus") == "gus"
