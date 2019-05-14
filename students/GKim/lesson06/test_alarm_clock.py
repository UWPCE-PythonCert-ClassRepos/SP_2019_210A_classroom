

"""
test code from alarm clock example on coding bat

Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"
and on the weekend it should be "10:00". Unless we are on vacation -- 
then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

"""

# you can change this import to test different versions
from alarm_clock import alarm_clock



def test_1():
    assert alarm_clock(1, False) == "7:00"


def test_2():
    assert alarm_clock(5, False) == "7:00"


def test_3():
    assert alarm_clock(0, False) == "10:00"


def test_4():
    assert alarm_clock(6, False) == "10:00"


def test_5():
    assert alarm_clock(0, True) == "off"


def test_6():
    assert alarm_clock(6, True) == "off"


def test_7():
    assert alarm_clock(1, True) == "10:00"


def test_8():
    assert alarm_clock(3, True) == "10:00"


def test_9():
    assert alarm_clock(5, True) == "10:00"


