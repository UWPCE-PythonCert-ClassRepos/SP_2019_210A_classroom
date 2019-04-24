
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
    nameinput = input("Please enter a full name, 'list' for list of names \n>>>").strip()
    if nameinput in donors.keys():
        print("name in keys")

def report():
    pass

main_menu()