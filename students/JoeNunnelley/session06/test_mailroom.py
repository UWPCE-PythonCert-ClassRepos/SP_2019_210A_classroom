#! /usr/bin/env python3

"""

Send Thank You

Your unit tests should test the data manipulation
logic code: generating thank you text, adding or updating donors, and listing donors.

Create Report
 Then you can write a unit test for your data logic function.

Example:

def display_report():
    for row in get_report():
        print(row)

Here you would write a unit test for get_report function.

Send Letters

The unit test can assert that a file is created per donor entry
the file content contains text as expected.

Note that you should test the file creation separately from testing the
file content (that the correct text being generated). That way you don’t
need to read each file generated to know it contains correct text. So
the function that generates the text should be separate from the function
that writes the file.
"""
import glob
import mailroom
import os
import pytest
import sys
import tempfile
from unittest import mock


# Formulate Mail Tests
# 1. validate that the mail contains the proper Recipient name and Donations values
def test_formulate_mail():
    donor_in = ("Bob Smith", [100.00, 50.00])
    letter = mailroom.formulate_mail(donor_in, echo_terminal=False)
    print(letter)
    assert letter.startswith('Attn: Bob Smith')
    assert "100.00 USD" in letter
    assert "50.00 USD" in letter


# Add Donation Tests
# 1. validate that typing done returns true
@mock.patch('builtins.input')
def test_add_donations_done(mocked_input):
    mocked_input.return_value = "done"
    assert len(mailroom.add_donations()) == 0
    assert mailroom.add_donations() == []


# 2. validate that inputing a donation number adds to the donation set
@mock.patch('builtins.input')
def test_add_donations_appends(mocked_input):
    mocked_input.side_effect = ['20', 'done']
    result = mailroom.add_donations()
    assert len(result) == 1
    assert result[0] == 20.0


# 3. validate that inputing an invalid (non numeric) value produces the input guidance message
@mock.patch('builtins.input')
def test_add_donations_invalid_input(mocked_input, capsys):
    mocked_input.side_effect = ['a', 'done']
    result = mailroom.add_donations()
    assert len(result) == 0
    out,err=capsys.readouterr()
    assert 'Not a number. Please input positive numbers or "done"' in out
    assert len(err) == 0


# Print Report Tests
# 1. validate that the appropriately formatted list is printed
def test_print_report_formatting():
    expected_header = 'Donor Name              | Total Given  | Num Gifts  | Average Gift'
    row_format = '{:<24} ${:>13.2f} {:>12} ${:>13.2f}'
    report_width = 68
    raw_result, formatted_result = mailroom.print_report()

    assert formatted_result[0] == expected_header
    assert len(formatted_result[1]) == report_width
    assert len(formatted_result[-1]) == report_width

    for row in raw_result:
        expected_row = row_format.format(*row)
        assert expected_row in formatted_result


# 2. validate that the report is sorted correctly
def test_print_report_check_sorting():
    report_result = mailroom.print_report()[0]
    first_row = report_result[0]
    assert first_row[0] == 'Elmer Fudd'
    assert first_row[1] == 80730.00
    assert first_row[2] == 5
    assert first_row[3] == 16146.00


# Select Donor Tests
# 1. test that donor name 'list' prints a list
def test_select_donor_list():
    result = mailroom.select_donor('list')
    assert not result


# 2. test that providing an exsting name returns the correct information
def test_select_donor_existing_name():
    user = "George Jetson"
    existing_donor = mailroom.select_donor(user)
    assert existing_donor[0] == user
    assert len(existing_donor[1]) > 0


# 3. test that providing a non-existent name adds it to the list and returns correct information
def test_select_donor_new_name():
    user = 'Dave Barris'
    new_donor = mailroom.select_donor(user)
    assert new_donor[0] == user
    assert new_donor[1] == []


# Generate Thank You Tests
def file_contents_correct(destination_dir, donor_set):
    # check that each recipient is mentioned in a file
    # check that each recipient's donation are in that same file
    for donor_name, donations in donor_set.items():
        try:
            with open("{}/{}.txt".format(destination_dir, donor_name), 'r') as readfile:
                contents = readfile.read()
                assert donor_name in contents
        except IOError:
            print("File {}/{} not found".format(destination_dir, donor_name))
            assert False


# 1. validate that the files for each donor are written in the output directory
def test_generate_thankyou_files():
    destination_dir = tempfile.gettempdir()
    donor_files = [ "{}.txt".format(donor_name) for donor_name in mailroom.DONOR_SET ]
    mailroom.generate_thankyou_files(destination_dir)
    output_files = glob.glob('{}/*.txt'.format(destination_dir))
    assert len(output_files) > 0
    for donor_file in donor_files:
        assert "{}/{}".format(destination_dir, donor_file) in output_files

    for f in output_files:
        os.remove(f)


# 2. validate that the file contents are correct
def test_generate_thankyou_files_contents():
    destination_dir = tempfile.gettempdir()
    mailroom.generate_thankyou_files(destination_dir)
    output_files = glob.glob('{}/*.txt'.format(destination_dir))
    file_contents_correct(destination_dir, mailroom.DONOR_SET)

    for f in output_files:
        os.remove(f)