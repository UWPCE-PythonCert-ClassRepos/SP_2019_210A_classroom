#!/usr/bin/env python3
import sys
import time
from textwrap import dedent # I took this from the solutions code because I thought it was great

# "{:.>20}".format("${:,.2f}".format(123.3214))

donors_list = [("Rufio", [897, 200, 200]),
               ("Maggie", [543, 2, 3000]),
               ("Gus", [23, 32, 33222]),
               ("Kramer", [10, 87, 886]),
               ("Polly", [432, 32, 7896])
               ]


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num)

    return stats


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
    3: Quit
    >>> """)
        print(f"You selected {answer}")

        answer = answer.strip()
        if answer == "1":
            send_thank_you_letter()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom")
    main_menu()