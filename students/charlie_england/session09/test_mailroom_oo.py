from donor_models import Donor
from donor_models import Donor_Collection

def test_donor():
    #test to make sure new donor can be created and that values should all be 0
    no_amt = Donor("Jack")
    assert no_amt.name == "Jack"
    assert no_amt.total == 0
    assert no_amt.average == 0
    assert no_amt.num_donations == 0
    #test that there can be an amount added
    no_amt.add_donation(10000)
    assert no_amt.total == 10000
    no_amt.add_donation(10000)
    #make sure the total, number of donations and average amount is updated correctly
    assert no_amt.total == 20000
    assert no_amt.num_donations == 2
    assert no_amt.average == 10000
    assert no_amt.send_thank_you() == (
    """Dear Jack,\n\n 
            On behalf of Local Charity we would like to extend our sincerest thanks for your $10,000.00 donation.\n
            Without people like you we could not continue blah blah blah.\n
            You have given us a total of $20,000.00 over 2 donation(s) with an average of $10,000.00 per donation!
            Again thank you\n
        Sincerely,\n
            Local Charity """
    )

def test_donor_collection():
    #make sure a new donor_collection instance can be created with no inputs
    no_donors = Donor_Collection()
    assert no_donors.donor_data == {}
    #test to make sure the donor_collection instance can be added to with a list of donor objects
    donors = Donor_Collection([Donor('Jack',[1000,2000,3000])])
    #test to make sure that the donor name "Jack" appears in the search_donor function
    assert donors.search_donor("Jack")
    donors.add_donor(Donor("Pepe",[500,200,100]))
    assert donors.search_donor("Pepe")

def test_donor_collection_gen_report():
    donors = Donor_Collection([Donor("Jack",100)])
    assert "".join(donors.gen_report()[1].lower().strip().replace(" ","")) == "jack$100.001$100.00"

def test_donor_collection_send_letters():
    donors = Donor_Collection([Donor("Jack",100)])
    assert donors.send_letters()[0][0].lower().strip().replace(" ","") == 'dearjack,\n\n\nonbehalfoflocalcharitywewouldliketoextendoursincerestthanksforyourmostrecent$100.00donation.\n\nwithoutpeoplelikeyouwecouldnotcontinueblahblahblah\n\novertimeyouhavegivenusatotalof$100.00over1donation(s)whichaveragesoutto$100.00perdonation!\n\nagainthankyou\n\nsincerely,\n\nlocalcharity'