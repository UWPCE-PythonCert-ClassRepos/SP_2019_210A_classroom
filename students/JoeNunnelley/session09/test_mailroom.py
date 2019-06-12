#! /usr/bin/env python3

"""
Unit Test for Mailroom Project

Formulate Thank You Letters Tests:
- 1. test_formulate_mail : validate that the mail contains the proper Recipient
     name and Donations values for a newly created donor
- 2. test_generate_thankyou_files : validate that the files for each donor are
     written in the output directory
- 3. test_generate_thankyou_files_contents : validate that the file contents
     are correct

Add Donation Tests:
- 1. test_add_donations_done : validate that typing done returns true
- 2. test_add_donations_appends : validate that inputing a donation number
     adds to the donation set
- 3. test_add_donations_invalid_input : validate that inputing an invalid (non numeric)
     value produces the input guidance message

Create Report Tests:
- 1. test_print_report_formatting : validate that the appropriately formatted list is
     printed
- 2. test_print_report_check_sorting : validate that the report is sorted correctly

Select Donor Tests:
- 1. test_select_donor_list : test that donor name 'list' prints a list
- 2. test_select_donor_existing_name : test that providing an exsting name returns the
     correct information
- 3. test_select_donor_new_name : test that providing a non-existent name adds it to the
     list and returns correct information

Verify Basic Class Functions:
- 1. verify the donation class
- 2. verify the donor class
- 3. verify the donorcollection class
"""
import datetime
import glob
from unittest import mock
import os
import tempfile

import cli_main
import donor_models as dm


# Formulate Mail Tests
def test_formulate_mail():
    """
    Verify that given a donor, the letter generated contains that
    user's information
    """
    donor_in = dm.Donor("Bob Smith", [100.00, 50.00])
    letter = cli_main.formulate_mail(donor_in, echo_terminal=False)
    print(letter)
    assert letter.startswith('Attn: Bob Smith')
    assert "100.00 USD" in letter
    assert "50.00 USD" in letter


def test_generate_thankyou_files():
    """
    Verify that the thank you letters are created for each donor
    and saved to the correct location
    """
    destination_dir = tempfile.gettempdir()
    donor_files = ["{}.txt".format(donor.name) for donor in cli_main.DONOR_SET.donors]
    cli_main.generate_thankyou_files(destination_dir)
    output_files = glob.glob('{}/*.txt'.format(destination_dir))
    assert output_files is not None
    for donor_file in donor_files:
        assert "{}/{}".format(destination_dir, donor_file) in output_files

    for output_file in output_files:
        os.remove(output_file)


def test_generate_thankyou_files_contents():
    """
    Verify that the thank you files contain the appropriate
    contents for all donors in the list
    """
    destination_dir = tempfile.gettempdir()
    cli_main.generate_thankyou_files(destination_dir)
    output_files = glob.glob('{}/*.txt'.format(destination_dir))

    for donor in cli_main.DONOR_SET.donors:
        try:
            with open("{}/{}.txt".format(destination_dir, donor.name), 'r') as readfile:
                contents = readfile.read()
                # check that each recipient is mentioned in a file
                assert donor.name in contents

                # check that each recipient's donation are in that same file
                for donation in donor.donations:
                    assert "{:,.2f} USD".format(donation) in contents

        except IOError:
            print("File {}/{} not found".format(destination_dir, donor.name))
            assert False

    for output_file in output_files:
        os.remove(output_file)


# Add Donation Tests
@mock.patch('builtins.input')
def test_add_donations_done(mocked_input):
    """
    Verify that inputing 'done' when adding donations,
    the set of donations is unchanged
    """
    mocked_input.return_value = "done"
    assert cli_main.add_donations() is not None
    assert cli_main.add_donations() == []


@mock.patch('builtins.input')
def test_add_donations_appends(mocked_input):
    """
    Verify that inputing a donation in the UI successfully
    adds that donation to the donations list
    """
    mocked_input.side_effect = ['20', 'done']
    result = cli_main.add_donations()
    assert len(result) == 1
    assert result[0] == 20.0


@mock.patch('builtins.input')
def test_add_donations_invalid_input(mocked_input, capsys):
    """
    Verify that giving the add donations function an invalid (non-numeric)
    input results in the proper error message to the user
    """
    mocked_input.side_effect = ['a', 'done']
    result = cli_main.add_donations()
    assert result is not None
    out, err = capsys.readouterr()
    assert 'Not a number. Please input positive numbers or "done"' in out
    assert err == ''


# Print Report Tests
def test_print_report_formatting():
    """
    Verify that the donor report output to the console is
    correctly formatted given the expected header and row format
    definitions
    """
    expected_header = 'Donor Name              | Total Given  | Num Gifts  | Average Gift'
    row_format = '{:<24} ${:>13.2f} {:>12} ${:>13.2f}'
    report_width = 68
    raw_result, formatted_result = cli_main.print_report()

    assert formatted_result[0] == expected_header
    assert len(formatted_result[1]) == report_width
    assert len(formatted_result[-1]) == report_width

    for row in raw_result:
        expected_row = row_format.format(*row)
        assert expected_row in formatted_result


def test_print_report_check_sorting():
    """
    Verify that the printed donations report has the correctly sorted
    top element thereby proving that the sorting function is being called
    and operating correctly
    """
    report_result = cli_main.print_report()[0]
    first_row = report_result[0]
    assert first_row[0] == 'Elmer Fudd'
    assert first_row[1] == 80730.00
    assert first_row[2] == 5
    assert first_row[3] == 16146.00


# Select Donor Tests
def test_select_donor_list():
    """
    Verify that when selecting a donor, inputing 'list'
    returns no donor
    """
    result = cli_main.select_donor('list')
    assert not result


def test_select_donor_existing_name():
    """
    Verify that when selecting a donor and asking for
    an existing donor, that donor's details are returned
    """
    user = "George Jetson"
    existing_donor = cli_main.select_donor(user)
    assert existing_donor.name == user
    assert existing_donor.donations is not None

@mock.patch('builtins.input')
def test_select_donor_new_name(mocked_input):
    """
    Verify that when selecting a donor and asking for
    a non-existent donor, that donor is added and its
    details are returned. User name is correct and
    donation history is empty.
    """
    mocked_input.side_effect = ['y', '20', 'done']
    user = 'Dave Barris'
    new_donor = cli_main.select_donor(user)
    assert new_donor.name == user
    assert new_donor.donations[0] == 20


def test_donation_class():
    """Verify basic operations of the donation class"""
    donation_amount = 20
    donation = dm.Donation(donation_amount)
    assert donation.amount == float(donation_amount)
    assert donation.date.year == datetime.datetime.now().year


def test_donor_class():
    """Verify basic operations of the donation class"""
    donor = dm.Donor('Joe Nunnelley', [20, 40])
    assert donor.key == 'joenunnelley'
    assert donor.name == 'Joe Nunnelley'
    assert len(donor.donations) == 2

def test_donorcollection_class():
    """Verify basic operations of the donation class"""
    donors = dm.DonorCollection()
    donors.add(dm.Donor('Joe Nunnelley', [20, 40]))
    donors.add(dm.Donor('Mary Margaret', [30, 50]))
    assert donors.get_donor('Joe Nunnelley').name == 'Joe Nunnelley'
    assert len(donors.get_donor('Mary Margaret').donations) == 2
    donors.delete('Joe Nunnelley')
    assert len(donors.donors) == 1
    assert donors.get_donor('Mary Margaret').name == 'Mary Margaret'
