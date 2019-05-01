"""
Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.
"""
import sys
donor_db = [("William Gates, III", [653772.32, 12.17]),   
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

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
    donor_name = input("Enter the name of donor or type 'list' if you wish to view the list of donors: ")
                
    #if user types 'list' show the list of donors and prompt to enter donor name
    if donor_name.lower() == 'list':
        while True:
            print(donor_db)
            donor_name = input("Enter the name of donor: ")
            if donor_name != 'list':
                break
            
    found = False
    #if the donor name does not exist in the list, add the donor
    for item in donor_db:
        if item[0] == donor_name:
            found = True
    if found :
        pass
    else:
        donor_db.append((donor_name, []))
            
    #donation amount entered by user
    try:
        donation_amount = float(input("Enter the donation amount: "))
    except:
        donation_amount = float(input("Invalid value. Type a number >>> "))
    
    #match the donor_name and add the donation amount
    for item in donor_db:
        if item[0] == donor_name:
            item[1].append(donation_amount)
        
    print("donor_db",donor_db)
    print (f"Thank you {donor_name} for your generous donation amount of ${donation_amount}" )
    

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

def gen_stats(donor):
	donations = donor[1]
	total_donation = float(format(sum(donations),'.2f'))
	num_donation = len(donations)
	avg_donation = float(format(total_donation/num_donation,'.2f'))
	print("{0:18}      ${1:13}{2:15}     ${3:12}".format(donor[0],total_donation, num_donation,avg_donation))
    
def sort_stats(item):
    return sum(item[1])

def do_createreport():
	print("<<<PRINTING REPORT>>>")
	donor_db.sort(key=sort_stats, reverse = True)
	print("{0:23}|  {1:15}|  {2:12}|  {3:10}".format('Donor Name','Total Given','Num Gifts', 'Average Gifts'))
	print('--------------------------------------------------------------------------')
	for item in donor_db:
		gen_stats(item)
	print('--------------------------------------------------------------------------')
	
def do_quit():
	print("--------Exit----------")
	sys.exit(0)


def main_menu():
    while True:
        answer = input("What would you like to do?\nPick one:\n1: Send a Thank you\n2: Create a report\n3: Quit\n>>>")
        answer = answer.strip()
        if answer == "1":
            do_thankyou()
        elif answer == "2":
            do_createreport()
        else:
            do_quit()

if __name__ == "__main__":
    print("Welcome to mailroom!")
    main_menu()
	
	
	
