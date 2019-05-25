# from mailroom_4 import thanks
from mailroom_4 import thank_u_letter
# from mailroom_4 import take_total
from mailroom_4 import gen_stats_print
from mailroom_4 import table_header
# from mailroom_4 import letter4all
# from mailroom_4 import main_menu


# def test_thanks():
#     assert thanks() == '''
# Dear {},
#
# Thank you for generous donation of ${:.2f} to The Org!
#
# -The Org
#     '''

def test_thank_u_letter():
    assert thank_u_letter('x', 10) == ('''
Dear x,
           
Thank you for generous donation of $10.00 to The Org!
           
-The Org
    ''')


donors = {"Donny Donor": [100, 10, 45],
          "Gav Giver": [12, 16, 20],
          "Stingy Steve": [2, 5, 1],
          "Freaky Frank": [1200, 999, 1005],
          }


def take_total(item):  # used in conjunction with sorted() to take the donations and sort by total donation
    return item[1]

def test_table_header():
    assert table_header() == (
'''
Donor Name             _ Total Given _ Num Gifts _ Average Gift
''')


def test_gen_stats_print():
    assert gen_stats_print(donors) == ('''Freaky Frank           $    3204.00       3      $      1068.00
Donny Donor            $     155.00       3      $        51.67
Gav Giver              $      48.00       3      $        16.00
Stingy Steve           $       8.00       3      $         2.67
''')

