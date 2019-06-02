#!/usr/bin/env python3

import MailRoom
import os


def test_initalize_donor_db():
    """
    Ensure initial seed values are present after initializing donor database
    :return: PASS/FAIL assertion
    """
    result = MailRoom.initalize_donor_db()
    assert result == {
        'Brian Ervin': [100.57, 200.63, 350.47],
        'Steve Walline': [300.55, 500.14, 443.80],
        'Mike Tomson': [100.25, 300.12, 543.45],
        'Michelle Anderson': [700.67, 1300.56, 154],
        'Matt Anderson': [224.34, 600.50, 5000.12]}


 # Will need to be updated once donors DB data is persistent and/or not initialized with the same values
def test_list_donors():
    """
    Ensure list_donors() returns as expected
    :return: PASS/FAIL assertion
    """
    result = MailRoom.list_donors(MailRoom.initalize_donor_db())
    assert 'Brian Ervin' in result
    assert 'Steve Walline' in result
    assert 'Mike Tomson' in result
    assert 'Michelle Anderson' in result
    assert 'Matt Anderson' in result


def test_generate_email():
    """
    Ensure generate_email creates an email as expected
    :return: PASS/FAIL assertion
    """
    result = MailRoom.generate_email(donor='Brian Ervin', recent_donation_amount=350.47)
    assert result.startswith("Dear Brian Ervin")
    assert "recent donation of $350.47" in result
    assert len(result) == 156


def test_generate_all_thankyou_emails():
    """
    Ensure thank-you email files are generated properly
    :return: PASS/FAIL assertion
    """
    test_db = {
        'Brian Ervin': [100.57, 200.63, 350.47],
        'Steve Walline': [300.55, 500.14, 443.80],
        'Mike Tomson': [100.25, 300.12, 543.45],
        'Michelle Anderson': [700.67, 1300.56, 154],
        'Matt Anderson': [224.34, 600.50, 5000.12]}
    MailRoom.generate_all_thankyou_emails(test_db)
    for donor in test_db:
        assert os.path.isfile(donor+".txt")


def test_generate_report():
    """
    Ensure donor report is generated properly
    :return: PASS/FAIL assertion
    """
    test_db = {
        'Brian Ervin': [100.57, 200.63, 350.47],
        'Steve Walline': [300.55, 500.14, 443.80],
        'Mike Tomson': [100.25, 300.12, 543.45],
        'Michelle Anderson': [700.67, 1300.56, 154],
        'Matt Anderson': [224.34, 600.50, 5000.12]}
    result = MailRoom.generate_report(test_db)
    assert result.startswith('| Donor Name          | Total Donated | Num Gifts | Average Gift')
    assert '| Brian Ervin         |        651.67 |          3|     217.22 |' in result
    assert '| Matt Anderson       |       5824.96 |          3|    1941.65 |' in result

