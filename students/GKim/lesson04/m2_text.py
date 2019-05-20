#!/usr/bin/env python

from textwrap import dedent 
import sys, os


main_donors = [
          {"name": "Luke Skywalker", "donations": [100.25, 200.55, 50]},
          {"name": "Han Solo", "donations": [100.80, 50.99, 600]},
          {"name": "Yoda", "donations": [1000.01, 50, 600.55, 200.47]},
          {"name": "Ben Kenobe", "donations": [101.32, 500, 60.34]},
]

def clear_screen():
    """
    clears the command screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_list():
    """
    shows the donors in the list with donation amounts
    \n"""
    print("#" * 25, "The Current Donor List", "#" * 25)
    index = 1
    for row in main_donors:
        print("{:<1}: {:>15}{:>10}: {:<20}".format(index, row["name"], "Amt", str(row["donations"]).replace("[","").replace("]","")))
        index += 1
    print("#" * 75 + "\n")
    return show_list

def main_menu():
    """
    Main menu options
    """
    prompt = input("\n".join(("\nWelcome to the Mailroom!",
"Please choose from one of the options below:\n",
"1: Send a Thank You",
"2: Create a Report",
"3: Send to All",
"4: Quit",
">>> ")))
    return prompt



def menu_thank_you():
    """
    Menu to user to enter options for thank you
    """
    print("""\nTo whom would you like to send a Thank You?
Please enter full name""")
    thanks_answer = input("""
Enter 'LIST' to see Donor list or 'MENU' to return to Main Menu.
>>> """)
    return thanks_answer


def send_email(name, amount):
    """
    This functions sends a letter to an individual donor
    """
    print("""\n
    Dear {n},
       Thank you for your generous donation of ${a}! This will help our cause
       immensely in our battle against the darkside.  You, {n} , have made a big 
       difference in our efforts and we greatly appreciate you!!!  Your ${a} will be 
       put to great use to our forces against evil!  

       Thank you,

       The FORCE
    
    \n""".format(n = name, a = amount))

def send_letter(name, amount):
    """
    This function can send a letter to all but mainly to write to file
    """
    return dedent(''' 
          Dear {},
            Thank you for your very kind donations totaling ${:,.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Force
          '''.format(name, amount))
   

def send_thank_you():
    """
    Either adds to list or adds a new donor to the list and  a 
    new donation amount 
    """
    clear_screen()
    while True:
        thanks_answer = menu_thank_you().strip()
        if thanks_answer.upper() == "LIST":
            clear_screen()
            show_list()
        elif thanks_answer.upper() == "MENU":
            clear_screen()
            break
        else:
            idx = len(main_donors)-1
            in_main_donors = False
            for x in range(len(main_donors)-1, -1, -1):
                if main_donors[x].get("name").lower() == thanks_answer.lower():
                    in_main_donors = True
                    print("\nThe Donor you have selected is {}".format(thanks_answer))
                    donation_amount = float(input("\nPlease enter the amount that {} kindly donated: ".format(thanks_answer)))
                    main_donors[idx]["donations"].append(donation_amount)
                    print("{}: ${:.2f}".format(thanks_answer, donation_amount))
                idx -= 1
            
            if in_main_donors == False:
                donation_amount = float(input("\nPlease enter {}'s donated amount: ".format(thanks_answer)))
                add_new_donors = {"name": thanks_answer, "donations": [donation_amount]}
                main_donors.append(add_new_donors)
                print("{} was added with a donation of ${:.2f}".format(thanks_answer,float(donation_amount)))
            
            send_email(thanks_answer, donation_amount)



def report_menu():
    """
    Menu for Create a Report and to give the user an option to exit
    """
    report_menu_answer = input(""" 
    Welcome to the 'Create a Report option'!
Enter 'MENU' to exit and return to the Main Menu
Press Enter to continue
 >>>  """)

    return report_menu_answer


def gen_stats(lst):
    donor_stats = []
    for donor in lst:
        donations = donor["donations"]
        total = sum(donations)
        num = len(donations)
        avg = round(total / num, 2)
        stats = [donor["name"], total, num, avg]
        donor_stats.append(stats)

    return donor_stats

def create_report():
    """
    Generates the report of donors by donation amount from greatest to least
    """
    while True:
        response = report_menu().strip()
        if response.upper() == "MENU":
            break
        else:
            clear_screen()
            stats_list = gen_stats(main_donors)
            stats_list.sort(key=lambda stats_list: stats_list[1],reverse=True)
            
            print("{:<20}|{:^15}|{:^15}|{:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
            print("-" * 68)
            for donor in stats_list:
                print("{:<20}${:>15} {:>15} ${:>15}".format(donor[0], donor[1], donor[2], donor[3]))
            print("\nEnd of Report\n")    

def save_letters():
    """
    Saves letters to disk of all donors in data base
    """

    for donor in main_donors:   
        file_name = donor["name"].replace(" ", "_") + ".txt"
        letter =  send_letter(donor["name"], donor["donations"][-1])
        with open(file_name, "w") as text_file:
            text_file.write(letter)   
            print("\nSaving {} file to disk".format(donor["name"]))
    print("\nSAVING COMPLETE\n")

def quit():
    print("You are leaving the Mailroom!")
    sys.exit()

def mailroom_main():
    """
    Main mailroom script using a switch menu to use a dictionary instead of elif statments
    """
    switch_menu = {"1": send_thank_you, "2": create_report, "3": save_letters, "4": quit}
            
    while True:
        if:
            answer = main_menu()
            switch_menu.get(answer)()
        else:
            print("Please choose a number 1-4")


# def main():
#     mailroom_main()

if __name__ == "__main__": mailroom_main()