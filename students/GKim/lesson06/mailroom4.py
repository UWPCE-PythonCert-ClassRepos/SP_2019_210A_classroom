#!/usr/bin/env python

from textwrap import dedent 
import sys, os, math

def main_donors_db():
    x = {
            "Luke Skywalker": [100.25, 200.55, 50],
            "Han Solo": [100.80, 50.99, 600],
            "Yoda": [1000.01, 50, 600.55, 200.47],
            "Ben Kenobe": [101.32, 500, 60.34],
            }
    return x
# donors_db = [
#             {"name": "Luke Skywalker", "donations": [100.25, 200.55, 50]},
#             {"name": "Han Solo", "donations": [100.80, 50.99, 600]},
#             {"name": "Yoda", "donations": [1000.01, 50, 600.55, 200.47]},
#             {"name": "Ben Kenobe", "donations": [101.32, 500, 60.34]},
#             ]

def clear_screen():
    """
    clears the command screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_list():
    """
    shows the donors in the list with donation amounts
    \n"""
    
    list_display = []
    list_display.append("#" * 25 + "The Current Donor List" + "#" * 25)
    index = 1
    for key, val in donors_db.items():
        list_display.append("{:<1}: {:>15}{:>10}: {:<20}".format(index, key, "Amt", str(val).replace("[","").replace("]","")))
        index += 1
    list_display.append("#" * 75 + "\n")
    return "\n".join(list_display)

def print_donor_list():
    print(show_list())
    print()




def send_email(name, amount):
    """
    This functions sends a letter to an individual donor
    """
    return dedent("""\n
    Dear {n},
       Thank you for your generous donation of ${a}! This will help our cause
       immensely in our battle against the darkside.  You, {n} , have made a big 
       difference in our efforts and we greatly appreciate you!!!  Your ${a} will be 
       put to great use to our forces against evil!  

       Thank you,

       The FORCE
    
    \n""".format(n = name, a = amount))



def donor_name(name):
    """
    Function finds donor in donor db
    """
    key = name.title().strip()
    return donors_db.get(key) 

def add_donor(name):
    """
    Function adds a new donor to the donor
    """
    name = name.title().strip()
    new_donor = donors_db[name] = []
    return new_donor

def add_donations():
    """
    Adding donation amount from existing or new donor
    """
    while True:
        clear_screen()
        name = input("Enter a Name (new or existing): \n>> ")
        if name == "":
            print("Name must not be blank space\n")
            return
        try:
            donation_amt = input ("Enter donated amount: \n>> ")
            if not donation_amt:
                clear_screen()
                print("""You can not enter a blank value.\nPlease enter a number\n""")
                return
            amount = float(donation_amt)    
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                print("error: donation amount is invalid\n")
                continue
            else:
                break

        except ValueError:
            clear_screen()
            print("\nYou must enter a numeric value (ex. 10.99)\n")
            return
        
    donor = donor_name(name)
    if donor is None :
        donor = add_donor(name)
    
    donor.append(amount)
    print(send_email(name.title(), amount))


def create_report():
    """
    Generates the report of donors by donation amount from greatest to least
    """
    donor_stats = []
    for key, val in donors_db.items():
        total = sum(val)
        num = len(val)
        avg = round(total / num, 2)
        stats = [key, total, num, avg]
        donor_stats.append(stats)

    stats_list = donor_stats
    stats_list.sort(key=lambda stats_list: stats_list[1],reverse=True)
    report = []
    report.append("{:<20}|{:^15}|{:^15}|{:>15}".format("Donor Name", 
                                               "Total Given",
                                               "Num Gifts",
                                               "Average Gifts"))
    report.append("-" * 68)
    for row in stats_list:
        report.append("{:<20}${:>15.2f} {:>15} ${:>15.2f}".format(*row))
    report.append("\nEnd of Report\n")
    return "\n".join(report)  

def print_report():
    print(create_report())

def save_letters():
    """
    Saves letters to disk of all donors in data base
    """

    for key, val in donors_db.items():   
        file_name = key.replace(" ", "_") + ".txt"
        letter =  send_email(key, val[-1])
        with open(file_name, "w") as text_file:
            text_file.write(letter)   
            print("\nSaving {} file to disk".format(key))
    print("\nSAVING COMPLETE\n")

def return_to_menu():
    ''' Return True to trigger exit out of sub-loop'''
    return True

def quit():
    print("Exiting the Mailroom!")
    sys.exit()



def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    prompt = ("'Send a Thank You' Menu Options:\n\n"
              "1: Update donor and send 'Thank-You'\n"
              "2: List all existing DONORS\n"
              "3: Return to Main Menu\n > ")
    selection_dict = {"1": add_donations,
                      "2": print_donor_list,
                      "3": return_to_menu,
                      }
    run_menu(prompt, selection_dict)

def mailroom_main():
    
    """
    Run the main menu for mailroom
    """
    prompt = dedent('''
                    Choose an action:

                    (1) - Send a Thank You
                    (2) - Create a Report
                    (3) - Send letters to everyone
                    (4) - Quit

                    > ''')

    selection_dict = {"1": send_thank_you,
                      "2": print_report,
                      "3": save_letters,
                      "4": quit}
    
    run_menu(prompt, selection_dict)

def run_menu(prompt, selection_dict):
    """
    Main mailroom script using a switch menu to use a dictionary instead of elif statments
    """
    while True:
        selection = input(prompt).strip().lower()
        clear_screen()
        action = selection_dict.get(selection, None)
        if action is None:
            clear_screen()
            print("error: menu selection is invalid!")
        else:
            if action():
                # break out of the loop if action returns True
                break
  
if __name__ == "__main__": 

    donors_db = main_donors_db()

    mailroom_main()