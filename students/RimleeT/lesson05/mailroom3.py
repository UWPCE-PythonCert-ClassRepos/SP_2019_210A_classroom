import sys
import os
import tempfile
donor_db = {"William Gates, III": [653772.32, 12.17],   
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
}

"""
Send a Thank You
If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
If the user types 'list' show them a list of the donor names and re-prompt.
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
Add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.
"""	

def do_thankyou():
    print("<<<SEND A THANK YOU>>>")
                
    #if user types 'list' show the list of donors and prompt to enter donor name
    donor_name = None
    while True:
        donor_name = input("Enter the name of donor or type 'list' if you wish to view the list of donors: ")
        if donor_name.lower() == 'list':
            print(donor_db)
        else:
            break
    donation_amount = get_donation_amount() 

    if donor_name not in donor_db:
        donor_db[donor_name] = [donation_amount]
    else:
        donor_db[donor_name].append(donation_amount)
    
    print("donor_db",donor_db)
    print (f"Thank you {donor_name} for your generous donation amount of ${donation_amount}" )

def get_donation_amount():
    try:
        return float(input("Enter the donation amount: "))
    except ValueError:
        print("Invalid value. Type a number.")
        return get_donation_amount()


"""
Create a Report
If the user (you) selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor’s donations, just the summary info.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below).
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
Your report should look something like this:

Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24   
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14
"""

def gen_stats(k,v):
	donations = v
	total_donation = float(format(sum(donations),'.2f'))
	num_donation = len(donations)
	avg_donation = float(format(total_donation/num_donation,'.2f'))
	print("{0:18}      ${1:13}{2:15}     ${3:12}".format(k,total_donation, num_donation,avg_donation))

def do_createreport():
    print("<<<PRINTING REPORT>>>")
    sorted_x = sorted(donor_db.items(), key=lambda item: sum(item[1]), reverse=True)
    print("{0:23}|  {1:15}|  {2:12}|  {3:10}".format('Donor Name','Total Given','Num Gifts', 'Average Gifts'))
    print('-' * 70)
    for key,value in sorted_x :
        gen_stats(key,value)
    print('-' * 70)


def do_sendlettertoalldonors():
    dir_name = tempfile.mkdtemp(prefix = 'Letters-', dir = os.getcwd())
    [sendlettertoalldonors(donor_name, donation_amount, dir_name) for donor_name, donation_amount in donor_db.items()]
    print('Letters saved in your current directory with folder name starting with "Letters"')

def sendlettertoalldonors(donor_name, donation_amount, dir_name):
    total_donation = float(format(sum(donation_amount),'.2f'))
    x = f"Dear {donor_name}\n\n\tThank you for your very kind donation of ${total_donation} It will be put to very good use. \n\nSincerely,  \nThe Team"
    f1 = tempfile.NamedTemporaryFile(prefix = donor_name + '-', dir = dir_name, delete = False)
    f1.write(x.encode())
    

def do_quit():
	print("--------Exit----------")
	sys.exit(0)


def main_menu():
    switch_func_dict = {
        '1': do_thankyou,
        '2': do_createreport,
        '3': do_sendlettertoalldonors,
        '4': do_quit
    }

    while True:
        try:    
            answer = input("What would you like to do?\nPick one:\n1: Send a Thank you\n2: Create a report\n3: Send letters\n4: Quit\n>>>")
            answer = answer.strip()
            option = switch_func_dict[answer]
        except KeyError:
            print("Incorrect option selected!")
            continue
        
        option()

if __name__ == "__main__":
    print("Welcome to mailroom!")
    main_menu()
