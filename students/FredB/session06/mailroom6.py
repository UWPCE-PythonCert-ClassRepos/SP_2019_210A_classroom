#Mailroom Part2
#FredBallyns
#Session06

import sys, os

donors = {"Fred Flintstone": [100, 200, 50],
        "James Bond": [0,0,7],
        "Lex Luthor": [5000,],
        "Harambe": [3, 2, 1],
        "Herman Cain": [9, 9, 9]
		}

def clear_screen():
    #Windows 'nt'
    if os.name == 'nt':
        clearText="cls"
    #Linux 'posix'
    else:
        clearText="clear"
    os.system(clearText)


def standard_name(donor_name):
    return donor_name.lower().replace(" ", "")


def requested_list(userEntry):
    return (userEntry.lower() == 'list') or (userEntry.lower() == 'l')


def repeat_donor(donor):
    lower_keys = [standard_name(k) for k in donors.keys()]
    return (standard_name(donor) in lower_keys)

def dict_donor_name(donor):
    for k in donors.keys():
        if standard_name(donor) == standard_name(k):
            return k

def valid_donation(donation):
    return (type(donation) == int) and (donation>0)

def thank_you():
    #print("in thank you")
    donor = input("Enter full name of donor else type 'list' to see donor list: ")
    if requested_list(donor):
        print('\n','Donor List','\n', "------")
        for i in donors.keys():
            print(i)
        return
    elif not repeat_donor(donor):
        new_donor = input("Donor not found. Is this a new donor? (y/n): ")
        if new_donor[0].lower() == "y":
            donors[donor]=[]
        else:
            return
    else:
        print("Donation again :)")
    donation = -1
    while valid_donation(donation)==False:
        print("Must be a positive integer")
        try:
            donation = int(input("Enter donation amount: "))
        except ValueError:
            donation = -1
    donors[dict_donor_name(donor)].append(donation)
    print (f"Thank you {donor} for your generous donation of ${donation} from a charity")



def gen_stats():
    stats=[]
    for donor in donors.keys():
        donations = donors[donor]
        total = sum(donations)
        num = len(donations)
        stats.append((donor, total, num, total / num))
    return stats

def gen_report():
    report_file =  ('Donor Name      | Total Given | Num Gifts   |  Average Gift \n')
    report_file += ('----------------------------------------------------------- \n')
    stats = gen_stats()
    stats = sorted(stats, key=lambda x: x[1], reverse=True)
    for j in stats:
        report_file += ('{:15}   ${:10.2f}{:8}         ${:10.2f} \n'.format(*j))
    return report_file

def print_report():
    print(gen_report())

def send_letters():
    print(os.getcwd())
    letter_template = "Dear {},\n \n Thank you for your very kind donation of ${:.2f}. It will be put to very good use.\n \n Sincerely,\n  -The Team"
    for donor in donors.keys():
        with open((os.getcwd() + "/" + "{}.txt").format(donor), 'w') as new_letter:
            new_letter.write(letter_template.format(donor, sum(donors[donor])))
            new_letter.close()

def quit_program():
    print("quitting")
    sys.exit()

def hello():
    print("Hello")

def main_menu():
    while True:
        choice = input("""What would you like to do?
Please enter a number 1-4:
1: Send a Thank You
2: Create a Report
3: Send letters to all donors
4: Quit
>>>""")
        switcher={
                "1":thank_you,
                "2":print_report,
                "3":send_letters,
                "4":quit_program,
             }
        switcher[choice]()


"""
        #print(answer)
        clear_screen()
        if answer == "1" or answer.lower() == "send a thank you":
            thank_you()
        elif answer == "2" or answer.lower() == "create a report":
            print(gen_report())
        elif answer == "3" or answer.lower() == "send letters to all donors":
            send_letters()
        elif answer == "4" or answer.lower() == "quit":
            quit_program()
        else:
            print("Please follow instructions dummy :)","\n")
"""

if __name__ == "__main__":
    print("Welcome to the mailroom")
    main_menu()