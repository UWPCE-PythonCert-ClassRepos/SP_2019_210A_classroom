import pytest
import os.path
from donor_models import Donor
from donor_models import DonorCollection


class TestDonor:
    def test_ctor(self):
        donor = Donor("First Last")
        assert donor.name == "First Last"
        assert donor.donations == []

        donations = [123.123, 456.456]
        donor = Donor("First Last", donations)
        assert donor.name == "First Last"
        assert donor.donations == donations

    def test_normalize_name(self):
        assert Donor.normalize_name("   ABC efg  ") == "abcefg"

    def test_add_donation(self):
        donor = Donor("First Last")
        donor.add_donation("not a float")
        assert not donor.donations
        letter = donor.add_donation("100.1")
        assert "100.1" in letter
        assert "Dear First Last" in letter

    def test_add_donations(self):
        donor = Donor("mydonor")
        donations = []
        donor.add_donations(donations)
        assert not donor.donations

        donations = [222.2, 333.4, 555.2]
        donor.add_donations(donations)
        assert donor.donations == donations

    def test_properties(self):
        donor = Donor("testdonor")
        donations = [123, 231, 444.7]
        donation_sum = sum(donations)
        donation_avg = donation_sum / len(donations)
        donor.add_donations(donations)
        assert donor.donor_name == "testdonor"
        assert donor.donation_sum == donation_sum
        assert donor.donation_avg == donation_avg

    def test_gen_stats(self):
        donor = Donor("testdonor")
        donations = [123, 231, 444.7]
        donation_sum = sum(donations)
        donation_avg = donation_sum / len(donations)
        donor.add_donations(donations)
        assert ("testdonor", donation_sum, len(donations), donation_avg) == donor.gen_stats()


class TestDonorCollection:
    def test_ctor(self):
        dc = DonorCollection()
        assert not dc.donor_data
        first_donor = Donor("firstDonor")
        second_donor = Donor("secondDonor")
        dc = DonorCollection([first_donor, second_donor])
        assert {first_donor.norm_name: first_donor, second_donor.norm_name: second_donor} == dc.donor_data

    def test_list_donors(self):
        first_donor = Donor("firstDonor")
        second_donor = Donor("secondDonor")
        dc = DonorCollection([first_donor, second_donor])
        assert "{0}, {1}".format(first_donor.norm_name, second_donor.norm_name) == dc.list_donors()

    def test_add_donor(self):
        dc = DonorCollection()
        dc.add_donor("first")
        assert "first" in dc.donor_data.keys()
        assert len(dc.donor_data) == 1
        dc.add_donor("first")
        assert "first" in dc.donor_data.keys()
        assert len(dc.donor_data) == 1
        dc.add_donor("second")
        assert "first" in dc.donor_data.keys()
        assert "second" in dc.donor_data.keys()
        assert len(dc.donor_data) == 2

    def test_add_donations(self):
        dc = DonorCollection()
        dc.add_donation("first", [111, 222, 333])
        dc.add_donation("first", [444])
        dc.add_donation("second", [555])
        assert "first" in dc.donor_data.keys()
        assert "second" in dc.donor_data.keys()
        assert len(dc.donor_data) == 2
        assert [111, 222, 333, 444] == dc.donor_data["first"].donations
        assert [555] == dc.donor_data["second"].donations

    def test_find_donor(self):
        dc = DonorCollection()
        dc.add_donor("first")
        dc.add_donor("second")
        assert dc.find_donor("first").name == "first"
        assert dc.find_donor("second").name == "second"
        assert not dc.find_donor("noSuchDonor")

    def test_generate_report(self):
        dc = DonorCollection()
        dc.add_donation("first", [111, 222, 333])
        dc.add_donation("second", [555])
        report = dc.generate_report()
        assert "first" in report
        assert "second" in report
        assert "666" in report # sum of first
        assert "222" in report # sum of first
        assert "3" in report # len of first
        assert "555" in report # sum, avg of second
        assert "1" in report # len of second

    def test_generate_thank_you_letters(self):
        dc = DonorCollection()
        dc.add_donation("first", [111, 222, 333])
        dc.add_donation("second", [555])
        dc.generate_thank_you_letters("testDir")
        os.path.isfile("testDir\\first.txt")
        os.path.isfile("testDir\\second.txt")
        with open("testDir\\first.txt", "r") as f:
            content = f.read()
            assert "first" in content
            assert "666" in content
        with open("testDir\\second.txt", "r") as f:
            content = f.read()
            assert "second" in content
            assert "555" in content

