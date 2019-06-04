import pytest
import os
from MailroonPart4 import donors, addDonation, genThankYouLetter, report, gen_thank_you_letters

def test_genReport():
    output = report().split("\n")
    assert "{:<20}{:<20}{:<15}{:<20}".format("Donor Name", "|Total Given", "|Num Gifts", "|Average Gift") == output[0]
    assert "-------------------------------------------------------------------" == output[1]
    assert "Jeff Bezos          $750.00              3              $250.00              " == output[2]

def test_genThankYouLetters():
    gen_thank_you_letters(donors)
    for name, amount in donors.items():
        firstLastName = name.split(" ")
        print(firstLastName)
        with open("{0}_{1}.txt".format(firstLastName[0], firstLastName[1]), "r") as f:
            content = f.read()
            assert '''
            Dear {0},
                    Thank you for your very kind donation of ${1:.2f}.

                    It will be put to very good use.

                                        Sincerely,
                                            - The Team'''.format(name, sum(amount)) == content

def test_addDonation():
    # Add amount to existing donor
    for name, donations in donors.items():
        prevDonations = len(donations)
        addDonation(name, 123.456)
        assert len(donations) == prevDonations + 1
        assert donations[-1] == 123.456

    # Add new name
    addDonation("NoSuchPerson", 111.11)
    assert len(donors["NoSuchPerson"]) == 1
    assert [111.11] == donors["NoSuchPerson"]

def test_genThankYouLetter():
    assert '''
    Dear abc,
    Thank you for donating 123.456!\n''' == genThankYouLetter("abc", 123.456)



