#!/usr/bin/env python

import sys

print("in mailroom")

donors = [("Fred Flintstone", [100, 200, 50]),
          ("Barney Rubble", [100, 50, 600]),
          ("Wilma Flintstone", [1000, 50, 600, 200]),
          ("Pebbles Flintstone", [10, 5, 6]),
          ]


def thank_you():
    print("in thank you")


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num)

    return stats

def report():
    print("in report")




def quit():
    print("quitting")
    sys.exit()


def main_menu():

    while True:
        answer = input("""What would you like to do?
    Pick one:
    1: Send a Thank You
    2: Create a Report
    3: Quit
    >>>""")
        print("you replied:", answer)
        answer = answer.strip()
        if answer == "1":
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

    donor = ('Barney Rubble', [100, 50, 600])
    assert gen_stats(donor) == ('Barney Rubble', 750, 3, 250.0), str(gen_stats(donor))

    # main_menu()
