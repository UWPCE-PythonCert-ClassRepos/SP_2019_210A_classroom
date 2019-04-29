#!/usr/local/bin/python3
import sys
import operator

#donor (Donor name, donations[])
#donors [donor1, donor2]
donors = []

def add_donor(name):
    donations = []
    return (name, donations)

def report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("------------------------------------------------------------------")
    donors.sort(reverse = True, key = lambda item: (sum(item[1])))
    for donor in donors:
        name, total, num_gifts, avg = gen_stats(donor)
        part_1 = "{}{}".format(name, ' ' * (27 - len(name)))
        part_2 = "${}{}".format(' ' * (11 - len(str(total))), total)
        part_3 = "{}{}{}{}{}".format(' ' *(12 - len(str(num_gifts))), num_gifts,'  $', ' ' * (12 - len(str(avg))), avg)
        result = part_1 + part_2 + part_3
        print(result)
    return

def gen_stats(donor):
    name = donor[0]
    donations = donor[1]
    total = round(sum(donations),2)
    num_gifts = len(donations)
    avg = round((total / num_gifts), 2)
    return (name, total, num_gifts, avg)

def thank_you():

def main_menu():
    while True:
        answer = input("""What would you like to do?
Pick one:
1: Send a Thank you
2: Create a report
3: Quit
""")
        print("You replied:", answer)
        answer = answer.strip()
        if answer == '1':
            thank_you()
        elif answer == '2':
            report()
        elif answer == '3':
            sys.exit(0)
        else:
            print("please answer 1, 2 or 3")

if __name__ == '__main__':
    donors = [('William Gates, III', [100000, 800227.556]), ('Mark Zuckerberg', [10000, 8697.67]), ('Jeff Bezos', [100, 1255]), ('Paul Allen', [100, 200, 3000, 5000, 10000])]
    print("Welcome to the mailroom!")
    main_menu()
