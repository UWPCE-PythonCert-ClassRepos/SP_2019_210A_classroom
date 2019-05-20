"""
tests for mailroom
"""


import mailroom_part4

def test_thank_you_inputs():
    #test to make sure new name will input with the correct value
    assert mailroom_part4.thank_you("Jack",1000) == """Dear Jack,\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your $1,000.00 donation.\n
        Without people like you we could not continue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """
    #test to make sure a name currently in donors will output with the correct values
    assert mailroom_part4.thank_you("Nick Nilly",250) == """Dear Nick Nilly,\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your $250.00 donation.\n
        Without people like you we could not continue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """

def test_compose_thank_you():
    pass

def test_report():
    pass

def test_make_letters():
    pass

def test_main_menu():
    pass
