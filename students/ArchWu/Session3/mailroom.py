#!/usr/local/bin/python3
import sys

donors = []

def add_donor():
    return
def get_donor():
    return
def report():
    return

def gen_stats(donor):
    name = donor[0]
    donations = donor[1]
    total = sum(donations)
    avg = total / len(donations)
    return (name, total, avg)

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

    quit = False
    # while(quit):
    #     #do something
    #     add_donor()
    # return

if __name__ == '__main__':
    print("Welcome to the mailroom!")
    main_menu()
