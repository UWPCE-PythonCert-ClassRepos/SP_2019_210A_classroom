#! /usr/bin/env python3

import pytest

from mailroom import *

def test_add_donation():
    assert(add_donations())