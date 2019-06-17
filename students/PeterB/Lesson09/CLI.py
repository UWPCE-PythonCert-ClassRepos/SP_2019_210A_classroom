#!/usr/bin/env python3

import sys
from Lesson9mailboxmoneyOO import Donor
from Lesson9mailboxmoneyOO import DonorDB


DONOR_DICT = d.DonorDB()
DONOR_DICT.add(d.Donor("Road Runner", [4839283.32, 17842102.94]))
DONOR_DICT.add(d.Donor("Shawn Michaels", [55303.04, 5000.08, 300.03]))
DONOR_DICT.add(d.Donor("Sasuke Uchiha", [80040033.32]))
DONOR_DICT.add(d.Donor("Frieza", [0.50, 1.75, 2000.25]))


def send_thanks():
    selected_donor = prompt_for_donor()

    if selected_donor:
        for donor in DONOR_DICT.donors:
            if selected_donor.name == donor.name:
                donor.donations.extend(add_donations())

        print(f'\nSending a Thank You to {donor.name}...\n')
        formulate_mail(donor)
        print()


def gen_report(name, amount):
    return dedent("""\n
Dear {n},
   Thank you for your donation of ${a}! Your ${a} will be 
   used to help many people!  

   Thank you,

\n""".format(n=name, a=amount))


def goodbye():
    print("Goodbye!\n")
    sys.exit(2)


def main():
    """main CLI loop"""
    switch = {
                 "1": Send_Thanks,
                 "2": gen_report,
                 "3": goodbye,
    }
    while True:
        try:
            choice = input("select 1 - 3 > ")
            if choice not in switch.keys():
                print("please select 1 - 3")
            else:
                switch[choice]()
        except SystemExit as e:
            return


if __name__ == "__main__":
    main()
