#! /usr/bin/env python3
"""
The Mailroom Program : Part 1
Author : Joe Nunnelley
"""
import sys

def send_thankyou():
    print('Sending a Thank You')
    pass
    print()
    print()


def print_report():
    print('Printing Report')
    pass
    print()
    print()

def quit():
    print('Mailroom Closing...')
    print()
    sys.exit(0)


def main_menu():
    response = input(
    """
    What would you like to do?
    Pick one:
        1.) Send a Thank You
        2.) Create a Report
        3.) Quit
    >>>
    """)

    print("You chose: {}".format(response))

    if response == "1":
        send_thankyou()
    elif response == "2":
        print_report()
    elif response == "3":
        quit()
    else:
        print("Invalid input. Please refer to instructions")

def run():
    """
    the entry point for the program
    """
    print("Starting Mailroom...")
    donors = [("George Jetson", [100, 50, 200]),
              ("Bugs Bunny", [400, 55, 5000]),
              ("Daffy Duck", [0, 3, 5, 6, 76, 8]),
              ("Elmer Fudd", [66, 666, 6666, 6666, 66666,]),
              ("Porky Pig", [0.50, 56.45, 67.89])]

    while True:
        main_menu()


if __name__ == "__main__":
    run()
