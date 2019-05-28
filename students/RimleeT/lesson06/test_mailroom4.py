import os
import mailroom4 as mailroom

def test_find_donor():
    donor_name = mailroom.find_donor("Jeff Bezos", 100)
    donation = mailroom.donor_db.get("Jeff Bezos") 
    assert donation != None
    assert 877.33 in donation
    assert 100 in donation

	
def test_do_create_report():
    report = mailroom.gen_stats("Rimlee", [10.0, 20.0])
    assert "Rimlee                  $         30.0              2     $        15.0" in report


'''
def test_do_sendlettertoalldonors():
    mailroom.do_sendlettertoalldonors()
    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('William_Gates_III.txt')
    # check that it'snot empty:
    with open('William_Gates_III.txt') as f:
        size = len(f.read())
    assert size > 0

'''
if __name__ == "__main__":
    test_find_donor()
    test_do_create_report()
    print("All tests Passed")

