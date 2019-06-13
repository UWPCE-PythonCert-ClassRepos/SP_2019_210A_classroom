


from textwrap import dedent 
import sys, os, math
from donor_models import *


x = [Donor("Luke Skywalker", [100.25, 200.55, 50]),
Donor("Han Solo", [100.80, 50.99, 600]),
Donor("Yoda", [1000.01, 50, 600.55, 200.47]),
Donor ("Ben Kenobe", [101.32, 500, 60.34]),
    ]

donor_db = DonorDb(x)

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

def add_donations():
    """
    Adding donation amount from existing or new donor
    """
    while True:
       
        name = input("Enter a Name (new or existing): \n>> ")
        if name == "":
            print("Name must not be blank space\n")
            return
        try:
            donation_amt = float(input ("Enter donated amount: \n>> "))
            if not donation_amt:
               
                print("""You can not enter a blank value.\nPlease enter a number\n""")
                return
            if math.isnan(donation_amt) or math.isinf(donation_amt) or round(donation_amt, 2) == 0.00:
                print("error: donation amount is invalid\n")
                continue
            else:
                break

        except ValueError:
            print("\nYou must enter a numeric value (ex. 10.99)\n")
            return
        
    donor = Donor(name, donation_amt)
    if donor_db.has_key(donor.key):
        donor_db.add_donation(donor.key, donation_amt)
    else:
        donor_db.add_donor(donor)
    
    print(send_email(name, donation_amt))

def return_to_menu():
    """ Return True to trigger exit out of sub-loop"""
    return True

def exit():
    print("Exiting the Mailroom!")
    sys.exit(0)


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

def run_menu(prompt, selection_dict):
    """
    Main mailroom script using a switch menu to use a dictionary instead of elif statments
    """
    while True:
        selection = input(prompt).strip().lower()
        action = selection_dict.get(selection, None)
        if action is None:
            print("error: menu selection is invalid!")
        else:
            if action():
                # break out of the loop if action returns True
                break



def main(): #added **x to run test 

    donor_db.print_donors()

def show_list():
    """
    shows the donors in the list with donation amounts
    \n"""
    
    list_display = []
    list_display.append("#" * 25 + "The Current Donor List" + "#" * 25)
    index = 1
    for donor_key, donor in donor_db.donor_data.items():
        list_display.append("{:<1}: {:>15}{:>10}: {:<20}".format(index, donor.name, "Amt", str(donor.donations).replace("[","").replace("]","")))
        index += 1
    list_display.append("#" * 75 + "\n")
    return "\n".join(list_display)

def print_donor_list():
    print(show_list())
    print()

def print_report():
    print(donor_db.create_report())

def mailroom_main():
    
    """
    Run the main menu for mailroom
    """
    prompt = dedent("""
                    Choose an action:

                    (1) - Send a Thank You
                    (2) - Create a Report
                    (3) - Send letters to everyone
                    (4) - Quit

                    > """)

    selection_dict = {"1": send_thank_you,
                      "2": print_report,
                      "3": donor_db.save_letters,
                      "4": exit}
    
    run_menu(prompt, selection_dict)

if __name__ == "__main__":
    main()
    mailroom_main()

'''
def clear_screen():
    """
    clears the command screen
    """
    os.system("cls" if os.name == "nt" else "clear")












  


    
if __name__ == "__main__": 

    donors_db = main_donors_db()

    mailroom_main()


if __name__ == "__main__":
    main()'''