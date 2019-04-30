#!/usr/bin/env python3

import sys

print("Mailroom")

donors = [("Fred Flintstone", [100, 200, 50]),
          ("Barney Rubble", [100, 50, 600]),
          ("Wilma Flintstone", [1000, 50, 600, 200]),
          ("Pebbles Flintstone", [10, 5, 6]),
          ]

def Thank_You():
    cash = []
    name = input("Please tell me your name: ")
    cash_input = int(input("Please tell me how much you would like to donate: "))
    cash.append(cash_input)
    donor = (name,cash)
    donors.append(donor)
    print(donor)
    print("Thank you {} for your generous donation.".format(donor[0]))

def gen_stats(donor):
    donations = donor[1]
    total = sum(donations)
    num = len(donations)
    stats = (donor[0], sum(donor[1]), len(donor[1]), sum(donor[1]) / len(donor[1]))
    return stats

def Report():
    header = "{:<20}  |{:^10}  |{:^10}  |{:>10}".format("Donor Name","Total Given","Num Gifts","Average Gift")
    print(header)
    for i in range(len(donors)):
        row = "{:<20}  ${:^10}  {:^10}   ${:>10}".format(donors[i][0],sum(donors[i][1]),len(donors[i][1]),format(sum(donors[i][1])/len(donors[i][1]),".2f"))
        print(row)

def Quit():
    sys.exit()

def main_menu():
    while True:
        answer = input("""
            Please tell me what do you want to do:
            1. Thank you
            2. Report
            3. Quit
            >>> 
            """)
        print("Your reply is ", answer)
        
        answer = answer.strip()
        if answer == "1":
            gen_stats(donor)
            Thank_You()
        elif answer == "2":
            Report()
        elif answer == "3":
            Quit()
        else:
            print("Please input 1,2 or 3")

#main_menu()

if __name__ == "__main__":
    print("Welcome to mailroom!")
    donor = ('Barney Rubble', [100, 50, 600])
    assert gen_stats(donor) == ('Barney Rubble', 750, 3, 250.0)
    main_menu()