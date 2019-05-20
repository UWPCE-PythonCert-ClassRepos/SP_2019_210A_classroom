"""
tests for mailroom
"""


import mailroom_part4

def test_thank_you_inputs():
    """
    this test will test the output string to make sure that it outputs correctly if a new name is entered or if the name is already in the donors section
    """
    #test to make sure new name will input with the correct value
    assert mailroom_part4.thank_you("Jack",1000,"y") == """Dear Jack,\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your $1,000.00 donation.\n
        Without people like you we could not continue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """
    #test to make sure a name currently in donors will output with the correct values
    assert mailroom_part4.thank_you("Nick Nilly",250,"n") == """Dear Nick Nilly,\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your $250.00 donation.\n
        Without people like you we could not continue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """

def test_report():
    assert mailroom_part4.report("y")[0] == "Donor Name           |    Total Given    | Num Gifts | Average Gift\n------------------------------------------------------------"
    assert mailroom_part4.report("y")[1] == "Chris Christly       $          1,251.01      2       $     625.50"

def test_make_letters():
    mailroom_part4.make_letters()
    expected = """Dear Jose Hooray,

 
        On behalf of Local Charity we would like to extend our sincerest thanks for your $750000 donation.

        Without people like you we could not continue blah blah blah

        Over time you have given us a total of $2,250,000.00 over 3 donation(s) which averages out to $750,000.00 per donation! 

        Again thank you

    Sincerely,

        Local Charity """
    lines = []
    with open("Jose Hooray.txt") as txt_file:
        lines.extend(txt_file.readlines())
    print(lines)
    output = "".join(lines)
    assert output == expected

