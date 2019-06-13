"""
Unit testing Mailroom Part4
FredBallyns
Session06
"""


import pytest, sys, os

import mailroom6 as mr


def test_standard_name():
    """
    Tests that standard name does care about case or spacing
    """
    assert mr.standard_name("James Bond") == mr.standard_name("James Bond   ")
    assert mr.standard_name("James Bond") == mr.standard_name("JamesBond")
    assert mr.standard_name("James Bond") == mr.standard_name("james bond")
    assert mr.standard_name("James Bond") != mr.standard_name("villian")

def test_requested_list():
    """
    Tests various forms of typing list are accepted as list
    """
    assert mr.requested_list("LIST") == True
    assert mr.requested_list("list") == True
    assert mr.requested_list("List") == True
    assert mr.requested_list("L") == True
    assert mr.requested_list("l") == True
    assert mr.requested_list("like") == False
    assert mr.requested_list("James") == False

def test_repeat_donor():
    """
    Checks if repeat donor, not case or space sensitive
    """
    assert mr.repeat_donor("James Bond") == True
    assert mr.repeat_donor("james bond") == True
    assert mr.repeat_donor("James Bond") == True
    assert mr.repeat_donor("Austin Powers") == False


def test_dict_donor_name():
    assert mr.dict_donor_name("james bond") == "James Bond"


def test_valid_donation():
    """
    Tests that dontation value is a positive integer
    """
    assert mr.valid_donation(100) == True
    assert mr.valid_donation(1) == True
    assert mr.valid_donation(0) == False
    assert mr.valid_donation(0.1) == False
    assert mr.valid_donation("Text") == False


def read_file(filename):
    """
    :returns: list of words in the file
    """
    lines=[]
    with open(filename) as text:
        for line in text:
            lines.append(line)
    return str(" ".join(lines))

def test_gen_report():
    start_text = "Donor Name      | Total Given | Num Gifts   |  Average Gift"
    first_part = len(start_text)
    output=mr.gen_report()
    print(type(output))
    assert output[:first_part] == start_text

def test_send_letters():
    """
    Tests files created
    """
    mr.send_letters()
    assert os.path.isfile('James Bond.txt')
    # check that it'snot empty and starts with dear
    message = read_file('James Bond.txt')
    size = len(message)
    assert size > 0
    assert message[:4] == "Dear"