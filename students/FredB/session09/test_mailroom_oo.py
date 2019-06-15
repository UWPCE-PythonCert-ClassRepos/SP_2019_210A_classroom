"""
tests mailroom
"""

from donors_models import standardize_name, valid_donation, Donor, DonorCollection
from cli_main import requested_list

def test_standardize_name():
    assert standardize_name("Jake    ") == "jake"
    assert standardize_name("Jake Frost") == "jakefrost"
    assert standardize_name("Jake Frost") != "villian"

def test_valid_donation():
    assert valid_donation(10)
    assert valid_donation(1000)
    assert not valid_donation(-1000)
    assert not valid_donation(0)
    assert not valid_donation("crazy")

def test_make_donor():
    d1 = Donor("Fred")
    assert d1.name == "Fred"


def test_donor_name_whitespace():
    d1 = Donor("Jake    ")
    assert d1.name == "Jake"

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

def test_create_empty_db():
    db = DonorCollection()
    assert db.donors == {}

def test_empty_db():
    db =  DonorCollection()

def test_add_donor():
    db =  DonorCollection()
    db.add_donor(Donor("Rick", [9, 9, 9]))
    assert db.donors["rick"].donations == [9,9,9]
    db.add_donor(Donor("Bob", [1,2,3]))
    assert db.donors["bob"].donations == [1,2,3]
    assert db.donors["rick"].donations == [9,9,9]

def test_load_db():
    db =  DonorCollection([Donor("Rick", [9, 9, 9]),Donor("Bob", [1,2,3])])
    assert db.donors["bob"].donations == [1,2,3]
    assert db.donors["rick"].donations == [9,9,9]

def test_requested_list():
    """
    Tests various forms of typing list are accepted as list
    """
    assert requested_list("LIST") == True
    assert requested_list("list") == True
    assert requested_list("List") == True
    assert requested_list("L") == True
    assert requested_list("l") == True
    assert requested_list("like") == False
    assert requested_list("James") == False

def test_donor_present():
    db =  DonorCollection([Donor("Rick", [9, 9, 9]),Donor("Bob", [1,2,3])])
    assert db.donor_present("Rick")
    assert db.donor_present("boB")
    assert not db.donor_present("Carlos")

def test_name_list():
    db =  DonorCollection([Donor("Rick", [9, 9, 9])])
    assert db.name_list == ["Rick"]
    db =  DonorCollection([Donor("Rick", [9, 9, 9]),Donor("Other", [1, 3])])
    assert db.name_list == ["Rick","Other"]

def test_stats():
    db =  DonorCollection([Donor("Rick", [9, 9, 9])])
    assert db.stats == [("Rick",27,3,9)]
    db =  DonorCollection([Donor("Rick", [9, 9, 9]),Donor("Other", [1, 3])])
    assert db.stats == [("Rick",27,3,9),("Other",4,2,2)]


def test_stats_sort():
    db =  DonorCollection([Donor("Other", [1, 3]),Donor("Rick", [9, 9, 9])])
    assert db.stats_sorted == [("Rick",27,3,9),("Other",4,2,2)]