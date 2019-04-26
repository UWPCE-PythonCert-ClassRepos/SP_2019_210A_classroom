
#Donors dict Name:[[list of donations],[average of donations]]
donors = {"Chris Christly": [1000, 250], "Bob Barley": [800], "Nick Nilly": [500000, 250000, 750000], "Julia July": [200], "Jose Hooray": [500000, 1000000, 750000]}


if __name__ == "__main__":
    print("Welcome to the Mailroom!")

def main_menu():
    while True:
        answer = input("""What would you like to do?
            1: Send a thank you
            2: Create a Report
            3: Quit
            >>>""").strip()
        if answer == "1":
            #Call thank you function
            thank_you()
        elif answer == "2":
            #calls report function
            pass
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
            #Send a thank you report
            break
        elif name_input == "list":
            for name in donors.keys(): print(name)
        else:
            new_name_decision = input(name_input + " not found, would you like to add a new donator? y/n \n>>>").strip()
            if new_name_decision.lower() == "y":
                donors.update({name_input:input("Please enter a donation amount: >>> ")})
                print(donors)
            break
    

def report():
    pass

def add_donation():
    '''
    requests input from the user for a list of donations and returns this when done
    '''
    lst = []
    while True:
        lst.append(float(input("Please enter a donation amount >>>"))) #need a method to make sure it's a number
        if input("Would you like to enter another amount? y/n >>>") != "y":
            return lst


main_menu()