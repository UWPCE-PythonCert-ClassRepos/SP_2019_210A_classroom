import math
#Donors dict Name:[[list of donations],[average of donations]]
donors = {"Chris Christly": [1000.21, 250.80], "Bob Barley": [800.33], "Nick Nilly": [500000.12, 250000.55, 750000], "Julia July": [200.80], "Jose Hooray": [500000, 1000000, 750000]}

def main_menu():
    '''
    Main menu for the program.
    Will loop through and requests input until 3 is entered and then quits.
    1 will allow an addition of a donator, a new donation and the printing of a thank you later
    2 will print a report of the donators and their donations as well as their average donation.
    '''
    while True:
        answer = input("""What would you like to do?
            1: Send a thank you
            2: Create a Report
            3: Quit
            >>>""").strip()
        if answer == "1":
            #Call thank you function
            print(thank_you())
        elif answer == "2":
            #calls report function
            for line in report():
                print(line)
        elif answer == "3":
            print("Quitting...")
            break
        else:
            print(("You replied {}, please reply with 1, 2 or 3").format(answer))

def thank_you():
    while True:
        name_input = input("Please enter a full name, 'list' for list of names \n>>>").strip()
        if name_input in donors.keys():
            donors[name_input].append(float(input("Please enter a donation amount: >>> ")))
            return compose_thank_you(name_input)
        elif name_input == "list":
            for name in donors.keys(): print(name)
        else:
            new_name_decision = input(name_input + " not found, would you like to add a new donator? y/n \n>>>").strip()
            if new_name_decision.lower() == "y": 
                donors.update({name_input:[input("Please enter a donation amount: >>> ")]})
                return compose_thank_you(name_input)
    
def compose_thank_you(name_input):
    return (
        """Dear {},\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your ${} donation.\n
        Without people like you we could not coninue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """.format(name_input,int(donors[name_input][-1])))

def report():
    report_list = ["Donor Name" + " "*10 + "| Total Given " + "| Num Gifts " + "| Average Gift\n" + "-"*59]
    for donor in donors:
        donor_sum = round(sum(donors[donor]),2)
        donor_num_gifts = len(donors[donor])
        donor_average = round(donor_sum/donor_num_gifts,2)
        #used variables even though it can be fit into 1 line for readability
        #report list is: Donor + White Space + Donor Sum + white space + num gifts + white space + donor average. amount of white space changes on length of donor items
        report_list.append(donor + " "*(21-len(donor)) + "$" +" "*(11-len(str(donor_sum))) + str(donor_sum) + " "*(13-len(str(donor_num_gifts))) + str(donor_num_gifts) + " "*(13-len(str(donor_average))) + str(donor_average))
    return report_list

if __name__ == "__main__":
    print("Welcome to the Mailroom!")
    main_menu()