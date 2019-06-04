#------------------- Script Details--------#
# Week 6 Homework: Testing Mailroom Part 4
# Miguel Rovira-Gonzalez, 5/19/19
#-------------------------------------------#

"""Testing Methods from Mailroom 4"""
import mailroom_part_4 as mailroom


def test_gen_stats():
    result = mailroom.gen_stats()
    assert ["Pepper", 125, 3, 41.67] in result
    assert ["Cristina Rovira", 150, 3, 50.0] in result


def test_send_letters():
    result = mailroom.send_letters()
    for donor_name in mailroom.donors:
        expected = f"""Dear {donor_name},
Thank you for your most recent generous donation of ${mailroom.donors[donor_name][-1]}.

Sincerely,

The Mailroom Team"""
        with open(f"{donor_name}.txt", "r") as donor_txt_file:
            assert expected in donor_txt_file.read()


def test_send_thank():
    """This is testing the donor exists in my donors diotionary based off my send thank you method"""
    result = mailroom.donors
    assert "Miguel Rovira" in result
    assert "Pepper" in result
    assert "Cristina Rovira" in result
    assert "Coffee" not in result






