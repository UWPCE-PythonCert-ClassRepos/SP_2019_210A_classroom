#!/usr/bin/env python3
#refactor to have the donors dict be 2 lists

# Donors dict Name:[[list of donations],[average of donations]]
donors = {"Chris Christly": [[1000.21, 250.80],[]], "Bob Barley": [[800.33],[]], "Nick Nilly": [[
    500000.12, 250000.55, 750000],[]], "Julia July": [[200.80],[]], "Jose Hooray": [[500000, 1000000, 750000],[]]}


def main_menu():
    '''
    Main menu for the program.
    Will loop through and requests input until 3 is entered and then quits.
    1 will allow an addition of a donator, a new donation and the printing of a thank you letter
    2 will print a report of the donators and their donations as well as their average donation.
    '''
    while True:
        answer = input("""What would you like to do?
            1: Send a thank you
            2: Create a Report
            3: Quit
            >>>""").strip()
        if answer == "1":
            # Call thank you function and then print the return statement
            print(thank_you())
        elif answer == "2":
            # calls report function which returns a list and then prints every line in the list
            for line in report():
                print(line)
        elif answer == "3":
            print("Quitting...")
            break
        else:
            # if the item is not 1, 2, or 3, will print this and go back to beginning of while loop
            print(f"You replied {answer}, please reply with 1, 2 or 3")


def thank_you():
    """
    will ask for a name input or a list.
    Will print a list of names if list is entered
    If name is in the dict, will ask for a donation amount, if name is not in dict, will ask if you would like to add a new name and will ask for a donation amount
    """
    while True:
        name_input = input(
            "Please enter a full name, 'list' for list of names \n>>>").strip()
        if name_input in donors.keys():
            # Ask for donation amount and append to key in dict
            donors[name_input][0].append(
                float(input("Please enter a donation amount: >>> ")))
            # Call compose thank you function and return breaking the loop
            return compose_thank_you(name_input)
        elif name_input == "list":
            for name in donors.keys():
                print(name)
        else:
            # if the name_input was not list and was not already in the donors dict, will ask if the user wants to add
            new_name_decision = input(
                name_input + " not found, would you like to add a new donator? y/n \n>>>").strip()
            if new_name_decision.lower() == "y":
                donors.update(
                    {name_input: [[int(input("Please enter a donation amount: \n>>>"))],[]]})
                return compose_thank_you(name_input)


def compose_thank_you(name_input):
    return (
        """Dear {},\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your ${} donation.\n
        Without people like you we could not continue blah blah blah\n
        Again thank you\n
    Sincerely,\n
        Local Charity """.format(name_input, int(donors[name_input][0][-1])))


def report():
    """
    return a report by adding a line for every name in the donor dictionary
    """
    report_list = ["Donor Name" + " "*10 + "| Total Given " +
                   "| Num Gifts " + "| Average Gift\n" + "-"*60]
    for donor in donors:
        donors[donor][1].append(round(sum(donors[donor][0]),2))
        donors[donor][1].append(len(donors[donor][0]))
        donors[donor][1].append(round(round(sum(donors[donor][0]), 2)/len(donors[donor][0]), 2))
        # used variables even though it can be fit into 1 line for readability
        # report list is: Donor + White Space + Donor Sum + white space + num gifts + white space + donor average. amount of white space changes on length of donor items
        #report_list.append(donor + " "*(21-len(donor)) + "$" +" "*(11-len(str(donor_sum))) + str(donor_sum) + " "*(13-len(str(donor_num_gifts))) + str(donor_num_gifts) + " "*(13-len(str(donor_average))) + str(donor_average))
        report_list.append(
            f"{donor:<20} $  {donors[donor][1][0]:>10} {donors[donor][1][1]:^12} $ {donors[donor][1][2]:>10}")
    return report_list


if __name__ == "__main__":
    print("Welcome to the Mailroom!")
    main_menu()
