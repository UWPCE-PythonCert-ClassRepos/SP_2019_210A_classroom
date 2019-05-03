#!/usr/bin/env python3
import sys
import time

# "{:.>20}".format("${:,.2f}".format(123.3214))

donors_list = [("Rufio", [897, 200, 200]),
               ("Maggie", [543, 2, 3000]),
               ("Gus", [23, 32, 33222]),
               ("Kramer", [10, 87, 886]),
               ("Polly", [432, 32, 7896])
               ]


def thank_you():
    find_donor()


def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], total, num, total / num)

    return stats


def report():
    print("Generating report...")
    time.sleep(1)  # dramatic effect of creating the report
    generate_report_template()
    # gen_stats(donor)


def generate_report_template():
    donor_name = "Donor Name"
    total_given = "Total Given"
    num_gifts = "Num Gifts"
    average_gift = "Average Gift"

    print(f"{donor_name}           |  {total_given}   |  {num_gifts}   |  {average_gift}")
    print("-" * 68)

    donor_name_row = []
    for donor in donors_list:
        donor_name_row.append(donor[0])
        print(f"{donor_name_row[0]}")


def find_donor():
    print("Type 'List' to get a list of donors")
    donor_name = input("Type in the name of a donor: ").title()

    if donor_name == "List":
        print("\nHere is your list of donors:\n")
        print(f"Donor Names      ")
        print("-" * 12)
        for donor in donors_list:
            print(f"{donor[0]}")
        print()
    else:
        for donor in donors_list:
            if donor_name == donor[0]:
                print(f"Found donor: {donor_name}")
        else:
            donors_list.append(donor_name.title())
            print(f"Adding {donor_name} to the list of donors.")


def quit():
    print("Quitting Mailroom...")
    time.sleep(.5)
    print("Goodbye")
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
            thank_you()
        elif answer == "2":
            report()
        elif answer == "3":
            quit()
        else:
            print("Please answer 1, 2, or 3")


if __name__ == "__main__":
    print("Welcome to the Mailroom")

    donor = ("fred flinstone"), [100, 50, 600]
    # assert gen_stats(donor) == ("fred flinstone"), [750, 3, 250.0]

    main_menu()
