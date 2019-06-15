
from donors_models import Donor, standardize_name, valid_donation
import sys


donors_source = {"Fred Flintstone": [100, 200, 50],
        "James Bond": [0,0,7],
        "Lex Luthor": [5000,],
        "Harambe": [3, 2, 1],
        "Herman Cain": [9, 9, 9]
        }







def main_menu():
    while True:
        choice = input("""What would you like to do?
Please enter a number 1-4:
1: Send a Thank You
2: Create a Report
3: Send letters to all donors
4: Quit
>>>""")
        switcher={
                "1":thank_you,
                "2":print_report,
                "3":send_letters,
                "4":quit,
             }
        switcher[choice]()


if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()