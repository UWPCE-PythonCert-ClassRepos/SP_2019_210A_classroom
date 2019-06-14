import os
from mailroom import Donor


def test_donor_name():
    donor = Donor("Road Runner")

    assert donor.name == "Road Runner"


def test_add_donation():
    donor = Donor("Road Runner")

    donor.add_donation(4839283.32)

    assert donor.num_donations == 1


def test_send_thanks():
    pass


def test_donorDB():
    db = DonorDB()

    db.add_donation(Donation("Bob"))

    db.avg_by_donor()

    db.total_donations()





# def get_donors_db():
#     donors = {'Bill Gates': [1000, 2000, 3000],
#               'Rick James': [5000, 5000, 6000, 3000],
#               'James Brown': [4000, 10000, 9000, 12000],
#               'Prince': [5500, 6500, 7000, 12000],
#               'Cat Williams': [2000, 3000, 1000]}
#     return donors


# def test_get_donors_db():
#     # test that the database function returns a full database
#     donors = get_donors_db()
#     assert len(donors) != 0
#     assert len(create_report(donors)) == len(donors)


# def test_everyone():
#     donors = get_donors_db()
#     # tests that a file was created for each donor emailed
#     everyone(donors)
#     for i in donors:
#         assert os.path.exists(i + ".txt")
