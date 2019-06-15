#!/usr/bin/env python3

import sys,os,textwrap,csv
from donor_models import donor_db_collection
from donor_models import donor



def donation_accept():
    donor_name = input("Please tell me your name: ")
    donor_name = donor_name.capitalize()

    try:
        donation_amount =list(int(input("Please tell me how much you would like to donate: ")))


    except ValueError:
        print("Please input a number here!")

    with open("donors.csv","a",newline='') as donor_db:
        donor_db_writer = csv.writer(donor_db)
        donor_db_writer.writerow([donor_name,donation_amount])

    donors.update({donor_name:donation_amount})

    return donor(donor_name,donation_amount).thank_you()

def system_quit():
    sys.exit(1)


def user_selection():

    user_selection = input(textwrap.dedent("""
    Choose an action:

    (1) - I would like to donate.
    (2) - Create a donors collection report.
    (3) - Quit
    >>>"""))

    main_menu = {
        "1":donation_accept,
        "2":donor_db_collection.gen_report,
        "3":system_quit,
        }

    try:
        main_menu[user_selection]
    except KeyError:
        print("Please input a digit from 1,2 or 3")
        user_selection()

    if user_selection == "2":
        main_menu[user_selection](donors)
    else:
        main_menu[user_selection]()


donors = donor_db_collection.from_csv('donors.csv')

while True:
    user_selection()

if __name__ == '__main__':
    main()