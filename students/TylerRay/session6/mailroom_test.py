import pytest
import mailroom_4 as mr


def test_donor_list():
    '''
    This test asserts that known values are indeed included in the database
    '''
    database = mr.get_donor_db()

    assert "Alpha Beta" in database
    assert "Tucker Jones" in database
    assert "Vladimir Putin" not in database

def test_get_donor_not():
    '''
    In conjunction with test_donor_list() this affirms that names not included in the database are in face not included
    '''
    donor = mr.find_donor("Tyler")

    assert donor is None


def test_report():
    '''
    Checks to see if the gen_donor_report() outputs as expected
    :return:
    '''
    result = mr.gen_donor_report()

    assert "Vladmir Putin               $1500000.00           3   $  500000.00" in result


def test_thank_you_letter():
    '''
    Testing to see if the letter outputs as expected with the two variables (name and $)
    :return:
    '''
    donor = ("Tucker Jones", [800])
    letter = mr.gen_letter(donor)

    assert letter.startswith("Dear Tucker Jones")
    assert letter.startswith("Hi Tucker Jones") is False
    assert "$800" in letter
