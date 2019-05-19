#!/usr/bin/env python3
import os
import sys
import time
import shutil
from textwrap import dedent


donors_list = {"Rufio": ("Rufio", [897, 200 , 200]),
               "Maggie": ("Maggie", [543, 2, 3000]),
               "Gus": ("Gus", [23, 32, 33222]),
               "Kramer": ("Kramer", [10, 87, 886]),
               "Polly": ("Polly", [432, 32, 7896]),
              }


def report():
    print("📊 Generating report...")
    time.sleep(1)  # dramatic effect of creating the report
    print_donor_report()


def print_donor_report():
    report_rows = []
    for (donor_name, gifts) in donors_list.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((donor_name, total_gifts, num_gifts, avg_gift))

    report_rows.sort(key=sort_key, reverse=True)

    print("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)

    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))


def print_donors():
    print("\nHere is your list of donors:\n")
    print("{:6s}".format("Donor Name"))
    print("-" * 12)
    for donor in donors_list:
        print(donor)


def get_donor(donor_name):
    key = donor_name.strip().lower()

    return donors_list.get(key)


def add_donor(donor_name):
    donor_name = donor_name.strip()
    donor = (donor_name, [])
    donors_list[donor_name.lower()] = donor

    return donor


def send_thank_you_letter():
    while True:
        print("type 'list' to get a list of donors or 'exit' to go back to the main menu")
        donor_name = input("Type in the name of a donor: ")

        if donor_name == "list":
            print_donors()
        elif donor_name == "exit":
            main_menu()
        else:
            break

    while True:
        try:
            add_amount = input("Enter an amount to donate: ")
            donated_amount = float(add_amount)
            break
        except ValueError:
            print(f"\n‼️  '{add_amount}' is not a valid number. Please enter a valid number\n")

    donor = get_donor(donor_name)

    if donor is None:
        donor = add_donor(donor_name)

    donor[1].append(donated_amount)
    print(thank_you_letter(donor))


def thank_you_letter(donor):
    thank_you_letter = f"""
        Hi {donor[0]},

        Your donation of ${donor[1][-1]} has been saved and is greatly appreciated.

        Thank you,
            - Some team that build Mailroom
    """

    return dedent(thank_you_letter)


def sort_key(item):
    return item[1]


def send_letter_to_all_donors():
    """
    Asks to name a directory then creates said directory.donors_list.
    Loops through all donors creatign a txt file for each name.
    Writes their last contribution to the outfile file.
    Moves all files into the directory that was named earlier.
    """
    name_destination_directory = input("Name the directory to save the letters: ")
    os.mkdir(f"./{name_destination_directory}")

    for donor_name in donors_list.values():
        time.sleep(.5)
        source = f"{donor_name[0]}.txt"
        print(f"✅ Thank you letter created for: {source}")
        print(f"    Check {os.path.abspath(source)}\n")

        outfile = open(f"{source}", "w+")
        outfile.write(thank_you_letter(donor_name))

        while True:
            try:
                destination = f"./{name_destination_directory}/"
                shutil.move(source, destination)
            except FileExistsError:
                print(f"‼️ already exists, please try again.")
            break


def quit_mailroom():
    print("Quitting Mailroom...")
    time.sleep(.5)
    print("Goodbye 👋")
    sys.exit(0)


def main_menu():
    while True:
        answer = input(""" -> What you would you like to do?
    Pick One:
    1: Send a thank you
    2: Create a report
    3: Send letters to ALL donors
    4: Quit
    >>> """)
        print(f"You selected {answer}")

        answer = answer.strip()

        try:
            answer_dict = {
                "1": send_thank_you_letter,
                "2": report,
                "3": send_letter_to_all_donors,
                "4": quit_mailroom,
            }

            answer_dict.get(answer)()
        except TypeError:
            print(f"\n‼️  ️{answer} is not a valid option, please select from 1, 2, 3 or 4\n")


if __name__ == "__main__":
    print("Welcome to the Mailroom.")
    main_menu()
    # send_letter_to_all_donors()
    # quit()
    # report()
    # get_donor("Rufio")