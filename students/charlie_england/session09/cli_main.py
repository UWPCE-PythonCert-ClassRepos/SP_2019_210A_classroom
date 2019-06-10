from donor_models import Donor_Collection
from donor_models import Donor
import sys

def thank_you(donor_collection,new_don=None):
    """
    Tries to gather name input and donation info before reaching out to Donor and and Dono_Collection functions to add a new donation amount
    will also print a list of the current donor names if requested, allows the user to quit back to main menu
    new don will be a Donor class from another function so that this code can be used later
    will check to see if the name is currently in the donors by using the search donor function
    """
    while True:
        if not new_don:
            name_choice = input("Please input a name of an existing donor, enter 'l' for a list of donors, 'q' to go back to previous menu\n>>> ")
            norm_name_choice = name_choice.lower().strip().replace(" ","")
        else:
            norm_name_choice = new_don.lower().strip().replace(" ","")
        if donor_collection.search_donor(norm_name_choice) or new_don:
            while True:
                try:
                    donation_amt = float(input(f"Please enter a donation amount for {donor_collection.donor_data[norm_name_choice].name}\n>>> "))
                    break
                except ValueError:
                    print("That was an invalid, please try again, 'q' to head back to main menu")
            donor_collection.donor_data[norm_name_choice].add_donation(donation_amt)
            print(donor_collection.donor_data[norm_name_choice].send_thank_you())
            return donor_collection
        elif name_choice == "l":
            for donor in donor_collection.donor_data.values():
                print(donor.name)
        elif name_choice == "q":
                return donor_collection
        else:
            print(f'Could not find donor by the name of {name_choice}')

def thank_you_new(donor_collection):
    """
    Create a donor, and then send a thank you (use logic from the thank_you function, send new_don =instance of Donor class with the user inputted name)
    """
    while True:
        usr_name_input = input("Input a name of a new donor, 'q' to head back to main menu\n>>> ")
        norm_usr_name = usr_name_input.lower().strip().replace(" ","")
        if donor_collection.search_donor(norm_usr_name):
            print(f"{usr_name_input} already in donors, please select a new name")
        elif usr_name_input == "q":
            return donor_collection
        else:
            break
    donor_collection.add_donor(Donor(usr_name_input))
    thank_you(donor_collection,new_don=usr_name_input)


def create_report(donor_collection):
    """
    reached out to the Donor_Collection instance of the donor_data and uses the gen_reports function to get a list and prints this out.
    """
    report_list = donor_collection.gen_report()
    for line in report_list:
        print(line)

def send_letters(donor_collection):
    """
    uses the Donor_Collection class to get a list back and will create a file named donor_name.txt and writes the letter to this list
    """
    for letter in donor_collection.send_letters():
        file_name = f"{letter[1]}.txt"
        with open(file_name, "w") as fh:
            fh.writelines(letter[0])
        print(f'Created letter for {letter[1]}')
        fh.close()
    print("Finished!")

def halt(pos_arg):
    """
    Quit..
    """
    print('quitting...')
    sys.exit()

def main():
    """
    main function which contains the switch_case dictionary
    tests to make sure the user input a correct entry
    """
    # d1 = Donor("Jeff Bezos",[1000,500,20])
    # d2 = Donor('blue berry',[1233,513])
    donor_collection = Donor_Collection()
    switch = {
        "1":thank_you,
        "2":thank_you_new,
        "3":create_report,
        "4":send_letters,
        "5":halt
    }
    
    while True:
        choice = input("""What would you like to do?
            1: Send a Thank You to a single existing donor
            2: Send a Thank You to a new donor
            3: Create a Report
            4: Send letters to all donors
            5: Quit
            >>> """).strip()
        if choice not in switch.keys():
            print(f'You input {choice}, please input 1 through 5')
        else:
            switch[choice](donor_collection)



if __name__=="__main__":
    while True:
        main()