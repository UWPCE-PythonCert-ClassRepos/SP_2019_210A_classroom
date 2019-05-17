"""Test for mailroom"""
import pytest
import mailroom as mr

def test_thank_you_letter():
    letter = mr.thank_you_letter(("Rufio", [897, 200, 200]))

    # Break the letter down testing the name and value amount.
    # The rest of the letter is trivial
    assert letter.startswith == "Hi Rufio"
