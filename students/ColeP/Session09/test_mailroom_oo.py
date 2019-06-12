from mailroom_oo import *


def test_donors():
    a = Donor('Cole Phalen')
    print(a.donations)
    assert a.donations == []

    b = Donor('Mikey', 69)
    print(b.donations)
    assert b.donations == [69]


def test_add_donation():
    a = Donor('Marg Marty', 122)
    print(a.donations)
    assert a.donations == [122]

    a.add_donation(8)
    print(a.donations)
    assert a.donations == [122, 8]

    a.add_donation(99)
    print(a.donations)
    assert a.donations == [122, 8, 99]


def test_dictionary():
    a = Donor('Marg Marty', 122)
    a.add_donation(8)
    a.add_donation(99)
    print(a.dictionize())
    assert a.dictionize() == {'Marg Marty': [122, 8, 99]}


def test_dicionary2():
    donors = {"Donny Donor": [100, 10, 45],
              "Gav Giver": [12, 16, 20],
              "Stingy Steve": [2, 5, 1],
              "Freaky Frank": [1200, 999, 1005],
              }

    a = Donor('Marg Marty', 122)
    a.add_donation(55)
    b = Donor('Cole Phalen')
    b.add_donation(12)
    c = Donor('Mikey', 69)
    dct = {**a.dictionize(), **b.dictionize(), **c.dictionize(), **donors}
    print(dct)
    assert dct == {'Marg Marty': [122, 55], 'Cole Phalen': [12], 'Mikey': [69]}

    b.add_donation(10)
    c.add_donation(100)
    assert dct == {'Marg Marty': [122, 55], 'Cole Phalen': [12, 10], 'Mikey': [69, 100]}


def test_letter():
    a = Donor('Marg Marty', 122)
    a.add_donation(55)
    b = Donor('Cole Phalen')
    b.add_donation(12)
    c = Donor('Mikey', 69)
    dct = {**a.dictionize(), **b.dictionize(), **c.dictionize()}
    print(dct)

    le = StatsTable(dct)
    print(le.header())
    print(le.body())

    # assert False  # always Fails but allows tester to see if the output is satisfactory


def test_ty():
    a = Donor('Marg Marty', 122)
    a.add_donation(55)

    print(a.ty())

    assert False
    # assert a.ty() == '''
    #     Dear Marg Marty,
    #
    #     Thank you for your most recent donation of $55.00 to The Org!
    #
    #     -The Org'''


def test_thx4all():
    a = Donor('Marg Marty', 122)
    a.add_donation(55)
    b = Donor('Cole Phalen')
    b.add_donation(12)
    c = Donor('Mikey', 69)
    dct = {**a.dictionize(), **b.dictionize(), **c.dictionize()}
    print(dct)

    le = StatsTable(dct)
    le.thx4all()

    assert False


# def test_big_dict():
#     a = Donor('Marg Marty', 122)
#     a.add_donation(55)
#     b = Donor('Cole Phalen')
#     b.add_donation(12)
#     c = Donor('Mikey', 69)
#
#     d = MakeDict
#     print(d.big_dict(a.dictionize(), b.dictionize(), c.dictionize()))
#     assert False

# def test_donor_collection():
#     a = DonorCollection(Donor('Marty M'))

