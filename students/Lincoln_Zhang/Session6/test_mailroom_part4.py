#!/usr/bin/env python3

import mailroom_part4, os
import unittest.mock

def test_gen_letter():
    result = mailroom_part4.gen_letter("Bob", 11.2)
    assert result.startswith("\nDear Bob")
    assert result.find("11.2")

def test_Mail_to_donors():
    mailroom_part4.Mail_to_donors({"Bob":[11.2]})
    file_path = os.path.join(os.getcwd(),"letters.txt")
    expanded_file_path = os.path.expanduser(file_path)
    assert os.path.isfile(file_path)
    assert os.path.isfile(expanded_file_path)

def test_find_donor():
    result = mailroom_part4.find_donor("Bob",11.2)
    assert "Bob" in result.keys()
    assert result["Bob"] == [11.2]
    assert result["Fred Flintstone"] == [100, 200, 50]

@unittest.mock.patch('builtins.input')
def test_Thank_You():
    
    result = mailroom_part4.Thank_You()
    unittest.mock.patch('builtins.input', return_value="y")
    unittest.mock.patch('builtins.input', return_value="Bob")
    unittest.mock.patch('builtins.input', return_value=11.2)

    with mock.patch('builtins.input', return_value="y"):
        assert from_user.user_donation() == True
        if from_user.user_donation():
            with mock.patch('builtins.input', return_value="bob"):
                assert donor_name == "Bob"
                assert builtins.output == "Please tell me how much you would like to donate: "
            with mock.patch('builtins.input', return_value=11.2):
                assert donation_amount == 11.2
        else:
            with mock.patch('builtins.input', return_value="n"):
                assert from_user.user_donation() == False

    file_path = os.path.join(os.getcwd(),"Bob.txt")
    expanded_file_path = os.path.expanduser(file_path)
    assert os.path.isfile(file_path)
    assert os.path.isfile(expanded_file_path)
    assert result["Bob"] == [11.2]

def test_gen_stats():
    result = mailroom_part4.gen_stats([1,2,3])
    #the third element has special format
    assert result[:2] == (6,3)

# def test_gen_report():
#     #mailroom_part4.gen_report({"Bob":[11.2]})
#     #for function doesn't have return value, how to test it
#     assert mailroom_part4.gen_report({"Bob":[11.2]}).header == "Donor Name            | Total Given |  Num Gifts  | Average Gift"