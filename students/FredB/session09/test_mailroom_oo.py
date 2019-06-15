"""
tests mailroom
"""

from donors_models import Donor


def test_make_donor():
    d1 = Donor("Fred")
    assert d1.name == "Fred"


def test_donor_name_whitespace():
    d1 = Donor("Jake    ")
    assert d1.name == "Jake"


def test_standard_name():
    d1 = Donor("Jake    ")
    assert d1.standard_name == "jake"
    d2 = Donor("Jake Frost")
    assert d2.standard_name == "jakefrost"
    assert d2.standard_name != "villian"

def test_load_donations():
    d1 = Donor("Fred",[500])
    assert d1.donations == [500]
    d2 = Donor("Mike",[500, 1000])
    assert d2.donations == [500, 1000]
    d3 = Donor("Smith",["candy"])
    assert d3.donations == []
    assert d3.load_error == ["candy"]
    d4 = Donor("Santa",[1000,"candy"])
    assert d4.donations == [1000]
    assert d4.load_error == ["candy"]


def test_add_donation():
    d1 = Donor("Fred")
    d1.add_donation(5)
    d1.add_donation(10)
    assert d1.donations == [5,10]


def test_count_donation():
    d1 = Donor("Ricky", [9, 9, 9])
    assert d1.num_donations == 3
    d2 = Donor("zzzz", [1, 2])
    assert d2.num_donations == 2
    d3 = Donor("nothing", [])
    assert d3.num_donations == 0

def test_ave_donation():
    d1 = Donor("Rick", [9, 9, 9])
    assert d1.donations == [9,9,9]
    assert d1.ave_donation == 9
    d2 = Donor("zzzz", [1, 2, 3])
    assert d2.ave_donation == 2

def test_tot_donation():
    d1 = Donor("Ricky", [9, 9, 9])
    assert d1.tot_donation == 27
    d2 = Donor("zzzz", [1, 2])
    assert d2.tot_donation == 3
    d3 = Donor("nothing", [])
    assert d3.tot_donation == 0