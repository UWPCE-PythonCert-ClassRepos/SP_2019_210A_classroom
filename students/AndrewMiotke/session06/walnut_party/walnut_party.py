#!/usr/bin/env python3

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    if walnuts <= 30 and is_weekend == False:
        return False
    elif walnuts <= 30 and is_weekend == True:
        return False
    elif walnuts == 39 and is_weekend == True:
        return False
    elif walnuts == 39 and is_weekend == False:
        return False
    elif walnuts > 60 and is_weekend == False:
        return False
    else:
        return True