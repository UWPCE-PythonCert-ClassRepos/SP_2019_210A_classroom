
#Donors dict Name:[[list of donations],[average of donations]]
donors = {"Chris Christly": [1000, 250], "Bob Barley": [800], "Nick Nilly": [500000, 250000, 750000], "Julia July": [200], "Jose Hooray": [500000, 1000000, 750000]}

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
            print(report())
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
    return ("Donor Name" + " "*10 + "| Total Given " + "| Num Gifts" + "| Average Gift")        


if __name__ == "__main__":
    print("Welcome to the Mailroom!")
    main_menu()