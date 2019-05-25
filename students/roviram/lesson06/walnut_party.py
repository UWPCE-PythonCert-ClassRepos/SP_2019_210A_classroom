#!/usr/bin/env python
#---------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Week 6 Homework
# Script Name: Walnut Party
# Script Creation Date: Saturday 5/18/2019
#---------------------------------------------------#
"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    return (is_weekend is True and walnuts >= 40) or (is_weekend is False and (40 <= walnuts <= 60))









