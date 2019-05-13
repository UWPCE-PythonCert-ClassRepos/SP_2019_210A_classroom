#!/usr/bin/env python3
import os
import sys
import time
from textwrap import dedent # I took this from the solutions code because I thought it was great

# The names come from dogs that are in my office
donors_list = [("Rufio", [897, 200, 200]),
               ("Maggie", [543, 2, 3000]),
               ("Gus", [23, 32, 33222]),
               ("Kramer", [10, 87, 886]),
               ("Polly", [432, 32, 7896])
               ]


def report():
    print("📊 Generating report...")
    time.sleep(1)  # dramatic effect of creating the report
    print_donor_report()


def print_donor_report():
    report_rows = []
    for (donor_name, gifts) in donors_list:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((donor_name, total_gifts, num_gifts, avg_gift))

    report_rows.sort(key=sort_key, reverse=True)

    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 66)

    for row in report_rows:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))


def print_donors():
    print("\nHere is your list of donors:\n")
    print(f"Donor Names      ")
    print("-" * 12)
    for donor in donors_list:
        print(donor[0])


def get_donor(donor_name):
    for donor in donors_list:
        if donor_name.strip().lower() == donor[0].lower():
            return donor
    return None


def send_thank_you_letter():
    while True:
        print("type 'list' to get a list of donors")
        donor_name = input("Type in the name of a donor: ")

        if donor_name == "list":
            print_donors()
        else:
            break

    while True:
        add_amount = input("Enter an amount to donate: ")
        donated_amount = float(add_amount)
        break

    donor = get_donor(donor_name)

    if donor is None:
        donor = (donor_name, [])
        donors_list.append(donor)

    donor[1].append(donated_amount)
    print(thank_you_letter(donor))


# Just the thank you letter
def thank_you_letter(donor):
    thank_you_letter = f"""
        Hi {donor[0]},

        Your donation of ${donor[1][-1]} has been saved and is greatly appreciated.

        Thank you,
            - Some team that build Mailroom
    """

    return dedent(thank_you_letter)


def sort_key(item):
    donor = get_donor(item[0])
    return sum(donor[1])


def send_letter_to_all_donors():
    """
    Asks to name a directory then creates said directory.donors_list.
    Loops through all donors creatign a txt file for each name.
    Writes their last contribution to the outfile file.
    Moves all files into the directory that was named earlier.
    """
    name_destination_directory = input("Name the directory to save the letters: ")
    os.mkdir(f"./{name_destination_directory}")

    for donor_name in donors_list:
        time.sleep(.5)
        source = f"{donor_name[0]}.txt"
        print(f"✅ Thank you letter created for: {source}")
        print(f"    Check {os.path.abspath(source)}\n")

        outfile = open(f"{source}", "w+")
        outfile.write(thank_you_letter(donor_name))

        while True:
            destination = f"./{name_destination_directory}/"
            os.system(f"mv {source} {destination}")
            break


def quit():
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

        answer_dict = {
            "1": send_thank_you_letter,
            "2": report,
            "3": send_letter_to_all_donors,
            "4": quit,
        }

        answer_dict.get(answer)()


if __name__ == "__main__":
    print("Welcome to the Mailroom.")
    main_menu()
    # send_letter_to_all_donors()
    # quit()
    # report()