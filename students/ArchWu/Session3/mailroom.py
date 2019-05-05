#!/usr/bin/env python3
import sys
import operator

#donor (Donor name, donations[])
#donors [donor1, donor2]
donors = []
# The data struction used in this program, a list of tuples


def add_donor(name, donation = 0):
    """ Adds a new donor with an initial donation """
    donations = [donation]
    donors.append((name, donations))
    return

def add_donation(name, donation):
    """ Adds a donation to an existing donor """
    for donor, donations in donors:
        if name == donor:
            donations.append(donation)

def report():
    """ Make a report on donations received by a style as specified """
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
    """ A function calculates the total and average donation of a donor """
    name = donor[0]
    donations = donor[1]
    total = round(sum(donations),2)
    num_gifts = len(donations)
    avg = round((total / num_gifts), 2)
    return (name, total, num_gifts, avg)

def thank_you():
    """ Thank-you funcion that generates an email to thank new donations """
    while True:
        answer = input("Please type the Full Name, type quit to go back to previous menu> ")
        if answer == 'list':
            for donor in donors:
                print(donor[0])
        elif answer == 'quit':
            return
        elif answer in [donor[0] for donor in donors]:
            name = answer
            new_user = False
            break
        else:
            name = answer
            new_user = True
            break

    while True:
        amount = input("How much have you just donated? > ")
        if amount == 'quit': return
        try:
            num_donation = float(amount)
        except:
            print("Please type a float number")
        else:
            if new_user:
                add_donor(name, num_donation)
            else:
                add_donation(name, num_donation)
            break
    greetings = 'Dear {},\n'.format(name)
    body = '\nThank you for your generous gift ${} to us!\n'.format(num_donation)
    ending = '\nSincerely,\n  ABC foundations'
    print(greetings + body + ending)
    return

def main_menu():
    """ Main menu function """
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
